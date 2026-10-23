---
name: base-legal-tic
description: Como consultar a base local de legislação de contratações de TIC (Lei 14.133/2021, IN SGD/ME 94/2022, decretos, INs SEGES, portarias e modelos da SGD) em base-legal/. Use sempre que um agente precisar citar ou conferir um dispositivo legal, achar a norma aplicável a um tema ou verificar se uma norma está vigente.
---

# Base legal de contratações de TIC

Todos os textos estão em `base-legal/`, em markdown, com cabeçalho YAML:

```
titulo, tipo, url_origem, baixado_em, situacao
```

`base-legal/INDICE.md` lista tudo (gerado por `scripts/gerar_indice.py`). Leia o índice antes de procurar.

## Como achar e citar

1. **Ache a norma** pelo índice ou por tema:
   `grep -ril "pesquisa de preços" base-legal/ --include=*.md`
2. **Leia o dispositivo** com o script (normaliza as quebras de linha dos textos do Planalto, onde `Art. 18` às vezes aparece partido):
   `python3 .claude/skills/base-legal-tic/scripts/buscar_artigo.py base-legal/normas/leis/lei-14133-2021.md 18`
   `python3 .claude/skills/base-legal-tic/scripts/buscar_artigo.py base-legal/normas/instrucoes-normativas/in-sgd-me-94-2022.md 10 --ate 12`
   Para anexos (ex.: Anexo I da IN 94), use `grep -n "ANEXO" <arquivo>` e `Read` com offset.
3. **Confira a situação** no cabeçalho. `revogada` só vale como histórico. Textos do Planalto mostram dispositivos revogados entre `~~ ~~`: não cite esses trechos como vigentes.
4. **Cite assim**: `Lei 14.133/2021, art. 18, § 1º, IV (base-legal/normas/leis/lei-14133-2021.md)`.
5. **Se não achar**, diga que a norma não está na base e peça o link ao usuário (a skill `incluir-norma` baixa). Não cite de memória.

## Mapa rápido por assunto

| Assunto | Onde olhar primeiro |
|---|---|
| Fases, equipe de planejamento, DFD, ETP, TR, riscos (TIC) | IN SGD/ME 94/2022, arts. 8º a 24 e 38; Anexos I e II |
| Planejamento e conteúdo do ETP (regra geral) | Lei 14.133, art. 18; IN SEGES/ME 58/2022 (aplicação subsidiária, IN 94 art. 42) |
| Conteúdo do TR (regra geral) | Lei 14.133, art. 6º, XXIII; IN SEGES/ME 81/2022 |
| Pesquisa de preços | Lei 14.133, art. 23; IN SEGES/ME 65/2021; orientações de análise crítica da SGD |
| Plano de Contratações Anual e DFD | Decreto 10.947/2022 |
| Contratação direta | Lei 14.133, arts. 72 a 75; IN SEGES/ME 67/2021 (dispensa eletrônica) |
| Registro de preços | Lei 14.133, arts. 82 a 86; Decreto 11.462/2023 |
| Agente de contratação, fiscais | Decreto 11.246/2022 |
| Aprovação prévia da SGD por valor (alçadas) | IN SGD/MGI 6/2023 (com IN 86/2025) |
| Preferência a bens e serviços de informática | Decreto 7.174/2010 |
| Sustentabilidade | IN SLTI 1/2010; Lei 14.133, art. 18, § 1º, XII |
| Modelos por tipo de objeto (nuvem, estações, software, impressão, infraestrutura, comunicação de dados, UST, métricas) | `base-legal/modelos-orientacoes/<card>/` |
| Templates oficiais de artefatos | `base-legal/modelos-orientacoes/templates-artefatos-sgd/extraido/` (originais em `modelos-oficiais/`) |

Quando IN 94 e uma IN SEGES tratarem do mesmo ponto, a IN 94 prevalece para TIC; a norma do SISG se aplica de forma subsidiária e só onde não houver tratamento específico do Órgão Central do SISP (IN 94, art. 42 e parágrafo único).
