#!/usr/bin/env python3
"""Confere a coerência entre os artefatos de uma contratação em artefatos_ia/.

Referência: o Mapa de Preços (06-Mapa-de-Precos.xlsx, abas Itens e Mapa).
Para cada documento .docx (DFD, ETP, TR, Edital, Minuta de Contrato, MGR, Relatórios), verifica:
  - pendências esquecidas: [PREENCHER...], campos <...> do template, linhas de EXEMPLO;
  - se o valor total estimado do Mapa aparece no ETP, no TR e no Edital (salvo --sigiloso);
  - se, para cada item, o código CATMAT/CATSER e a quantidade aparecem no TR e no Edital,
    e a quantidade aparece no ETP.

Uso:
  python3 verificar_coerencia.py projetos/<projeto> [--sigiloso] [--saida pareceres/verificacao-coerencia.md]

O Mapa de Preços precisa estar recalculado (valores em cache). Se os valores vierem vazios,
rode antes: python3 /mnt/skills/public/xlsx/scripts/recalc.py <arquivo.xlsx>
Sai com código 1 se houver divergência ou pendência.
"""
import argparse
import re
import sys
from pathlib import Path

import openpyxl
from docx import Document

PENDENCIA = [
    (re.compile(r"\[PREENCHER[^\]]*\]"), "campo [PREENCHER]"),
    (re.compile(r"<[^<>\n]{1,80}>"), "campo <...> do template"),
    (re.compile(r"\bEXEMPLO\b"), "linha de EXEMPLO"),
]
# documento -> o que se espera encontrar nele
ESPERA = {
    "ETP": {"total": True, "quantidade": True, "codigo": False},
    "TR": {"total": True, "quantidade": True, "codigo": True},
    "Edital": {"total": True, "quantidade": True, "codigo": True},
}


def brl(v):
    """1234567.8 -> '1.234.567,80'"""
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def inteiro(v):
    v = float(v)
    return f"{int(v):,}".replace(",", ".") if v.is_integer() else brl(v)


def contem(valor, txt):
    """valor aparece como número inteiro, sem ser pedaço de outro número (150 não casa com 1500)."""
    return re.search(r"(?<![\d.,])" + re.escape(valor) + r"(?![\d]|,\d)", txt) is not None


def texto_docx(caminho):
    d = Document(caminho)
    partes = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            partes.extend(c.text for c in row.cells)
    return re.sub(r"[  ]", " ", "\n".join(partes))


def tipo(nome):
    n = nome.lower()
    for chave, rotulo in [("dfd", "DFD"), ("etp", "ETP"), ("-tr-", "TR"), ("edital", "Edital"),
                          ("contrato", "Minuta de Contrato"), ("mgr", "MGR"), ("fiscaliza", "Relatório de Fiscalização")]:
        if chave in n:
            return rotulo
    return nome


def ler_mapa(xlsx):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    itens = {}
    for row in wb["Itens"].iter_rows(min_row=2, values_only=True):
        if row[0] in (None, "") or (isinstance(row[1], str) and "EXEMPLO" in row[1]):
            continue
        itens[row[0]] = {"descricao": row[1], "codigo": str(row[2] or "").strip(), "quantidade": row[4]}
    total, sem_valor = 0.0, []
    for row in wb["Mapa"].iter_rows(min_row=2, values_only=True):
        if row[0] in itens:
            itens[row[0]]["unitario"], itens[row[0]]["total"] = row[13], row[15]
            if isinstance(row[15], (int, float)):
                total += row[15]
            else:
                sem_valor.append(row[0])
    return itens, round(total, 2), sem_valor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("projeto")
    ap.add_argument("--sigiloso", action="store_true", help="orçamento sigiloso: não exige o valor no Edital")
    ap.add_argument("--saida")
    a = ap.parse_args()
    pasta = Path(a.projeto) / "artefatos_ia"
    linhas, problemas = [f"# Verificação de coerência — {Path(a.projeto).name}", ""], 0

    xlsx = pasta / "06-Mapa-de-Precos.xlsx"
    if not xlsx.exists():
        sys.exit(f"Não achei {xlsx}")
    itens, total, sem_valor = ler_mapa(xlsx)
    if sem_valor:
        sys.exit(f"Mapa de Preços sem valores calculados nos itens {sem_valor}: recalcule a planilha antes.")
    linhas += [f"Referência: Mapa de Preços, {len(itens)} item(ns), valor total estimado R$ {brl(total)}.", ""]

    docs = sorted(pasta.glob("*.docx"))
    if not docs:
        sys.exit(f"Nenhum .docx em {pasta}")
    for doc in docs:
        rot = tipo(doc.name)
        txt = texto_docx(doc)
        achados = []
        for rx, desc in PENDENCIA:
            ocorr = sorted(set(rx.findall(txt)))
            if ocorr:
                achados.append(f"{desc}: {len(ocorr)} ({'; '.join(ocorr[:5])}{' ...' if len(ocorr) > 5 else ''})")
        esp = ESPERA.get(rot)
        if esp:
            if esp["total"] and not (rot == "Edital" and a.sigiloso) and not contem(brl(total), txt):
                achados.append(f"valor total do Mapa (R$ {brl(total)}) não aparece")
            for n, it in itens.items():
                if esp["quantidade"] and it["quantidade"] is not None and not contem(inteiro(it["quantidade"]), txt):
                    achados.append(f"item {n}: quantidade {inteiro(it['quantidade'])} não aparece")
                if esp["codigo"] and it["codigo"] and not contem(it["codigo"], txt):
                    achados.append(f"item {n}: código CATMAT/CATSER {it['codigo']} não aparece")
        linhas.append(f"## {doc.name} ({rot})")
        linhas += [f"- {x}" for x in achados] or ["- sem divergências"]
        linhas.append("")
        problemas += len(achados)

    linhas.append(f"**Total de apontamentos: {problemas}.** A ausência de um valor pode ser formato diferente no texto "
                  "(ex.: valor por extenso ou arredondado); confira o trecho antes de corrigir.")
    rel = "\n".join(linhas)
    if a.saida:
        Path(a.saida).write_text(rel, encoding="utf-8")
    print(rel)
    sys.exit(1 if problemas else 0)


if __name__ == "__main__":
    main()
