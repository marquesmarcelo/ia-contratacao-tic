#!/usr/bin/env python3
"""Imprime o texto de um artigo de uma norma da base-legal.

Uso:
  python3 buscar_artigo.py <arquivo.md> <numero_artigo> [--ate <numero_final>]
  python3 buscar_artigo.py base-legal/normas/leis/lei-14133-2021.md 18
  python3 buscar_artigo.py base-legal/normas/instrucoes-normativas/in-sgd-me-94-2022.md 10 --ate 12

Os textos do Planalto quebram linhas e misturam marcação no meio de "Art. 18";
o script normaliza espaços e marcação antes de procurar. Devolve do "Art. N"
até o início do artigo seguinte (ou de --ate + 1).
"""
import re
import sys


def normalizar(texto: str) -> str:
    texto = re.sub(r"[\*\\_]+", "", texto)
    texto = re.sub(r"[ \t]*\n[ \t]*", "\n", texto)
    # junta linhas quebradas no meio de frase (sem linha em branco entre elas)
    texto = re.sub(r"(?<!\n)\n(?!\n)", " ", texto)
    return re.sub(r"[ \t]+", " ", texto)


def inicio_artigo(texto: str, n: int):
    padrao = re.compile(rf"(?:^|\n|\s)Art\.? ?{n} ?(?:º|°|o\b|\.|-)", re.MULTILINE)
    m = padrao.search(texto)
    return m.start() if m else None


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    caminho, n = sys.argv[1], int(sys.argv[2])
    ate = int(sys.argv[sys.argv.index("--ate") + 1]) if "--ate" in sys.argv else n
    texto = normalizar(open(caminho, encoding="utf-8").read())
    ini = inicio_artigo(texto, n)
    if ini is None:
        print(f"Art. {n} não encontrado em {caminho}", file=sys.stderr)
        return 1
    fim = inicio_artigo(texto[ini + 5 :], ate + 1)
    trecho = texto[ini:] if fim is None else texto[ini : ini + 5 + fim]
    if fim is None:
        trecho = trecho[:20000]
    print(trecho.strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
