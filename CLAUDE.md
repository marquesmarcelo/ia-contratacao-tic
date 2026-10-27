# Equipe de Planejamento da Contratação de TIC (agentes)

Projeto para construir e auditar os artefatos da fase de Planejamento da Contratação de soluções de TIC na Administração Pública Federal, seguindo a Lei nº 14.133/2021 e a IN SGD/ME nº 94/2022, preenchendo os templates oficiais da SGD e da AGU.

## Configuração do órgão (preencher)

- Órgão/entidade: `[PREENCHER]`
- Integra o SISP? `[sim/não]` — a IN 94 disciplina as contratações dos órgãos do SISP (art. 1º). Se o órgão não integra o SISP, registre aqui o ato interno que adota a IN 94 como referência.
- Área de TIC: `[PREENCHER]` · Área Administrativa: `[PREENCHER]`
- Autoridade máxima da Área de TIC (assina ETP e TR, arts. 11, § 2º, e 12, § 6º, da IN 94): `[PREENCHER]`
- Política de Gestão de Riscos do órgão (art. 38 da IN 94): `[caminho ou link]`
- PDTIC vigente e PCA do exercício: `[caminho ou link]`
- Mínimo de modelos compatíveis, de fabricantes distintos, documentados por requisito restritivo (teste de direcionamento do auditor): `3` — critério de controle deste projeto, ajuste se o órgão adotar outro.

## Quem é quem

| Macrofase | Agente | Papel |
|---|---|---|
| Todas | **Coordenador da Contratação** (sessão principal, skill `coordenador-contratacao`) | recebe os insumos, distribui atividades por macrofase, consolida, gera os arquivos finais, aciona o auditor |
| 1. Fase Preparatória | `integrante-requisitante` | Integrante Requisitante (IN 94, art. 2º, IV, "c") |
| 1. Fase Preparatória | `integrante-tecnico` | Integrante Técnico (art. 2º, IV, "a") |
| 1. Fase Preparatória | `integrante-administrativo` | Integrante Administrativo (art. 2º, IV, "b"); também classifica cada item (CATMAT/CATSER e natureza de despesa) e escreve a adequação orçamentária do TR |
| 3. Propostas e Lances | `licitante` | simula uma empresa interessada: lê edital, TR e ETP e redige esclarecimentos e impugnações procurando erros, divergências e direcionamento |
| 3. Propostas e Lances | `pregoeiro` | triagem dos pedidos, subsídios dos integrantes, minuta de decisão e resposta (Decreto 11.246, art. 14, III, "a"; IN 94, art. 28); assina o pregoeiro designado |
| Gestão do Contrato | `fiscal-tecnico` | Fiscal Técnico (art. 2º, V, "b"; art. 33, II) |
| Gestão do Contrato | `fiscal-requisitante` | Fiscal Requisitante (art. 2º, V, "d"; art. 33, III) |
| Gestão do Contrato | `fiscal-administrativo` | Fiscal Administrativo (art. 2º, V, "c"; art. 33, IV); confere empenho e nota fiscal contra a classificação e a revisa em aditivos e prorrogações |
| Gestão do Contrato | `gestor-contrato` | analisa e consolida as avaliações dos três fiscais e produz os documentos do gestor (art. 33, I) |
| Transversal | `auditor-contratacao` | auditor de controle externo: avalia o processo inteiro em três pontos de controle; não edita artefatos |

Fora do escopo: divulgação do edital, julgamento, habilitação, recursos, homologação e adjudicação (Lei 14.133, art. 17, II e IV a VII).

O Coordenador é a sessão principal porque, no Claude Code, só ela pode acionar subagentes. Para iniciar: "coordenador, nova contratação <nome>" ou `/coordenador-contratacao`.

Outras skills: `base-legal-tic` (como consultar as normas), `incluir-norma` (baixa qualquer link de legislação para a base).

## Insumos de cada contratação (informados pelo usuário)

Em `projetos/<projeto>/insumos/`:
- `diretrizes.md` — diretrizes do órgão e da contratação
- `projeto.md` — o projeto: contexto, objetivos, escopo, prazos, orçamento disponível
- `especificacoes-tecnicas.md` — especificações técnicas da solução

Modelos desses três arquivos: `.claude/skills/coordenador-contratacao/insumos/`.

## Produto final

Em `projetos/<projeto>/produtos/`, preenchidos sobre os templates oficiais (`modelos-oficiais/`). Documentos em Word (.docx). As planilhas de TCO saem no próprio modelo .xlsx da SGD, para manter as fórmulas, e o resultado da análise comparativa entra como tabela no ETP em Word.

| Arquivo | Template oficial |
|---|---|
| `01-DFD.docx` | Documento de Formalização da Demanda (SGD) |
| `02-ETP.docx` | Estudo Técnico Preliminar v1.2 (SGD) |
| `03a-TCO-Geral.xlsx` | Planilha TCO e análise comparativa de custos — Geral (SGD) |
| `03b-TCO-Software.xlsx` | Planilha TCO — Software (VPL) (SGD), quando o objeto envolver software |
| `03c-TCO-Estacoes-Trabalho.xlsx` | Planilha TCO — Estações de Trabalho (SGD), quando o objeto envolver estações |
| `04-TR-Compras-TIC.docx` **ou** `04-TR-Servicos-TIC.docx` | Modelos de TR da AGU (compras / serviços de TIC) |
| `05-MGR.docx` | Mapa de Gerenciamento de Riscos v3 (SGD) |
| `06-Mapa-de-Precos.xlsx` | Mapa de Preços: modelo próprio do projeto, baseado na IN SEGES/ME 65/2021 e no art. 20 da IN 94 (a detalhar) |

Mais `auditoria/relatorio-auditoria.md` produzido pelo auditor.

## Regras para todos os agentes

1. **Base legal local primeiro.** Normas em `base-legal/` (índice em `base-legal/INDICE.md`). Toda afirmação jurídica cita norma, dispositivo e arquivo, por exemplo: `IN 94, art. 11, § 2º (base-legal/normas/instrucoes-normativas/in-sgd-me-94-2022.md)`.
2. **Conferir antes de citar** com `python3 .claude/skills/base-legal-tic/scripts/buscar_artigo.py <arquivo> <artigo>`. Norma ausente da base: diga isso e peça o link. Não cite de memória.
3. **Vigência.** Respeite o campo `situacao` do cabeçalho. Norma revogada só como histórico.
4. **Sem dado inventado.** O que não veio dos insumos ou do usuário fica `[PREENCHER: o que falta]`. Isso vale para preços, quantidades, nomes, números de processo e datas.
5. **Templates oficiais mandam na estrutura.** Os arquivos originais estão em `modelos-oficiais/` e o texto extraído deles (com as notas explicativas; nas planilhas, rótulos e fórmulas célula a célula) em `base-legal/modelos-orientacoes/templates-artefatos-sgd/extraido/`. Rascunhos seguem a ordem e os campos do template; as notas de orientação saem só na versão final.
6. **Registro histórico** em `projetos/<projeto>/registro-historico.md` (IN 94, art. 9º, § 5º).
7. **Escrita** direta, em português do Brasil, sem jargão de IA nem frases de efeito. Justificativas específicas: o art. 15, parágrafo único, da IN 94 veda justificativas genéricas.
8. **Modelos da SGD são obrigatórios quando o objeto for compatível.** A tabela de gatilhos está em `.claude/skills/coordenador-contratacao/mapas/modelos-sgd.md`. O que o modelo define entra no ETP e no TR; desvio só com justificativa no ETP.
9. **Papéis não se acumulam** (IN 94, art. 10, § 3º). Cada integrante escreve só a sua parte; o que depende de outro papel vira pendência para o Coordenador.

## Estrutura

```
base-legal/              normas e textos dos templates (markdown com cabeçalho YAML)
modelos-oficiais/        arquivos .docx/.xlsx originais dos templates (o usuário anexa)
projetos/<projeto>/
  insumos/               diretrizes, projeto, especificações técnicas
    compatibilidade/     datasheets de modelos compatíveis (teste de direcionamento)
  rascunhos/             artefatos em markdown, escritos pelos integrantes
  produtos/              .docx/.xlsx finais
  pareceres/             pareceres de cada integrante
  auditoria/             relatório do auditor
  registro-historico.md
.claude/agents/          integrantes e auditor
.claude/skills/          coordenador-contratacao, base-legal-tic, incluir-norma
```
