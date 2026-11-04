# Questionário da contratação, por etapa

> Aplicado pelo Chefe da Equipe da Contratação etapa por etapa: faz as perguntas da etapa, gera o artefato, mostra ao usuário e só passa à próxima etapa depois da validação. O que faltar vira `[PREENCHER]`. As respostas vão para `projetos/<projeto>/insumos/questionario-abertura.md` e para o `registro-historico.md`. Riscos que aparecerem em qualquer etapa vão para `rascunhos/riscos-identificados.md` e entram no MGR na Etapa 6.

## Etapa 0 — Abertura (antes de tudo)

Define o caminho e o template.

0. **Esta contratação já tem algum artefato feito?** (DFD, ETP, TR e anexos, Mapa de Preços, Mapa de Riscos.) Se tiver, coloque os arquivos em `projetos/<projeto>/artefatos_atual/`. O Chefe pergunta então se é para elaborar novos artefatos, usando os atuais como base (o resultado vai para `artefatos_ia/`), ou para seguir direto para a fase 2, Gestão do Contrato, com os artefatos atuais.
1. **Compra, serviço ou os dois?** Define o TR de Compras ou de Serviços. Se misto, qual natureza predomina? (IN 94, art. 3º, I: uma solução por contrato)
2. **Licitação, contratação direta ou adesão a ata?** Licitação: fluxo normal. Contratação direta (fornecedor exclusivo, valor abaixo do limite de dispensa ou outra hipótese do art. 75): o Chefe segue `mapas/contratacao-direta.md`, e a Etapa 4 troca o Edital pela instrução da contratação direta. Adesão a ata de outro órgão fica fora do escopo: o Chefe avisa e para.

## Etapa 1 — DFD

Gera `01-DFD.docx` e o despacho de instituição da equipe.

3. Área requisitante e responsável.
4. Problema que a contratação resolve, quem é afetado, com números.
5. **O que acontece se a contratação não for feita?** (impacto no serviço, na segurança, nos usuários, prazos legais)
6. Quantidade e memória de cálculo, considerando o consumo anual.
7. Estimativa preliminar de valor e origem.
8. Data em que a contratação precisa estar concluída.
9. Prioridade: baixa, média ou alta.
10. Vinculação ou dependência com outra contratação.
11. Item do PCA e ação do PDTIC.
12. Integrantes Requisitante, Técnico e Administrativo indicados.
13. Algum acúmulo de papéis? (só Requisitante + Técnico, com justificativa e aprovação do Comitê de Governança Digital, IN 94, art. 10, § 3º)

## Etapa 2 — ETP e TCO

Gera `02-ETP.docx` e as planilhas de TCO. O custo do ETP é a estimativa preliminar; a Etapa 4 atualiza.

14. **Se for compra: será por Sistema de Registro de Preços?**
   - Sim: a ata vale 1 ano, prorrogável por igual período se comprovado o preço vantajoso (Lei 14.133, art. 84; Decreto 11.462/2023, art. 22). O edital precisa trazer índice de reajuste com data-base na data do orçamento (Lei 14.133, art. 25, § 7º); padrão do projeto: ICTI. Perguntar: órgãos participantes, admite adesão de não participantes (e por quê), quantidades mínima e máxima.
   - Não: aquisição direta com entrega definida.
15. **Se for serviço: contínuo ou por escopo?** Contínuo: até 5 anos (art. 106), prorrogável até 10 (art. 107), com justificativa da vantagem do contrato plurianual no ETP (art. 106, I). Por escopo: prazo para concluir a entrega (art. 6º, XVII).
16. **Se for serviço contínuo: há dedicação exclusiva de mão de obra ou medição por posto de trabalho?** Se sim, ativa o Anexo F do TR (comprovação trabalhista) e a justificativa do art. 5º, IX, da IN 94.
17. **Especificação técnica e 3 equipamentos ou soluções compatíveis**, de fabricantes distintos, com datasheet de cada um (vai para `insumos/compatibilidade/`).
18. **Se não houver 3 compatíveis, qual o caso?**
   - marca ou part number vendido por várias revendas: licitação, com justificativa técnica e econômica numa hipótese do art. 41, I, da Lei 14.133 e prova (processo de padronização do art. 43, inventário do ambiente etc.);
   - fornecedor exclusivo: inexigibilidade (art. 74, I), com documento idôneo de exclusividade; autodeclaração não vale (IN 94, art. 5º, XII).
19. Situação atual: contrato vigente, fornecedor, término, problemas.
20. Alternativas já consideradas (compra x serviço, nuvem, software livre, solução de outro órgão).
21. Requisitos de negócio, legais, de capacitação e de sustentabilidade.
22. Trata dados pessoais ou informação sigilosa? (requisitos de segurança e LGPD, IN 94, Anexo I, item 7)
23. Garantia técnica e suporte esperados (meses, on-site, prazo de solução).
24. Um lote ou itens separados? Por quê?
25. Resultados esperados, com indicador e meta.
26. Horizonte do TCO em anos e custos indiretos a considerar.
27. Providências antes de contratar (ambiente, capacitação dos fiscais).

## Etapa 3 — TR e anexos

Gera o TR de Compras ou de Serviços com os anexos A a G e a classificação CATMAT/CATSER e de despesa.

28. **Haverá teste para validar o equipamento** (amostra, prova de conceito, teste de aceitação)? Se sim, ativa o Anexo C (roteiro de testes).
29. **Haverá entrega de grande quantidade de bens?** Se sim, ativa o Anexo E (amostragem, ABNT NBR 5426).
30. **Níveis de serviço.** Que níveis de serviço a contratação precisa (disponibilidade, prazo de atendimento e de solução, prazo de entrega, qualidade da entrega)? Se você não souber, os integrantes propõem os SLAs: o Requisitante diz o que o negócio precisa, o Técnico define indicador, fórmula, fonte, meta e faixas de glosa, e o Administrativo define o cálculo do pagamento (Anexo G). Você valida a proposta.
31. Compra: locais e prazo de entrega, instalação, forma de recebimento.
32. Serviço: horário, local, métrica de medição, transição final (os níveis de serviço e o pagamento vêm da pergunta sobre níveis de serviço desta etapa).
33. Habilitação técnica (sempre exigida): quais são as parcelas de maior relevância (valor ≥ 4% do total)? Manter o padrão de 50% da quantidade de cada uma (em SRP, da quantidade registrada) ou usar percentual menor? Serviço contínuo: exigir prazo mínimo de execução (até 3 anos)? Atestados de empresa do mesmo grupo da licitante não são aceitos (regra do projeto).
34. Consórcio e subcontratação: aceita?
35. Garantia contratual: exigir? Percentual? (Lei 14.133, arts. 96 a 102)
    Há parcela paga de uma vez e usufruída por anos (garantia de 5 anos, licença ou suporte por assinatura)? A garantia é do fabricante ou de terceiro? Se for do fabricante, o pagamento fica condicionado à prova do registro da garantia em nome do órgão. Se for pagamento antecipado de serviço, é preciso justificar economia ou indispensabilidade (Lei 14.133, art. 145).
36. Sanções: o órgão tem tabela padrão?

## Etapa 4 — Edital e minuta de contrato (ou instrução da contratação direta)

Na contratação direta, as perguntas desta etapa são as de `mapas/contratacao-direta.md`: documento de exclusividade ou somatório do exercício, razão da escolha do contratado, justificativa de preço.

Gera `08-Edital.docx` e `09-Minuta-Contrato.docx` sobre os modelos da AGU (edital de pregão e concorrência de TIC; termo de contrato de compras ou de serviços de TIC), com o TR e seus anexos como anexo do edital.

37. Modalidade: pregão (bens e serviços comuns) ou concorrência? Critério de julgamento: menor preço por item, por grupo, maior desconto, técnica e preço?
38. Modo de disputa: aberto ou aberto e fechado?
39. Há itens exclusivos para microempresas e empresas de pequeno porte, ou cota reservada? (LC 123/2006, art. 48, citada no modelo da AGU; a LC não está na base)
40. Aplica-se a preferência a bens e serviços de informática (Decreto 7.174/2010) ou a restrição a Processo Produtivo Básico?
41. Orçamento sob sigilo até o fim da licitação?
42. Setor responsável pela licitação, pregoeiro ou agente de contratação designado e endereço para pedidos de esclarecimento.

## Etapa 5 — Mapa de Preços

Gera `06-Mapa-de-Precos.xlsx` e atualiza o valor no ETP (estimativa e TCO), no TR (estimativa e adequação orçamentária) e no Edital.

43. **Anexe os preços que você já tem** em `insumos/precos/` (propostas, prints do Painel de Preços, contratos ou atas de outros órgãos, notas fiscais) e diga, para cada arquivo, a fonte: pesquisa com fornecedor, Painel de Preços, contratação similar, mídia ou site especializado, nota fiscal eletrônica. Os Integrantes Técnico e Administrativo montam o Mapa de Preços a partir disso e apontam o que falta.
44. Item em catálogo da SGD com PMC-TIC?
45. Dotação, fonte, ação orçamentária, valor disponível no exercício; previsão plurianual.

> **Como fazer uma boa pesquisa de preços** (IN SEGES/ME 65/2021, art. 5º; IN 94, art. 20):
> - Comece pelo Painel de Preços e por contratações similares da Administração dos últimos 12 meses (art. 5º, I e II); são as fontes prioritárias, e não usá-las exige justificativa (§ 1º).
> - Proposta de fornecedor só complementa. Preço baseado só em propostas exige justificativa (IN 94, art. 20, § 1º) e, quando possível, valores do fabricante (§ 2º).
> - Peça cotação a pelo menos 3 fornecedores, por ofício ou e-mail, explicando por que escolheu esses fornecedores, com prazo de resposta compatível e as mesmas condições do objeto (quantidade, prazo, garantia, SLA). Registre quem não respondeu (art. 5º, IV, e § 2º, I, III e IV).
> - A proposta precisa trazer descrição, valor unitário e total, CNPJ, endereço e telefone, data e nome do responsável (§ 2º, II). Proposta sem esses dados não entra.
> - Validade: cotação e site com até 6 meses antes da divulgação do edital; contratações similares e notas fiscais com até 1 ano (art. 5º, II a V). Fora disso, só com justificativa e atualização pelo índice (§ 3º).
> - Para sites, guarde print com data e hora de acesso (art. 5º, III).
> - Compare o mesmo objeto: mesma especificação, quantidade, prazo e garantia. Preço de objeto diferente distorce a média.

## Etapa 6 — Mapa de Gerenciamento de Riscos

Gera `05-MGR.docx` com os riscos do planejamento, da seleção do fornecedor e da futura gestão do contrato.

46. Riscos já conhecidos.
47. Política de gestão de riscos do órgão.
