# Equipe de Planejamento da Contratação de TIC (agentes)

Projeto para construir e auditar os artefatos da fase de Planejamento da Contratação de soluções de TIC na Administração Pública Federal, seguindo a Lei nº 14.133/2021 e a IN SGD/ME nº 94/2022, preenchendo os templates oficiais da SGD e da AGU.

## Configuração do órgão (preencher)

- Órgão/entidade: `[PREENCHER]`
- Integra o SISP? `[sim/não]` — a IN 94 disciplina as contratações dos órgãos do SISP (art. 1º). Se o órgão não integra o SISP, registre aqui o ato interno que adota a IN 94 como referência.
- Área de TIC: `[PREENCHER]` · Área Administrativa: `[PREENCHER]`
- Autoridade máxima da Área de TIC (assina ETP e TR, arts. 11, § 2º, e 12, § 6º, da IN 94): `[PREENCHER]`
- Política de Gestão de Riscos do órgão (art. 38 da IN 94): `[caminho ou link]`
- PDTIC vigente e PCA do exercício: `[caminho ou link]`
- Habilitação técnica: sempre exigida; quantidade mínima nos atestados `50%` da parcela de maior relevância (máximo da Lei 14.133, art. 67, § 2º); atestados emitidos pela licitante ou por empresa do mesmo grupo econômico `não aceitos` — critérios do projeto, ajuste se o órgão adotar outros.
- Mínimo de modelos compatíveis, de fabricantes distintos, documentados por requisito restritivo (teste de direcionamento do Consultor Jurídico): `3` — critério de controle deste projeto, ajuste se o órgão adotar outro.

## Quem é quem

| Macrofase | Agente | Papel |
|---|---|---|
| Fase Preparatória e Propostas e Lances | **Chefe da Equipe da Contratação** (sessão principal, skill `chefe-equipe-contratacao`) | aplica o questionário de abertura (inclusive a pergunta sobre documentos já feitos em `artefatos_atual/`), decide o caminho (compra ou serviço, registro de preços, contínuo, competição, testes, amostragem, posto de trabalho), escreve o plano de trabalho, aciona os integrantes, revisa, gera os .docx, aciona o Consultor Jurídico (PC1, PC2), aprova, roda Licitante e Pregoeiro e passa a condução ao Gestor do Contrato |
| 1. Fase Preparatória | `integrante-requisitante` | Integrante Requisitante (IN 94, art. 2º, IV, "c") |
| 1. Fase Preparatória | `integrante-tecnico` | Integrante Técnico (art. 2º, IV, "a") |
| 1. Fase Preparatória | `integrante-administrativo` | Integrante Administrativo (art. 2º, IV, "b"); também classifica cada item (CATMAT/CATSER e natureza de despesa)  que os Integrantes Requisitante e Técnico usam na adequação orçamentária (IN 94, art. 21) |
| 3. Propostas e Lances | `licitante` (modelo Fable) | simula uma empresa interessada: lê edital, TR e ETP e só questiona o que não está claro ou está errado no TR, depois de conferir que o texto não resolve; o Chefe avalia as perguntas e decide as alterações |
| 3. Propostas e Lances | `pregoeiro` | triagem dos pedidos, aciona os integrantes para subsídio, decide, responde e consolida o Relatório de Licitação (Decreto 11.246, art. 14, III, "a"; IN 94, art. 28); assina o pregoeiro designado |
| Gestão do Contrato | `fiscal-tecnico` | Fiscal Técnico (art. 2º, V, "b"; art. 33, II) |
| Gestão do Contrato | `fiscal-requisitante` | Fiscal Requisitante (art. 2º, V, "d"; art. 33, III) |
| Gestão do Contrato | `fiscal-administrativo` | Fiscal Administrativo (art. 2º, V, "c"; art. 33, IV); confere empenho e nota fiscal contra a classificação e a revisa em aditivos e prorrogações |
| Gestão do Contrato | **Gestor do Contrato** (sessão principal, skill `gestor-contrato`) | começa com a proposta do contratado, as respostas aos questionamentos e o empenho; gera o Relatório de Fiscalização por mês de referência ou por entrega; abate cada pagamento do empenho e alerta sobre saldo, valor anual e quantidade acima do contratado; conversa com o usuário, aciona os três fiscais, consolida o Relatório de Fiscalização, produz os documentos do gestor (art. 33, I) e aciona o Consultor Jurídico no PC3 |
| Transversal | `consultor-juridico` (modelo Fable) | Consultor Jurídico: controle prévio de legalidade (Lei 14.133, art. 53) e minuta de parecer jurídico no modelo da AGU, com teste de direcionamento e de sobrepreço, em três pontos de controle; não edita artefatos |

Fora do escopo: adesão a ata de registro de preços de outro órgão (os agentes são para nova licitação), divulgação do edital, julgamento, habilitação, recursos, homologação e adjudicação (Lei 14.133, art. 17, II e IV a VII).

Chefe e Gestor são skills, não subagentes, porque no Claude Code só a sessão principal aciona subagentes. Para iniciar: "chefe, nova contratação <nome>" ou `/chefe-equipe-contratacao`. Na gestão: `/gestor-contrato`.

Outras skills: `base-legal-tic` (como consultar as normas), `incluir-norma` (baixa qualquer link de legislação para a base).

## Insumos de cada contratação (informados pelo usuário)

Em `projetos/<projeto>/insumos/`:
- `diretrizes.md` — diretrizes do órgão e da contratação
- `projeto.md` — o projeto: contexto, objetivos, escopo, prazos, orçamento disponível
- `especificacoes-tecnicas.md` — especificações técnicas da solução

Modelos desses três arquivos: `.claude/skills/chefe-equipe-contratacao/insumos/`.

Artefatos já feitos por servidores (DFD, ETP, TR, anexos, Mapa de Preços, Mapa de Riscos) vão em `projetos/<projeto>/artefatos_atual/` e nunca são sobrescritos. Com arquivos lá, o Chefe pergunta: elaborar novos artefatos (os atuais são avaliados e viram base; o resultado vai para `artefatos_ia/`) ou seguir para a fase 2, Gestão do Contrato, com os atuais.

## Produto final

O objetivo da fase 1 é sempre este: produzir DFD, ETP (com TCO), TR com os anexos, Edital com a minuta de contrato, Mapa de Preços e Mapa de Gerenciamento de Riscos. Eles são feitos nessa ordem, um por etapa: perguntas da etapa, geração do artefato, validação do usuário. O Mapa de Preços atualiza o valor do ETP, do TR e do Edital; o MGR fecha com os riscos do planejamento, da seleção e da futura gestão.

Em `projetos/<projeto>/artefatos_ia/`, preenchidos sobre os templates oficiais (`modelos-oficiais/`). Os documentos finais vão anexados ao processo, então saem em Word (.docx; .doc por conversão se o órgão pedir). O Mapa de Preços e as planilhas de TCO saem em .xlsx, porque a planilha mostra a memória de cálculo; o resultado do TCO entra também em tabela no ETP.

| Arquivo | Template oficial |
|---|---|
| `01-DFD.docx` | Documento de Formalização da Demanda (SGD) |
| `02-ETP.docx` | Estudo Técnico Preliminar v1.2 (SGD) |
| `03a-TCO-Geral.xlsx` | Planilha TCO e análise comparativa de custos — Geral (SGD) |
| `03b-TCO-Software.xlsx` | Planilha TCO — Software (VPL) (SGD), quando o objeto envolver software |
| `03c-TCO-Estacoes-Trabalho.xlsx` | Planilha TCO — Estações de Trabalho (SGD), quando o objeto envolver estações |
| `04-TR-Compras-TIC.docx` **ou** `04-TR-Servicos-TIC.docx` | Modelos de TR da AGU (compras / serviços de TIC) |
| `05-MGR.docx` | Mapa de Gerenciamento de Riscos v3 (SGD) |
| `08-Edital.docx` e `09-Minuta-Contrato.docx` | Modelos AGU de edital (pregão e concorrência, TIC) e de termo de contrato (compras ou serviços de TIC) |
| `Anexo-D-Relatorio-Fiscalizacao.docx` | Modelo do projeto `07-Relatorio-Fiscalizacao-template.docx`, na estrutura do modelo da SGD (Portaria 750/2023, Anexo VIII), ajustado ao TR |
| `06-Mapa-de-Precos.xlsx` | Mapa de Preços: modelo próprio do projeto, baseado na IN SEGES/ME 65/2021 e no art. 20 da IN 94 |

Mais `juridico/parecer-juridico-PC<n>.docx` e a lista de verificação da AGU preenchida, produzidos pelo Consultor Jurídico.

## Regras para todos os agentes

1. **Base legal local primeiro.** Normas em `base-legal/` (índice em `base-legal/INDICE.md`). Toda afirmação jurídica cita norma, dispositivo e arquivo, por exemplo: `IN 94, art. 11, § 2º (base-legal/normas/instrucoes-normativas/in-sgd-me-94-2022.md)`.
2. **Conferir antes de citar** com `python3 .claude/skills/base-legal-tic/scripts/buscar_artigo.py <arquivo> <artigo>`. Norma ausente da base: diga isso e peça o link. Não cite de memória.
3. **Vigência.** Respeite o campo `situacao` do cabeçalho. Norma revogada só como histórico.
4. **Sem dado inventado.** O que não veio dos insumos ou do usuário fica `[PREENCHER: o que falta]`. Isso vale para preços, quantidades, nomes, números de processo e datas.
5. **Templates oficiais mandam na estrutura.** Os arquivos originais estão em `modelos-oficiais/` e o texto extraído deles (com as notas explicativas; nas planilhas, rótulos e fórmulas célula a célula) em `base-legal/modelos-orientacoes/templates-artefatos-sgd/extraido/`. Rascunhos seguem a ordem e os campos do template; as notas de orientação saem só na versão final.
6. **Registro histórico** em `projetos/<projeto>/registro-historico.md` (IN 94, art. 9º, § 5º).
7. **Escrita** direta, em português do Brasil, sem jargão de IA nem frases de efeito. Justificativas específicas: o art. 15, parágrafo único, da IN 94 veda justificativas genéricas.
8. **Modelos da SGD são obrigatórios quando o objeto for compatível.** A tabela de gatilhos está em `.claude/skills/chefe-equipe-contratacao/mapas/modelos-sgd.md`. O que o modelo define entra no ETP e no TR; desvio só com justificativa no ETP.
9. **Regras do projeto para o TR** (detalhes em `.claude/skills/chefe-equipe-contratacao/mapas/anexos-tr.md`): aceita-se o igual ou superior, nunca o inferior, sem compensação entre requisitos; o TR traz modelo de proposta e matriz de comprovação com arquivo e página; roteiro de testes objetivo quando houver amostra ou prova de conceito; Relatório de Fiscalização mensal ou por entrega; amostragem (ABNT NBR 5426) em grande quantidade de bens; comprovação trabalhista mensal em posto de trabalho; reajuste pelo ICTI; habilitação técnica sempre exigida, com atestados de 50% das parcelas de maior relevância e emitente fora do grupo econômico da licitante; garantia do fabricante registrada em nome do órgão como condição do recebimento definitivo e do pagamento, e pagamento antecipado só nas hipóteses do art. 145 da Lei 14.133; níveis de serviço com indicador, fórmula, fonte, meta e faixas de glosa, e fórmula de pagamento com teto de glosa e exemplo numérico (Anexo G); o Relatório de Fiscalização (Anexo D) é o modelo que, na gestão, os agentes preenchem a cada mês ou entrega a partir do que o fornecedor entregou e dos dados de nível de serviço, concluindo se o pagamento pode ser feito.
10. **Papéis não se acumulam** (IN 94, art. 10, § 3º). Cada integrante escreve só a sua parte; o que depende de outro papel vira pendência para o Chefe da Equipe da Contratação (ou para o Gestor do Contrato, na gestão).
11. **Relatórios de analistas de mercado** (Quadrante Mágico do Gartner e similares) entram só no levantamento de mercado do ETP, com fonte e data; nunca como requisito, habilitação, pontuação ou critério de aceitação.

## Estrutura

```
base-legal/              normas e textos dos templates (markdown com cabeçalho YAML)
modelos-oficiais/        arquivos .docx/.xlsx originais dos templates (o usuário anexa)
projetos/<projeto>/
  artefatos_atual/       artefatos feitos por servidores (entrada; nunca sobrescrita)
  insumos/               diretrizes, projeto, especificações técnicas
    compatibilidade/     datasheets de modelos compatíveis (teste de direcionamento)
  rascunhos/             artefatos em markdown, escritos pelos integrantes
  artefatos_ia/              .docx finais (e .xlsx de memória de cálculo)
  pareceres/             pareceres de cada integrante
  juridico/              minutas de parecer jurídico e lista de verificação da AGU
  registro-historico.md
.claude/agents/          integrantes, licitante, pregoeiro, fiscais e consultor jurídico
.claude/skills/          chefe-equipe-contratacao, gestor-contrato, base-legal-tic, incluir-norma, classificacao-despesa
```
