# Projetos de contratação

Uma pasta por contratação, criada pelo Chefe da Equipe da Contratação: `projetos/<nome-curto>/`.

```
projetos/<nome-curto>/
  plano-trabalho.md             decisões da triagem e divisão de atividades (Chefe da Equipe da Contratação)
  artefatos_atual/                 documentos já feitos por servidores (entrada); inventario.md e versões .md
  insumos/
    questionario-abertura.md    respostas do questionário
    diretrizes.md
    projeto.md
    especificacoes-tecnicas.md
    compatibilidade/            datasheets de modelos compatíveis, um por modelo
    precos/                     propostas e preços já obtidos, com a fonte de cada um
  rascunhos/                    markdown escrito pelos integrantes, na estrutura do template oficial
    00-instituicao-equipe.md
    01-dfd.md
    02-etp.md
    03a-tco-geral.md  03b-tco-software.md  03c-tco-estacoes.md
    06-mapa-precos.md
    07-classificacao.md          CATMAT/CATSER e natureza de despesa (Integrante Administrativo)
    04-tr.md
    05-mgr.md
  artefatos_ia/                     arquivos finais
    01-DFD.docx
    02-ETP.docx
    03a-TCO-Geral.xlsx  03b-TCO-Software.xlsx  03c-TCO-Estacoes-Trabalho.xlsx
    04-TR-Compras-TIC.docx  ou  04-TR-Servicos-TIC.docx
    05-MGR.docx
    Anexos-TR-*.docx             anexos do TR (proposta, matriz, roteiro de testes etc.)
    06-Mapa-de-Precos.xlsx       (planilha, mostra a memória de cálculo)
  pareceres/                    revisão cruzada dos integrantes
  juridico/                     Consultor Jurídico
    parecer-juridico-PC1.md/.docx  PC2  PC3
    lista-verificacao-agu-PC1.md  PC2  PC3
    matriz-compatibilidade.md
  licitacao/                    fase de Seleção do Fornecedor
    edital/                     edital publicado e anexos
    pedidos/                    pedidos reais e simulados (SIM-NNN.md, agente Licitante)
    subsidios/                  perguntas do pregoeiro e respostas dos integrantes
    respostas/                  minutas de decisão e resposta do pregoeiro
    registro-pedidos.md
    relatorio-licitacao.md      consolidado do Pregoeiro
  contrato/                     fase de Gestão do Contrato
    proposta/                   proposta comercial do contratado (início da gestão)
    questionamentos/            respostas aos pedidos de esclarecimento e impugnações
    empenho/                    nota de empenho, reforços e anulações
    controle-financeiro.md      pagamentos abatidos do empenho; quantidades usadas x contratadas
    conferencia-proposta-*.md   proposta x TR, por fiscal
    base-gestao.md              itens, preços, saldo, SLAs, cronograma, periodicidade
    fiscalizacao/<aaaa-mm>/     entrada/ (o que o fornecedor entregou), fiscal-*.md, gestor-consolidacao.md,
                                Relatorio-Fiscalizacao-<aaaa-mm>.docx (por mês de referência ou por entrega)
    evidencias/                 relatórios da contratada, chamados, logs
    contrato.md  designacoes.md  historico-gestao.md
    ordens-servico/  recebimentos/  medicoes/  ocorrencias/  sancoes/  prorrogacao/  riscos/
  registro-historico.md         IN 94, art. 9º, § 5º
```

Para começar, no Claude Code: `/chefe-equipe-contratacao` ou "chefe, nova contratação de <objeto>". Na gestão: `/gestor-contrato`.
