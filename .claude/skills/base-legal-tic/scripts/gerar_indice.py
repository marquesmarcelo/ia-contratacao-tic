#!/usr/bin/env python3
"""Gera base-legal/INDICE.md a partir dos cabeçalhos YAML dos arquivos .md.

Uso (na raiz do projeto): python3 .claude/skills/base-legal-tic/scripts/gerar_indice.py
"""
import os
import re
import sys

RAIZ = sys.argv[1] if len(sys.argv) > 1 else "base-legal"
IGNORAR = {"INDICE.md", "INSTRUCOES-DOWNLOAD.md"}


def cabecalho(caminho):
    with open(caminho, encoding="utf-8") as f:
        texto = f.read(4000)
    m = re.match(r"---\n(.*?)\n---", texto, re.S)
    campos = {}
    if m:
        for linha in m.group(1).splitlines():
            if ":" in linha:
                k, v = linha.split(":", 1)
                campos[k.strip()] = v.strip().strip('"')
    return campos


def main():
    linhas = ["# Índice da base legal", "",
              "Gerado por `.claude/skills/base-legal-tic/scripts/gerar_indice.py`. Não edite à mão.", ""]
    for pasta, _, arquivos in sorted(os.walk(RAIZ)):
        mds = sorted(a for a in arquivos if a.endswith(".md") and a not in IGNORAR)
        if not mds or "fontes-brutas" in pasta:
            continue
        linhas += [f"## {os.path.relpath(pasta, RAIZ)}", "",
                   "| Arquivo | Título | Situação | KB |", "|---|---|---|---|"]
        for a in mds:
            c = os.path.join(pasta, a)
            h = cabecalho(c)
            titulo = h.get("titulo", "(sem cabeçalho)").replace("|", "/")[:160]
            situacao = h.get("situacao", "?").replace("|", "/")[:80]
            linhas.append(f"| `{os.path.relpath(c)}` | {titulo} | {situacao} | {os.path.getsize(c)//1024} |")
        linhas.append("")
    with open(os.path.join(RAIZ, "INDICE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))
    print(f"{RAIZ}/INDICE.md atualizado")


if __name__ == "__main__":
    main()
