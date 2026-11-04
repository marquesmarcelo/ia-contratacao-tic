# Contratação direta (inexigibilidade e dispensa)

> Usado pelo Chefe da Equipe da Contratação quando a Etapa 0 indicar contratação sem licitação. Fundamentos conferidos na base: Lei 14.133, arts. 23, § 4º, 53, § 4º, 72, 74 e 75; IN SGD/ME 94/2022, art. 1º, § 1º; IN SEGES/ME 67/2021; Lista de Verificação de TIC da AGU, listas específicas de inexigibilidade e de dispensa.

## Quando cai aqui

| Situação | Hipótese | O que precisa provar |
|---|---|---|
| Só um produtor, empresa ou representante exclusivo fornece o bem ou serviço | inexigibilidade, art. 74, I | atestado ou contrato de exclusividade, declaração do fabricante ou outro documento idôneo; vedada a preferência por marca (art. 74, § 1º). Autodeclaração da empresa não vale (IN 94, art. 5º, XII) |
| Valor abaixo do limite de dispensa para bens e serviços | dispensa, art. 75, II | somatório do que a unidade gestora gastou no exercício com objetos da mesma natureza (art. 75, § 1º, I). O valor do inciso é atualizado por decreto: confira o vigente antes de usar |
| Outra hipótese do art. 75 (emergência, licitação deserta ou fracassada etc.) | dispensa, art. 75, III e seguintes | os requisitos do inciso usado |

Marca ou part number vendido por várias revendas **não** é inexigibilidade: há competição entre as revendas, então é licitação com a justificativa do art. 41, I (fluxo normal).

## Documentos (Lei 14.133, art. 72)

| Inciso | Documento | Quem escreve | Observação |
|---|---|---|---|
| I | DFD | Requisitante | sempre |
| I | ETP, se for o caso | Requisitante e Técnico | na inexigibilidade de TIC, o ETP é que demonstra por que só aquela solução atende; na dispensa por valor, a IN 94 é facultativa, salvo os arts. 6º e 24 (IN 94, art. 1º, § 1º) |
| I | Análise de riscos (MGR) | os três | proporcional ao objeto |
| I | TR | os três | mesmo modelo AGU de compras ou serviços, sem os itens de disputa |
| II e VII | Estimativa de despesa e **justificativa de preço** | Administrativo e Técnico | pela IN 65/2021 (art. 23 da Lei). Se não houver como estimar assim, a contratada comprova que o preço é o praticado com outros contratantes, com notas fiscais de até 1 ano ou outro meio idôneo (art. 23, § 4º). Use o Mapa de Preços com essas notas como fonte |
| III | Parecer jurídico e pareceres técnicos | Consultor Jurídico | controle prévio de legalidade também na contratação direta (art. 53, § 4º), com a lista específica de inexigibilidade ou de dispensa da AGU |
| IV | Compatibilidade com os recursos orçamentários | Requisitante e Técnico | como no TR (IN 94, art. 21) |
| V | Habilitação e qualificação mínima do contratado | Administrativo | certidões e documentos do contratado |
| VI | **Razão da escolha do contratado** | Técnico e Administrativo | na inexigibilidade, a exclusividade; na dispensa, o resultado da disputa eletrônica ou da cotação |
| VIII | Autorização da autoridade competente | Administrativo prepara a minuta | — |
| parágrafo único | Divulgação do ato ou do extrato do contrato em sítio oficial | Administrativo | registro no histórico |

Saída: `artefatos_ia/` com `01-DFD.docx`, `02-ETP.docx` (se for o caso), `04-TR-*.docx`, `05-MGR.docx`, `06-Mapa-de-Precos.xlsx` e `10-Instrucao-Contratacao-Direta.docx` (hipótese legal, documento de exclusividade ou de valor, justificativa de preço, razão da escolha, habilitação, minuta de autorização e de extrato).

## Fluxo

```
Etapa 0 → hipótese (inexigibilidade art. 74, I / dispensa art. 75, II / outra) e documento que a prova
Etapa 1 → DFD
Etapa 2 → ETP (inexigibilidade: por que só essa solução; dispensa por valor: facultativo)
Etapa 3 → TR e anexos aplicáveis (sem regras de disputa)
Etapa 4 → Instrução da contratação direta (no lugar do Edital)
          • inexigibilidade: documento de exclusividade conferido, razão da escolha, justificativa de preço
          • dispensa por valor: somatório do exercício, aviso e disputa no Sistema de Dispensa Eletrônica
            (IN SEGES/ME 67/2021, arts. 4º e 6º; aviso de no mínimo 3 dias úteis, Lei 14.133, art. 75, § 3º)
Etapa 5 → Mapa de Preços ou justificativa de preço (art. 23, § 4º)
Etapa 6 → MGR
Etapa 7 → revisão, parecer do Consultor Jurídico (lista específica da AGU), aprovação
```

Não há Licitante nem Pregoeiro. Na dispensa eletrônica há disputa de lances, mas sem fase de impugnação do edital; o Chefe pode pedir ao Licitante uma leitura do aviso e do TR só para achar ambiguidade.

## Pontos que o Consultor Jurídico confere

- Inexigibilidade: documento de exclusividade idôneo e atual, emitido por quem pode atestar; ausência de preferência por marca; justificativa de preço com notas fiscais de outros contratantes.
- Dispensa por valor: valor vigente do limite; somatório do exercício; aviso publicado; contratação dentro da natureza do objeto.
- Em todas: os oito incisos do art. 72 presentes e a divulgação do parágrafo único.
