---
name: incluir-norma
description: Baixa uma norma, modelo ou orientação a partir de um link (gov.br, planalto.gov.br, in.gov.br, PDF) e salva em base-legal/ com cabeçalho YAML para uso pelos agentes de contratação de TIC. Use sempre que o usuário colar um link de legislação, modelo ou orientação, mesmo sem pedir explicitamente para baixar.
---

# Incluir norma na base legal

Todo link de legislação, modelo ou orientação que o usuário passar entra na base. Siga `base-legal/INSTRUCOES-DOWNLOAD.md`. Resumo:

1. **Ferramenta**: `mcp__Firecrawl__firecrawl_scrape` (o shell não alcança gov.br). HTML: `formats ["markdown","links"]`, `onlyMainContent: true`. PDF: `parsers ["pdf"]`.
2. **Destino** conforme o tipo:
   - lei → `base-legal/normas/leis/`
   - decreto → `base-legal/normas/decretos/`
   - instrução normativa → `base-legal/normas/instrucoes-normativas/`
   - portaria → `base-legal/normas/portarias/`
   - modelo, guia, orientação, card da SGD → `base-legal/modelos-orientacoes/<slug>/`
3. **Cabeçalho** obrigatório: `titulo`, `tipo`, `url_origem`, `baixado_em` (data de hoje), `situacao` (como a fonte indica). Depois, o texto integral, sem resumir.
4. **Página hub** (lista de anexos/modelos): salve como `00-pagina-card.md` e baixe cada documento vigente listado.
5. **Já existe?** Se o arquivo já estiver na base, compare datas e substitua só se a fonte trouxer versão mais nova; registre a troca no corpo da resposta.
6. **Confira** que o arquivo tem o texto real (não só menu) e, em lei/IN, que o último artigo está presente (`buscar_artigo.py`).
7. **Atualize o índice**: `python3 .claude/skills/base-legal-tic/scripts/gerar_indice.py`.
8. Responda com a lista de arquivos salvos e o que falhou (ex.: `.xlsx` que não converteu, com a URL para o usuário baixar manualmente).
