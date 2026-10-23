# Regras de download (para os subagentes)
- Shell (curl/wget) NÃO alcança gov.br/planalto/in.gov.br. Use SOMENTE a ferramenta mcp__Firecrawl__firecrawl_scrape (carregue com ToolSearch "select:mcp__Firecrawl__firecrawl_scrape").
- Para páginas HTML: formats ["markdown","links"], onlyMainContent true.
- Para PDF: formats ["markdown"], parsers ["pdf"]. Para DOCX/XLSX/ODT: tente formats ["markdown"]; se falhar, registre como falha.
- Quando a resposta for grande, ela é salva num arquivo JSON em /root/.claude/projects/.../tool-results/. Extraia com:
  python3 -I -c "import json,sys;d=json.load(open(sys.argv[1]));open(sys.argv[2],'w').write(d['markdown'])" ARQ_JSON DESTINO.md
  (depois acrescente o cabeçalho). Para respostas pequenas (inline), grave com Write.
- Cada arquivo .md salvo começa com cabeçalho YAML:
  ---
  titulo: "<nome oficial completo>"
  tipo: lei|decreto|instrucao-normativa|portaria|modelo|orientacao|anexo
  url_origem: <url>
  baixado_em: 2026-10-23
  situacao: vigente|revogada|alterada por ...   (conforme a página índice indicar)
  ---
  seguido do texto integral em markdown, SEM resumir, SEM editar o conteúdo.
- Nome de arquivo: slug curto em minúsculas, ex.: in-sgd-me-94-2022.md, lei-14133-2021.md, decreto-11246-2022.md, portaria-sgd-mgi-750-2023.md.
- Se a página for um "hub" com links para anexos (PDF/DOCX/modelos de artefato), baixe também cada anexo para a mesma pasta, com prefixo do documento pai.
- Ignore links de rodapé, cookies, redes sociais e menus do portal.
- Confira que o arquivo final tem conteúdo real (não só menu/rodapé). Se o texto vier truncado ou vazio, tente maxAge 0 ou proxy "auto" uma vez; persistindo, registre como falha.
- No fim, devolva: lista de arquivos salvos (caminho + nº de caracteres) e lista de falhas (url + motivo).
