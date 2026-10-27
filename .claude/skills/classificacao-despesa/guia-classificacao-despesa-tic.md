---
titulo: "Guia de classificação da despesa para contratações de TIC (derivado do Manual de Classificação da Despesa Pública, 2ª ed., CGE-PE, 2021)"
tipo: orientacao
url_origem: base-legal/manuais/manual-classificacao-despesa-publica.md
baixado_em: 2026-10-27
situacao: "guia derivado de manual estadual; validar subelementos com a classificação federal (SIAFI/MTO) do órgão"
---

# Guia de classificação da despesa para contratações de TIC

## Como usar este guia

- Fonte única: `base-legal/manuais/manual-classificacao-despesa-publica.md` (Manual da Controladoria-Geral do Estado de Pernambuco, 2ª ed., atualizado até dezembro de 2020, L. 261). Toda referência "L. x" aponta para a linha desse arquivo.
- Marcadores usados abaixo:
  - **[NACIONAL]**: regra que o próprio manual atribui a norma de alcance nacional (Lei 4.320/1964, Portaria Interministerial STN/SOF 163/2001, Portaria Conjunta STN/SOF 2/2017, Portaria STN 448/2002, LRF).
  - **[ELEMENTO]**: definição de elemento de despesa (dois dígitos "ee"). O manual não cita a fonte dessas definições, mas a estrutura categoria/grupo/modalidade/elemento é atribuída à Portaria 163 (L. 281-291) e os elementos 39 e 40 são atribuídos à Portaria Conjunta STN/SOF 2/2017 (L. 226-233).
  - **[PE]**: subelemento (dois últimos dígitos "dd") ou regra baseada em norma do Estado de Pernambuco. O manual diz que o desdobramento é facultativo (L. 291) e que a SEFAZ-PE fez "ajustes, inclusões e exclusões de inúmeras naturezas da despesa no âmbito do Sistema Corporativo e-Fisco" (L. 233-235). **Nenhum subelemento [PE] deve ser usado em empenho federal sem conferência no SIAFI/MTO.**
- O manual não trata de CATMAT/CATSER. O código de catálogo do item sai do Catálogo de Materiais e Serviços do Compras.gov.br, não deste guia.
- O manual é anterior à Lei 14.133/2021 e ainda cita a Lei 8.666/1993 (ex.: L. 4302, L. 10077). Isso não afeta a classificação orçamentária, mas não use o manual como base para regra de licitação.

---

## 1. Estrutura do código e conceitos básicos

### 1.1 Estrutura da natureza de despesa [NACIONAL]

"De acordo com o art. 5º da Portaria Interministerial STN/SOF nº 163/2001, a estrutura da natureza da despesa a ser observada na execução orçamentária de todas as esferas de governo será: c.g.mm.ee.dd" (L. 281-285).

| Posição | Significado (L. 286-291) | Exemplo em TIC |
|---|---|---|
| c | categoria econômica | 3 (corrente) ou 4 (capital) |
| g | grupo de natureza da despesa | 3 (Outras Despesas Correntes) ou 4 (Investimentos) |
| mm | modalidade de aplicação | 90 (Aplicação Direta) |
| ee | elemento de despesa | 30, 36, 39, 40, 52 |
| dd | "desdobramento, facultativo, do elemento de despesa" | subelemento, varia por ente |

"O código da natureza de despesa orçamentária é composto por seis dígitos, desdobrado até o nível de elemento ou, opcionalmente, por oito, contemplando o desdobramento facultativo do elemento - subelemento ou item de gasto" (L. 307-309).

Elemento 99 ("A Classificar"): "vedada a sua utilização na execução orçamentária" (L. 1443-1446). Modalidade 99 também é vedada na execução (L. 730-734).

### 1.2 Categoria econômica [NACIONAL, Lei 4.320/1964, art. 12]

- **3 - Despesas Correntes**: "todas as despesas que não contribuem, diretamente, para a formação ou aquisição de um bem de capital" (L. 327-329). Desdobram-se em custeio e transferências correntes (L. 332-334).
- **Custeio**: despesas "relacionadas com a manutenção dos serviços anteriormente criados" (L. 335-337). Exemplos do manual: "material de consumo, pessoal, serviços de terceiros etc." (L. 338-339).
- **4 - Despesas de Capital**: "aquelas despesas que contribuem, diretamente, para a formação ou aquisição de um bem de capital" (L. 348-349). Desdobram-se em investimentos, inversões financeiras e transferências de capital (L. 350-352).
- **Investimentos**: "correspondem à aquisição ou formação de novos bens ou adicionam novo valor aos já existentes", incluindo "equipamentos, material permanente" (L. 353-360). Exemplo literal do manual: "aquisição de computadores novos" (L. 362).
- **Inversões financeiras**: "aquisição de imóveis ou bens de capital já em utilização" (L. 364-365). Atenção: equipamento de TI usado, comprado já em utilização, cai aqui pelo texto do manual, não em investimento.

### 1.3 Grupo de natureza da despesa [NACIONAL]

- **3 - Outras Despesas Correntes**: "aquisição de material de consumo, pagamento de diárias, contribuições, subvenções, [...] além de outras despesas da categoria econômica 'Despesas Correntes', não classificáveis nos demais grupos" (L. 403-408).
- **4 - Investimentos**: "Despesas orçamentárias com software e com o planejamento e a execução de obras, [...] e com a aquisição de instalações, equipamentos e material permanente" (L. 412-415). "Incluem-se também neste grupo as despesas necessárias à realização de programas especiais de trabalho, custeadas com recursos de operações de crédito" (L. 416-418).
- **5 - Inversões Financeiras**: L. 420-426.

Observação: o manual traz naturezas 4.4.90.30, 4.4.90.36, 4.4.90.39 e 4.4.90.40 (material de consumo e serviços dentro do grupo Investimentos). Ele não explica quando usá-las. O único indício textual está na L. 416-418 (programas custeados com operações de crédito) e no subelemento 4.4.90.40.13, que diz: "Despesa executada com recurso proveniente de operações de crédito" (L. 9887-9888). Uso de 4.4.90.40 para serviço de TIC: **confirmar com a área de orçamento**.

### 1.4 Modalidade de aplicação [NACIONAL]

- Finalidade: indicar se os recursos são aplicados diretamente ou mediante transferência, e evitar dupla contagem (L. 437-442).
- **90 - Aplicações Diretas**: "Aplicação direta, pela unidade orçamentária, dos créditos a ela alocados [...] no âmbito da mesma esfera de governo" (L. 653-658). É a modalidade padrão de uma contratação de TIC com fornecedor privado.
- **91**: quando o recebedor "também for órgão, fundo, autarquia, fundação, empresa estatal dependente ou outra entidade constante desses orçamentos, no âmbito da mesma esfera de Governo" (L. 660-670).
- **93 / 94**: operação com consórcio público do qual o ente participe / não participe (L. 681-703).

### 1.5 Material de consumo x material permanente

**Critérios do manual [PE: Decreto Estadual nº 39.639/2013, art. 2º, XXI e XXII]** (L. 3619-3644, repetidos em L. 7367-7391, 8328-8349, 10195-10214):

- "bem de consumo (material): todo artigo, peça, item ou gênero que, em razão de uso, perde sua identidade física, suas características individuais e operacionais e tenha durabilidade prevista limitada a 2 (dois) anos" (L. 3621-3623).
- É material de consumo o que atende a um dos critérios (L. 3630-3642):
  - a) **fragilidade**: "estrutura for quebradiça, deformável ou danificável, caracterizando sua irrecuperabilidade ou perda de sua identidade ou funcionalidade";
  - b) **perecibilidade**: "sujeito a modificações (químicas ou físicas) ou se deteriora ou perde sua característica pelo uso normal";
  - c) **descartabilidade**: "quando, após a sua utilização, se pode descartar";
  - d) **incorporabilidade**: "destinado à incorporação a outro bem, não podendo ser retirado sem que haja prejuízo das condições e características de funcionamento do bem principal";
  - e) **transformabilidade**: "destinado à transformação, composição ou fabricação de outro material ou produto";
  - f) **finalidade**: "adquirido para consumo imediato ou para reposição".
- "Todo o material que for enquadrado nesses conceitos deve ser considerado de consumo" (L. 3643-3644). No elemento 52: "Se um bem apresentar qualquer uma das características acima relacionadas, será considerado como material de consumo, classificado no elemento 30" (L. 10219-10220).

**Material permanente** (texto do elemento 52, L. 10190-10194): "aquisição de bens de capital que, em razão de sua utilização, não perdem a identidade física, ainda que utilizados ou destinados a serviços de natureza administrativa, e/ou que tenham sua durabilidade presumida superior a dois anos". O subelemento genérico 4.4.90.52.99 [PE] acrescenta: bem "passível de controle individual, de movimento próprio, ou de remoção por força alheia que, em razão do uso, não perde sua identidade física e autonomia de funcionamento e que não se consome, não se altera substancialmente pelo uso, e tenha durabilidade prevista superior a 02 (dois) anos" (L. 10656-10663).

**Referência à Lei 4.320/1964 [NACIONAL]**: nos subelementos de DEA, o manual descreve o material de consumo como aquele que, "em razão de seu uso corrente e da definição da Lei Federal nº 4.320/64, perde normalmente sua identidade física e/ou tem sua utilização limitada a dois anos" (L. 6712-6714; também L. 10798-10803).

**Bens de baixo valor [PE]**: o subelemento 3.3.90.30.58 "Bens Móveis Não Incorporáveis" classifica como consumo equipamentos "com baixo valor unitário de aquisição", com base na Portaria Conjunta SAD/SEFAZ nº 152/2016, de Pernambuco (L. 4190-4194). Regra estadual. Não aplicar na União sem norma equivalente do órgão.

Os critérios de fragilidade etc. aparecem no manual com base em decreto estadual. O manual cita a Portaria STN 448/2002 apenas para a regra de material por encomenda (item 1.7). A norma federal sobre consumo x permanente aplicável ao órgão deve ser confirmada com a contabilidade.

### 1.6 Serviço de terceiros: pessoa física x pessoa jurídica [ELEMENTO]

- **36 - Outros Serviços de Terceiros - Pessoa Física**: "serviços prestados por pessoa física pagos diretamente a esta e não enquadrados nos elementos de despesa específicos" (L. 1035-1041).
- **39 - Outros Serviços de Terceiros - Pessoa Jurídica**: "prestação de serviços por pessoas jurídicas para órgãos públicos, **exceto as relativas aos Serviços de Tecnologia da Informação e Comunicação – TIC**" (L. 1057-1059).
- **40 - Serviços de TIC - Pessoa Jurídica**: ver seção 2.1. O elemento 40 é só para PJ. Serviço de TIC prestado por pessoa física vai para o elemento 36 (ex.: 3.3.90.36.06 inclui "elaboração e manutenção de software de aplicação por pessoa física", L. 4677-4679).
- **37 - Locação de Mão de Obra**: serviços por PJ "nos casos em que o contrato especifique o quantitativo físico do pessoal a ser utilizado" (L. 1045-1048). O manual acrescenta que se trata de atividades "que não constam no plano de cargo e salário do órgão" (L. 5081-5086).
- **35 - Serviços de Consultoria**: contratos com PF ou PJ "nas áreas de consultorias técnicas ou auditorias financeiras ou jurídicas, ou assemelhadas" (L. 1029-1031). Finalidade, segundo o subelemento 35.01 [PE]: "emissão de parecer ou laudo técnico com o objetivo de orientar a tomada de decisões" (L. 4602-4603).
- **34**: mão de obra de terceirização computada no limite de pessoal da LRF (art. 18, § 1º) (L. 1020-1025).

### 1.7 Material por encomenda [NACIONAL, Portaria STN 448/2002, art. 6º]

"a despesa com confecção de materiais por encomenda, somente deverá ser classificada como serviços de terceiros se o próprio órgão ou entidade fornecer a matéria-prima. Caso contrário, deverá ser classificada na natureza 4.4.90.52, quando se tratar de material permanente, ou na natureza 3.3.90.30, quando for material de consumo" (L. 4646-4651; repetido em L. 5209-5214 e L. 9198-9203).

Atenção: no elemento 36, logo depois, o manual diz o contrário: "Não havendo fornecimento de matéria-prima, ainda que a nota fiscal seja de venda, como ocorre no fornecimento de refeições preparadas, a despesa será classificada como serviço de terceiros" (L. 4655-4657). Prevalece a regra citada da Portaria 448 (L. 4646-4651), repetida no elemento 39. Em caso concreto, confirmar.

### 1.8 Despesas de Exercícios Anteriores (DEA) [NACIONAL, Lei 4.320/1964, art. 37]

Elemento 92: "Art. 37. As despesas de exercícios encerrados, para as quais o orçamento respectivo consignava crédito próprio, com saldo suficiente para atendê-las, que não se tenham processado na época própria, bem como os Restos a Pagar com prescrição interrompida e os compromissos reconhecidos após o encerramento do exercício correspondente, poderão ser pagas à conta de dotação específica consignada no orçamento, discriminada por elemento, obedecida, sempre que possível, a ordem cronológica." (L. 1374-1384; também L. 6657-6667 e L. 10741-10751).

Subelementos de DEA relevantes para TIC [PE]:
- 3.3.90.92.30 - Material de Consumo (L. 6710-6715)
- 3.3.90.92.36 - Serviços de Terceiros – Pessoa Física (L. 6746-6749)
- 3.3.90.92.38 - Arrendamento Mercantil (L. 6757-6760)
- 3.3.90.92.39 - Serviços de Terceiros – Pessoa Jurídica (L. 6762-6765)
- 3.3.90.92.40 - Serviços de Tecnologia da Informação e Comunicação - Pessoa Jurídica – DEA (L. 6767-6771)
- 4.4.90.92.02 - Equipamentos e Material Permanente – Imobilizáveis (L. 10759-10764)
- 4.4.90.92.30 - Material de Consumo Imediato (L. 10796-10803)
- 4.4.90.92.40 - Serviços de Tecnologia da Informação e Comunicação - Pessoa Jurídica (L. 10830-10834)

---

## 2. O que o manual diz sobre TIC

### 2.1 Elemento 40 - Serviços de TIC - Pessoa Jurídica [ELEMENTO; criado pela Portaria Conjunta STN/SOF 2/2017, L. 226-233]

Definição literal (L. 1076-1088):

> "Despesas orçamentárias decorrentes da prestação de serviços por pessoas jurídicas para órgãos e entidades da Administração Pública, relacionadas à Tecnologia da Informação e Comunicação - TIC, não classificadas em outros elementos de despesa, tais como: locação de equipamentos e softwares, desenvolvimento e manutenção de software, hospedagens de sistemas, comunicação de dados, serviços de telefonia fixa e móvel, quando integrarem pacote de comunicação de dados, suporte a usuários de TIC, suporte de infraestrutura de TIC, serviços técnicos profissionais de TIC, manutenção e conservação de equipamentos de TIC, digitalização, outsourcing de impressão e serviços relacionados a computação em nuvem, treinamento e capacitação em TIC, tratamento de dados, conteúdo de web; e outros congêneres."

O mesmo texto aparece em 3.3.90.40 (L. 6014-6027) e em 4.4.90.40 (L. 9779-9792).

**O que inclui**: a lista acima.
**O que exclui, pelo próprio texto**:
- serviços de TIC "classificados em outros elementos de despesa" (L. 1080);
- serviço prestado por pessoa física (o elemento é "Pessoa Jurídica");
- telefonia fixa e móvel que **não** integre pacote de comunicação de dados: vai para o elemento 39 ("serviços de comunicação (telex, correios, telefonia fixa e móvel, que não integrem pacote de comunicação de dados)", L. 1060-1062);
- aquisição de bens (equipamentos vão para o 52, insumos para o 30).

**Elemento 39 [ELEMENTO]**, para contraste: "exceto as relativas aos Serviços de Tecnologia da Informação e Comunicação – TIC" (L. 1057-1059), e inclui "locação de equipamentos e materiais permanentes" em geral (L. 1067-1068).

#### Subelementos de 3.3.90.40 no manual [PE]

| Código (como no manual) | Título | Definição literal | Linha |
|---|---|---|---|
| 3.3.90.40.01 | LOCAÇÃO DE SOFTWARE (LICENÇAS) | "Despesas com licenças de uso de software de processamento de dados. Exemplos: programa de administração e controle de estoques." | 6029-6032 |
| 3.3.90.40.02 | LOCAÇÃO DE EQUIPAMENTOS DE TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO | "Despesas com aluguel de máquinas e equipamentos de interesse da Administração Pública. Exemplos: Locação de equipamentos de processamento de dados." | 6034-6039 |
| 3.3.90.40.03 | SERVIÇOS DE CAPACITAÇÃO E TREINAMENTO EM TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO (TIC) | "Despesas com contratação de pessoa jurídica responsável por promoção, implementação, capacitação, divulgação e transferência de conhecimentos acerca de recursos de Tecnologia da informação." | 6043-6048 |
| 3.3.90.40.04 | DESENVOLVIMENTO E MANUTENÇÃO DE SOFTWARE | "Despesas com elaboração, correção de defeitos e deficiências em software, despesas relacionadas ao desenvolvimento de novas funcionalidades para melhorar a aplicação e uso de softwares e despesas com a sustentação de sistemas." | 6050-6055 |
| 3.3.90.40.05 | REPARO, MANUTENÇÃO E CONSERVAÇÃO DE EQUIPAMENTOS DE PROCESSAMENTO DE DADOS (TIC) | "Despesas com serviços de reparos, consertos, revisões, manutenções e adaptações de equipamentos de processamento de dados e periféricos, etc." | 6057-6061 |
| 3.3.90.40.06 | HOSPEDAGEM DE SISTEMAS | "Despesas com serviço de manutenção de endereço web (.pe.gov.br) específico para o sistema, com segurança cibernética especializada no rastreamento de ataques e vandalismos contra o site ou portal hospedado, com suporte para implementar segurança e serviços de recuperação de sites ou portais danificados por ataques, com manutenção corretiva do sistema e com cópia de segurança." (texto ligado ao domínio de PE) | 6063-6070 |
| 3.3.90.40.07 | SERVIÇOS TÉCNICOS PROFISSIONAIS DE TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO (INCLUINDO SUPORTE A USUÁRIOS E INFRAESTRUTURA) | "Serviços prestados por profissionais técnicos da área de informática, tais como serviços de acesso e utilização de softwares, serviços de consultoria na área de informática, serviços de implantação de sistemas, serviços de instalação de softwares e equipamentos de informática e sustentação de ambiente computacional." | 6072-6080 |
| 3.3.90.40.08 | SERVIÇOS DE COMPUTAÇÃO EM NUVEM | "Despesas com o fornecimento de serviços de computação – servidores, armazenamento, bancos de dados, rede, software por empresas denominadas provedoras de nuvem." | 6082-6086 |
| 3.3.90.40.09 | SERVIÇOS DE TELEFONIA MÓVEL | "Despesas decorrentes da utilização dos serviços de telefonia móvel (celular), com tarifas decorrentes da utilização de serviços de tráfego de voz, imagem e dados." | 6090-6094 |
| 3.3.90.40.10 | SERVIÇOS DE TELEFONIA FIXA | "Despesas com serviços de telefonia fixa (despesas relativas ao serviço de ponto de voz, incluindo instalação e configuração, serviço de tráfego de rede e extra rede, outros serviços de tráfego – 0800, 0400), etc" | 6096-6100 |
| 3.3.90.40.11 | SERVIÇOS DE INFRAESTRUTURA E GERENCIAMENTO DE COMUNICAÇÃO DE DADOS E REDES | "Despesas com serviços teleprocessamento do PE-Conectado [...]" (rede corporativa estadual) | 6102-6109 |
| 3.3.90.40.12 | SERVIÇOS DE TELEPROCESSAMENTO | "Despesas com serviços de teleprocessamento." Exemplos incluem a rede PE-Multidigital, "acesso a banda larga, locação de circuito de dados locais ou interurbanos [...], serviços de rede privativa virtual, SLDD, [...] internet, IP direto [...]" | 6111-6124 |
| 3.3.90.40.13 | CERTIFICAÇÃO DIGITAL | "Despesas com serviços de fornecimento de certificados digitais e-CPF e e-CNPJ (ambos Tipo A3 com fornecimento de mídia token) e de prestação de serviços de visitas presenciais para emissão de certificados." | 6126-6130 |
| 3.3.90.40.14 | DIGITALIZAÇÃO | "Despesas com serviços de digitalização de documentos físicos para o formato digital." | 6136-6139 |
| 3.3.90.40.15 | OUTSOURCING DE IMPRESSÃO | "Despesas caracterizadas pela prestação de serviços de produção de cópias, digitalizações e impressões, com o fornecimento dos insumos, solução de bilhetagem e, principalmente, com existência de manutenção preventiva e corretiva garantindo disponibilidade dos referidos serviços." | 6141-6146 |
| 3.3.90.40.16 | SERVIÇOS DE VIDEOMONITORAMENTO | monitoramento de bens e pessoas, sistemas de segurança eletrônicos, "inclusive a manutenção dos equipamentos, bem como despesa com aquisição de aparelhos e equipamentos necessários ao funcionamento" | 6148-6155 |
| 3.3.90.40.17 | CONTEÚDO WEB | "Despesas com contratação de pessoa jurídica que realize planejamento e produção de textos, vídeos e infográficos para disposição na web." | 6157-6160 |
| 3.3.90.40.94 / .96 / .97 | SFI / REFIN-NPCO / Suprimento Individual | itens transitórios de regimes estaduais (Lei Estadual 7.741/78) | 6162-6231 |

#### Subelementos de 4.4.90.40 no manual [PE]

Mesmos títulos e textos de .01 a .10, .12 a .15, .94 e .97 (L. 9794-9928). Diferenças:
- não há 4.4.90.40.11, .16 e .17;
- 4.4.90.40.13 acrescenta "Despesa executada com recurso proveniente de operações de crédito" (L. 9887-9888);
- 4.4.90.40.15 tem texto curto: "Despesa com serviço de terceirização de impressão." (L. 9895-9897);
- o título do elemento em L. 9779-9780 omite "Pessoa Jurídica".

### 2.2 Material de consumo de TI (elemento 30) [ELEMENTO + PE]

Elemento 30 [ELEMENTO] inclui "material gráfico e de processamento de dados; aquisição de disquete; [...] material para telecomunicações" e "outros materiais de uso não duradouro" (L. 975-994).

Subelementos [PE]:
- **3.3.90.30.17 - MATERIAL DE PROCESSAMENTO DE DADOS**: "Despesas com aquisição de materiais utilizados no funcionamento e manutenção de sistemas de processamento de dados, inclusive peças destinadas à reposição direta no equipamento ou mesmo para estoque. Exemplos: cartuchos de tinta, capas plásticas protetoras para micros e impressoras, CD-ROM virgem, DVD virgem, etiquetas em formulário contínuo, fita magnética, fita para impressora, formulário contínuo, mouse PAD, peças e acessórios para computadores e periféricos: mouse, teclados e outros, toner para impressora lazer, cartões magnéticos, pendrive, etc." (L. 3801-3815; igual em 4.4.90.30.17, L. 8427-8436).
- **3.3.90.30.16 - MATERIAL DE EXPEDIENTE**: também lista "toner" entre os exemplos (L. 3798).
- **3.3.90.30.26 - MATERIAL ELÉTRICO E ELETRÔNICO**: "circuitos eletrônicos, [...] fios e cabos, [...] pilhas e baterias" (L. 3917-3927).
- **3.3.90.30.30 - MATERIAL PARA COMUNICAÇÕES**: "componentes, circuitos impressos ou integrados, peças ou partes de equipamentos de comunicações, materiais para instalações, headphones (peça de equipamento de central telefônica), headsets (peça de equipamento de central telefônica), aparelho telefônico (observar o custo de aquisição), etc." (L. 3963-3971).
- **3.3.90.30.25 - MATERIAL PARA MANUTENÇÃO DE BENS MÓVEIS**: peças de reposição de aparelhos e máquinas em geral (L. 3906-3915).
- **3.3.90.30.45 - MATERIAL TÉCNICO PARA SELEÇÃO E TREINAMENTO**: apostilas, manuais (L. 4095-4100).
- **3.3.90.30.58 - BENS MÓVEIS NÃO INCORPORÁVEIS**: baixo valor, Portaria Conjunta SAD/SEFAZ-PE 152/2016 (L. 4190-4204).

### 2.3 Equipamentos de TI (elemento 52) [ELEMENTO + PE]

Elemento 52 [ELEMENTO]: inclui "aparelhos e equipamentos de comunicação", "máquinas, aparelhos e equipamentos gráficos e equipamentos diversos", "máquinas, aparelhos e utensílios de escritório", "outros materiais permanentes" (L. 1171-1185).

Subelementos [PE]:
- **4.4.90.52.35 - EQUIPAMENTOS DE PROCESSAMENTO DE DADOS**: "Despesas com aquisições de máquinas, aparelhos e equipamentos utilizados em processamento de dados de qualquer natureza, exceto quando for aquisição de peças destinadas à reposição diretamente ao equipamento ou mesmo para estoque, quando, então, deverá ser classificada como material de consumo. Exemplos: caneta óptica, leitor ótico, computador, notebook, laptop, netbook, controladora de linhas, data show, fitas e discos magnéticos, DVD-RW, equipamento de videoconferência, gravador de DVD, impressora, Joystick, kit multimídia, lightpen, leitora, micro e minicomputadores, mesa digitalizadora, modem, monitor de vídeo, placas, processador, roteadores, scanner, storage, teclado para micro, urna eletrônica, webcam, switch, Hub e etc." (L. 10443-10458).
- **4.4.90.52.06 - APARELHOS E EQUIPAMENTOS DE COMUNICAÇÃO**: "material considerado permanente, portátil ou transportável, de uso em comunicações, que não se incorporem em instalações [...]. Exemplos: antena parabólica, aparelhos de telefonia, bloqueador telefônico, central telefônica, [...] PABX, rádio receptor, [...]" (L. 10240-10248).
- **4.4.90.52.30 - MÁQUINAS E EQUIPAMENTOS ENERGÉTICOS**: "não incorporáveis a instalações [...]. Exemplos: [...] estabilizador, gerador, [...] no-break, [...]" (L. 10393-10400).
- **4.4.90.52.24 - EQUIPAMENTO DE PROTEÇÃO, SEGURANÇA E SOCORRO**: inclui "alarme", "circuito interno de televisão" (L. 10367-10376).
- **4.4.90.52.33 - EQUIPAMENTOS PARA ÁUDIO, VÍDEO E FOTO**: inclui "data show", "projetor", "televisor", "microfone" (L. 10422-10431).
- **4.4.90.52.34 - MÁQUINAS, UTENSÍLIOS E EQUIPAMENTOS DIVERSOS**: inclui "catraca eletrônica", "leitor de código de barra" (L. 10433-10441).
- **4.4.90.52.32 - MÁQUINAS E EQUIPAMENTOS GRÁFICOS**: inclui "copiadora", "duplicadora" (L. 10411-10420).
- **4.4.90.52.87 - MATERIAL DE CONSUMO DE USO DURADOURO**: "materiais de consumo controlados como de uso duradouro" (L. 10625-10628).

Outros pontos do manual:
- Computadores para distribuição gratuita: 4.4.90.32.80 [PE], "Exemplos: veículos, computadores e equipamentos em geral" (L. 8642-8646).
- Computadores como prêmio: 3.3.90.31.01 [PE], "Exemplos: computadores etc." (L. 4298-4303).
- Instalações incorporáveis ao imóvel: elemento 51 [ELEMENTO], "instalações que sejam incorporáveis ou inerentes ao imóvel" (L. 1163-1169; 4.4.90.51.92, L. 10130-10133). O manual não cita cabeamento de rede nem sala-cofre.

### 2.4 Software

O que o manual diz, e só isso:
- Grupo 4 - Investimentos inclui "Despesas orçamentárias com software" (L. 412) [NACIONAL].
- Elemento 40 inclui "locação de equipamentos e softwares, desenvolvimento e manutenção de software" e "serviços relacionados a computação em nuvem" (L. 1081-1088) [ELEMENTO].
- 3.3.90.40.01 e 4.4.90.40.01 "LOCAÇÃO DE SOFTWARE (LICENÇAS)": "licenças de uso de software de processamento de dados" (L. 6029-6032; L. 9794-9797) [PE].
- 3.3.90.40.07: "serviços de acesso e utilização de softwares", "serviços de instalação de softwares" (L. 6076-6080) [PE].
- 3.3.90.40.08: nuvem, incluindo "software por empresas denominadas provedoras de nuvem" (L. 6084-6086) [PE].
- 3.3.90.40.04: desenvolvimento, manutenção e "sustentação de sistemas" (L. 6050-6055) [PE].
- Desenvolvimento por pessoa física: 3.3.90.36.06 (L. 4677-4679) e 4.4.90.36.57 "SOFTWARES, PRODUÇÃO DE PROGRAMAS APLICATIVOS E MICROFILMAGEM", "prestados por PESSOA FÍSICA", "Os softwares de aplicação são aqueles desenvolvidos para atender as necessidades específicas de um determinado usuário, executados a pedido e de acordo com as solicitações deste" (L. 9027-9042) [PE].
- 4.4.90.39.08 "MARCAS, DIREITOS E PATENTES INDUSTRIAIS", "conforme conceitos da Lei nº 9.279/96" (L. 9240-9243) [PE]. Não menciona software.
- 3.3.93.39 (modalidade 93) ainda lista "software" entre os serviços do elemento 39 (L. 7743). É texto anterior à criação do elemento 40 e conflita com L. 1057-1059.

**O que o manual NÃO trata**: aquisição de licença perpétua, cessão definitiva de direito de uso, subscrição (assinatura) de software, SaaS como categoria própria, suporte e atualização de versão contratados com o fabricante, e a fronteira entre software como investimento (L. 412) e licença como serviço (L. 6029-6032). Nesses casos: **não tratado no manual — confirmar com a área de orçamento**.

### 2.5 Suporte e manutenção

- Suporte a usuários e de infraestrutura (PJ): elemento 40 (L. 1083-1085); subelemento 3.3.90.40.07 [PE] (L. 6072-6080).
- Manutenção de equipamentos de TI (PJ): 3.3.90.40.05 [PE] (L. 6057-6061). O 3.3.90.39.17 exclui expressamente: "exceto de processamento de dados" (L. 5334-5335).
- Manutenção de equipamentos por pessoa física: 3.3.90.36.18 [PE], "conserto/revisão em máquinas e equipamentos de processamento de dados e periféricos" (L. 4749-4757).
- Manutenção de software: 3.3.90.40.04 [PE] (L. 6050-6055).
- Garantia estendida, suporte do fabricante (hardware ou software) e contratos de "subscrição de suporte": não tratado no manual — confirmar com a área de orçamento.

### 2.6 Locação de equipamentos de TI

- PJ: elemento 40, "locação de equipamentos e softwares" (L. 1081); 3.3.90.40.02 [PE] (L. 6034-6039).
- PF: 3.3.90.36.16 [PE], "aluguel de máquinas de escritório, de processamento de dados" (L. 4735-4740).
- Com opção de compra: elemento 38 - Arrendamento Mercantil [ELEMENTO] (L. 1050-1053); 3.3.90.38.01 [PE], "Exemplos: máquinas de escritório [...], máquinas de processamento de dados" (L. 5157-5162).
- Conflito no texto: 3.3.90.39.12 [PE] ainda lista "de processamento de dados (computador, impressora, scanner, copiadoras etc.)" como locação no elemento 39 (L. 5289-5296; também 4.4.90.39.12, L. 9260-9270). Pela definição dos elementos, locação de equipamento de TIC é elemento 40 (L. 1057-1059 e L. 1081).

### 2.7 Outsourcing de impressão

- Elemento 40 cita "outsourcing de impressão" (L. 1086).
- 3.3.90.40.15 [PE] (L. 6141-6146), texto na tabela da seção 2.1.
- Possível sobreposição: 3.3.90.39.83 "CÓPIA E REPRODUÇÃO DE DOCUMENTOS" [PE], "serviços de cópias xerográficas e reprodução de documentos, inclusive a locação e a manutenção de equipamentos reprográficos" (L. 5778-5781).

### 2.8 Telecomunicações e comunicação de dados

- Elemento 40: "comunicação de dados, serviços de telefonia fixa e móvel, quando integrarem pacote de comunicação de dados" (L. 1082-1084).
- Elemento 39: "serviços de comunicação (telex, correios, telefonia fixa e móvel, que não integrem pacote de comunicação de dados)" (L. 1060-1062).
- Subelementos 3.3.90.40.09 a 40.12 [PE] (L. 6090-6124). Os textos de 40.11 e 40.12 são construídos sobre redes do Estado (PE-Conectado, PE-Multidigital).
- Conflito: 3.3.90.39.59 tem título "ÁUDIO, VÍDEO E FOTO" mas descreve "tarifas decorrentes da utilização de serviços de tráfego de voz, imagem e dados. Exemplos: telefonia fixa [...]" (L. 5605-5611).
- Material: 3.3.90.30.30 [PE] (L. 3963-3971). Equipamento: 4.4.90.52.06 [PE] (L. 10240-10248).

### 2.9 Treinamento

- Treinamento em TIC por PJ: elemento 40, "treinamento e capacitação em TIC" (L. 1087-1088); 3.3.90.40.03 [PE] (L. 6043-6048).
- Treinamento em geral por PJ: 3.3.90.39.48 [PE] (L. 5519-5526).
- Por PF (instrutor): 3.3.90.36.28 [PE] (L. 4831-4839).
- Inscrição em congressos, seminários e afins: 3.3.90.39.22 [PE] (L. 5376-5383).
- Material didático: 3.3.90.30.45 [PE] (L. 4095-4100).

### 2.10 Outros serviços de TIC citados

- Hospedagem de sistemas: 3.3.90.40.06 [PE] (L. 6063-6070).
- Digitalização: 3.3.90.40.14 [PE] (L. 6136-6139).
- Certificação digital: 3.3.90.40.13 [PE] (L. 6126-6130).
- Videomonitoramento: 3.3.90.40.16 [PE] (L. 6148-6155).
- Conteúdo web: 3.3.90.40.17 [PE] (L. 6157-6160).
- Microfilmagem: 3.3.90.39.57 [PE] "EXCETO SERVIÇOS RELACIONADOS À TECNOLOGIA DE INFORMAÇÃO E COMUNICAÇÃO – TIC" (L. 5597-5603).

---

## 3. Tabela-guia: objeto de TIC → natureza de despesa sugerida

Regras de leitura:
- "Natureza (6 dígitos)" é o que o manual sustenta pelo texto do elemento. O subelemento entre parênteses é **[PE]** e serve só como pista para procurar o equivalente federal.
- Considera contratação direta pelo órgão com fornecedor privado (modalidade 90, L. 653-658).
- Bens novos. Bem de capital já em utilização vai para inversões financeiras (L. 364-365).

| Objeto | Natureza (6 dígitos) | Subelemento no manual [PE] | Justificativa no manual | Linha |
|---|---|---|---|---|
| Notebook | 4.4.90.52 | .35 | "computador, notebook, laptop, netbook" | 10453-10454 |
| Desktop (microcomputador) | 4.4.90.52 | .35 | "computador", "micro e minicomputadores"; categoria 4 cita "aquisição de computadores novos" | 10453-10456; 362 |
| Monitor | 4.4.90.52 | .35 | "monitor de vídeo" | 10457 |
| Servidor (rack/torre) | 4.4.90.52 | .35 | "servidor" não aparece nos exemplos; a definição abrange "equipamentos utilizados em processamento de dados de qualquer natureza" e cita "micro e minicomputadores". Confirmar subelemento | 10445-10446, 10456 |
| Storage | 4.4.90.52 | .35 | "storage" | 10457 |
| Switch, roteador, hub, modem | 4.4.90.52 | .35 | "modem", "roteadores", "switch, Hub" | 10457-10458 |
| Impressora, scanner | 4.4.90.52 | .35 | "impressora", "scanner" | 10455-10457 |
| Webcam, equipamento de videoconferência | 4.4.90.52 | .35 | "webcam", "equipamento de videoconferência" | 10455, 10458 |
| Projetor / data show | 4.4.90.52 | .35 ou .33 | aparece nos dois subelementos; confirmar | 10454; 10428 |
| No-break, estabilizador | 4.4.90.52 | .30 | "estabilizador", "no-break" | 10397-10399 |
| PABX, central telefônica, aparelho telefônico | 4.4.90.52 | .06 | "aparelhos de telefonia", "central telefônica", "PABX". Aparelho telefônico também aparece como consumo em 3.3.90.30.30 "(observar o custo de aquisição)" | 10245-10248; 3970 |
| CFTV, alarme | 4.4.90.52 | .24 | "alarme", "circuito interno de televisão" | 10373-10376 |
| Toner, cartucho de tinta | 3.3.90.30 | .17 (toner também em .16) | "cartuchos de tinta", "toner para impressora lazer" | 3811-3815; 3798 |
| Pendrive, mouse, mouse pad, CD/DVD virgem | 3.3.90.30 | .17 | listados nos exemplos | 3811-3815 |
| Teclado avulso | 3.3.90.30 ou 4.4.90.52 | .17 ou .35 | conflito: "teclados" em 30.17 e "teclado para micro" em 52.35. Confirmar | 3814; 10458 |
| Peças de reposição (placa, memória, disco, fonte) | 3.3.90.30 | .17 | "peças destinadas à reposição direta no equipamento ou mesmo para estoque"; 52.35 exclui peças de reposição. Atenção: 52.35 lista "placas, processador" nos exemplos | 3803-3805; 10446-10452; 10457 |
| Cabo de rede, patch cord | não tratado no manual — confirmar com a área de orçamento | (30.26 cita "fios e cabos" como material elétrico, sem menção a rede) | — | 3917-3927 |
| Cabeamento estruturado (instalação no prédio) | não tratado no manual — confirmar com a área de orçamento | (elemento 51 trata de "instalações que sejam incorporáveis ou inerentes ao imóvel", sem citar rede lógica) | — | 1163-1169 |
| Licença perpétua de software | não tratado no manual — confirmar com a área de orçamento | (o manual inclui "software" no grupo 4, L. 412, e só tem o subelemento "LOCAÇÃO DE SOFTWARE (LICENÇAS)", em 3.3.90.40.01 e 4.4.90.40.01) | — | 412; 6029-6032; 9794-9797 |
| Licença de uso por prazo determinado (locação de software) | 3.3.90.40 | .01 | elemento 40: "locação de equipamentos e softwares"; .01 "licenças de uso de software" | 1081; 6029-6032 |
| Subscrição SaaS | não tratado no manual — confirmar com a área de orçamento | (candidatos no texto: 3.3.90.40.01 licenças de uso; .07 "serviços de acesso e utilização de softwares"; .08 nuvem com "software por empresas denominadas provedoras de nuvem". O manual não diz qual prevalece) | — | 6029-6032; 6076-6077; 6084-6086 |
| Serviço de nuvem IaaS / PaaS | 3.3.90.40 | .08 | "servidores, armazenamento, bancos de dados, rede, software por empresas denominadas provedoras de nuvem" | 6082-6086 |
| Fábrica de software / desenvolvimento e manutenção (PJ) | 3.3.90.40 | .04 | "elaboração, correção de defeitos [...] novas funcionalidades [...] sustentação de sistemas" | 6050-6055 |
| Desenvolvimento de software por pessoa física | 3.3.90.36 | .06 | "elaboração e manutenção de software de aplicação por pessoa física" | 4677-4679 |
| Service desk / suporte a usuários | 3.3.90.40 | .07 | elemento 40: "suporte a usuários de TIC"; .07 "(incluindo suporte a usuários e infraestrutura)". Se o contrato fixar quantitativo de pessoal, ver dúvida 4.2-c | 1083-1084; 6072-6080 |
| Suporte de infraestrutura / sustentação de ambiente | 3.3.90.40 | .07 | "suporte de infraestrutura de TIC"; "sustentação de ambiente computacional" | 1084-1085; 6079-6080 |
| Consultoria em TI | 3.3.90.40 ou 3.3.90.35 | .07 (40) | .07 cita "serviços de consultoria na área de informática"; elemento 35 é consultoria técnica com fim de "parecer ou laudo técnico". Confirmar | 6077-6078; 1027-1031; 4602-4603 |
| Manutenção de equipamentos de TI (PJ) | 3.3.90.40 | .05 | elemento 40: "manutenção e conservação de equipamentos de TIC"; 39.17 exclui processamento de dados | 1085-1086; 6057-6061; 5334-5335 |
| Garantia estendida / suporte do fabricante | não tratado no manual — confirmar com a área de orçamento | — | — | — |
| Outsourcing de impressão | 3.3.90.40 | .15 | "produção de cópias, digitalizações e impressões, com o fornecimento dos insumos, solução de bilhetagem [...] manutenção preventiva e corretiva" | 1086; 6141-6146 |
| Locação de equipamentos de TI (PJ) | 3.3.90.40 | .02 | "locação de equipamentos e softwares"; conflito com 39.12 | 1081; 6034-6039; 5289-5296 |
| Locação de equipamento de TI com opção de compra | 3.3.90.38 | .01 | "máquinas de processamento de dados" com opção de compra | 1050-1053; 5157-5162 |
| Link de dados, internet, VPN, circuito dedicado | 3.3.90.40 | .12 | "acesso a banda larga, locação de circuito de dados [...], serviços de rede privativa virtual, [...] internet, IP direto" | 1082; 6111-6124 |
| Telefonia fixa ou móvel dentro de pacote de dados | 3.3.90.40 | .09 / .10 | elemento 40 só quando integrar pacote de comunicação de dados | 1082-1084; 6090-6100 |
| Telefonia fixa ou móvel fora de pacote de dados | 3.3.90.39 | (não há subelemento claro; ver conflito em 39.59) | elemento 39: "telefonia fixa e móvel, que não integrem pacote de comunicação de dados" | 1060-1062; 5605-5611 |
| Treinamento em TIC (PJ) | 3.3.90.40 | .03 | "treinamento e capacitação em TIC" | 1087-1088; 6043-6048 |
| Treinamento por instrutor pessoa física | 3.3.90.36 | .28 | "instrução e orientação profissional [...] e treinamento" | 4831-4839 |
| Inscrição em congresso/evento de TI | 3.3.90.39 | .22 | "inscrição em congressos e afins" | 5376-5383 |
| Hospedagem de site/sistema | 3.3.90.40 | .06 | "hospedagens de sistemas"; texto do subelemento cita domínio ".pe.gov.br" | 1082; 6063-6070 |
| Certificado digital A3 com token | 3.3.90.40 | .13 | "certificados digitais e-CPF e e-CNPJ (ambos Tipo A3 com fornecimento de mídia token)" | 6126-6130 |
| Digitalização de documentos | 3.3.90.40 | .14 | "digitalização de documentos físicos para o formato digital" | 1086; 6136-6139 |
| Computadores para doação/distribuição | 4.4.90.32 | .80 | "veículos, computadores e equipamentos em geral" | 8642-8646 |

---

## 4. Casos de dúvida e erros comuns

### 4.1 Regras de exclusão que o manual dá expressamente

a) **Peça de reposição não é equipamento.** 52.35 exclui "aquisição de peças destinadas à reposição diretamente ao equipamento ou mesmo para estoque, quando, então, deverá ser classificada como material de consumo" (L. 10446-10452). 30.17 confirma: "inclusive peças destinadas à reposição direta no equipamento ou mesmo para estoque" (L. 3803-3805).
b) **Basta um critério para ser consumo.** "Se um bem apresentar qualquer uma das características acima relacionadas, será considerado como material de consumo, classificado no elemento 30" (L. 10219-10220).
c) **Serviço de TIC não vai para o elemento 39.** O 39 é "exceto as relativas aos Serviços de Tecnologia da Informação e Comunicação – TIC" (L. 1057-1059). A manutenção de máquinas do 39.17 é "exceto de processamento de dados" (L. 5334-5335). A microfilmagem do 39.57 exclui TIC (L. 5599-5601).
d) **Telefonia só vai para o 40 se integrar pacote de dados.** Caso contrário, elemento 39 (L. 1060-1062 x L. 1082-1084).
e) **Material por encomenda**: serviço de terceiros só se o órgão fornecer a matéria-prima; senão, 52 ou 30 (Portaria STN 448/2002, art. 6º, L. 4646-4651).
f) **Elemento 99 e modalidade 99** não podem ser usados na execução (L. 1443-1446; L. 730-734).
g) **Itens genéricos e transitórios [PE]** (.99 "item genérico para o banco de preços", .94 SFI, .96 REFIN, .97 suprimento individual) devem ser reclassificados no subelemento específico na liquidação ou na prestação de contas (ex.: L. 4214-4219, 4283-4287, 6162-6231). São mecanismos do e-Fisco/PE. Não usar como classificação final.
h) **Obra x reparo**: ampliação ou melhoria que acrescenta patrimônio vai para o 51, "não podendo, nunca, confundir-se com os reparos e adaptações" (L. 10070-10076).

### 4.2 Pontos em que o próprio manual é ambíguo ou contraditório (não usar como regra; confirmar)

a) **Licença de software classificada como material.** O manual não traz alerta explícito sobre esse erro. O que existe: o elemento 30 não menciona software (L. 975-994) e o subelemento de licença está no elemento 40 (L. 6029-6032). Se aparecer licença em elemento 30 ou 52, tratar como inconsistência a apurar.
b) **Licença perpétua x licença como serviço.** O grupo 4 inclui "software" (L. 412), mas o único subelemento de licença é "LOCAÇÃO DE SOFTWARE (LICENÇAS)", que existe tanto em 3.3.90.40 quanto em 4.4.90.40. O manual não diz quando usar cada um.
c) **Elemento 37 x elemento 40 para serviços de TIC com postos fixos.** O 37 vale quando "o contrato especifique o quantitativo físico do pessoal" (L. 1045-1048). O 40 cobre suporte a usuários e serviços técnicos de TIC (L. 1083-1085). O manual não diz qual prevalece num service desk dimensionado por postos.
d) **Elemento 35 x 3.3.90.40.07 para consultoria em informática** (L. 1027-1031 x L. 6077-6078).
e) **Locação de equipamento de TI** aparece no 40.02 e também no 39.12 (L. 6034-6039 x L. 5289-5296). O texto do 39.12 é anterior à separação do elemento 40.
f) **Cópia e reprodução (39.83)** inclui "locação e a manutenção de equipamentos reprográficos" (L. 5780-5781) e se sobrepõe ao outsourcing de impressão (40.15, L. 6141-6146).
g) **Teclado**: consumo em 30.17 ("teclados", L. 3814) e permanente em 52.35 ("teclado para micro", L. 10458).
h) **Mídias**: "fita magnética", "CD-ROM virgem, DVD virgem" em 30.17 (L. 3812-3813) e "fitas e discos magnéticos, DVD-RW" em 52.35 (L. 10454-10455).
i) **Placas e processador** listados em 52.35 (L. 10457), embora o mesmo subelemento mande peças de reposição para o consumo (L. 10446-10452). Leitura possível: componente comprado para montar equipamento novo x peça de reposição. O manual não explica. Confirmar.
j) **Toner** aparece em 30.16 (expediente, L. 3798) e em 30.17 (processamento de dados, L. 3815).
k) **Data show** aparece em 52.33 (L. 10428) e em 52.35 (L. 10454).
l) **Aparelho telefônico** como consumo em 30.30 "(observar o custo de aquisição)" (L. 3970) e como permanente em 52.06 (L. 10246). O manual não define o valor de corte.
m) **3.3.90.39.59** tem título "ÁUDIO, VÍDEO E FOTO" e conteúdo de telefonia fixa (L. 5605-5611).
n) **3.3.93.39** ainda lista "software" e "habilitação de telefonia fixa e móvel celular" no elemento 39 (L. 7743, L. 7747-7748), em conflito com L. 1057-1059.
o) **Elemento 36, material por encomenda**: L. 4655-4657 contradiz a regra da Portaria 448 citada logo antes (L. 4646-4651).
p) **Subelementos com conteúdo estadual**: 40.06 (domínio .pe.gov.br, L. 6065), 40.11 (PE-Conectado, L. 6105), 40.12 (PE-Multidigital, L. 6114). Os códigos e textos não servem para órgão federal.
q) **4.4.90.40** não tem .11, .16 e .17, e o título omite "Pessoa Jurídica" (L. 9779-9780). Diferença de cadastro entre grupos no e-Fisco.

---

## 5. O que o agente deve sempre confirmar com a área de orçamento/contabilidade do órgão

1. **Subelemento federal**: todo subelemento citado neste guia é do e-Fisco/PE. Conferir o equivalente no plano de contas e na tabela de naturezas de despesa vigente no SIAFI e no MTO do exercício.
2. **Grupo 3 x grupo 4 para serviços de TIC** (3.3.90.40 x 4.4.90.40) e para material de consumo (3.3.90.30 x 4.4.90.30): o manual não dá critério além de L. 416-418 e L. 9887-9888.
3. **Software**: licença perpétua, cessão de direito de uso, subscrição, SaaS, suporte e atualização de versão. Confirmar elemento, grupo e se há registro como intangível. O manual não trata.
4. **Consumo x permanente**: qual norma o órgão adota (o manual usa decreto estadual de PE, L. 3619) e se há valor de corte para bens de baixo valor (o manual usa portaria estadual, L. 4194).
5. **Itens limítrofes**: teclado, mídias, placas e processadores, aparelho telefônico, data show, toner (seção 4.2).
6. **Serviço com postos de trabalho fixados** (elemento 37 x 40) e enquadramento no limite de pessoal da LRF (elemento 34, L. 1020-1025).
7. **Consultoria** (elemento 35 x 40).
8. **Telefonia**: se o contrato integra pacote de comunicação de dados (decide entre 39 e 40).
9. **Modalidade de aplicação** quando o fornecedor for órgão, entidade ou estatal integrante do orçamento (91) ou consórcio público (93/94).
10. **Bem usado** (inversão financeira, grupo 5, L. 364-365, 420-426) x bem novo (investimento).
11. **DEA**: reconhecimento da dívida e uso do elemento 92 com o subelemento do elemento original (L. 1374-1384).
12. **Garantia estendida, suporte do fabricante, cabeamento estruturado, cabos de rede**: não tratados no manual.
13. **Código CATMAT/CATSER**: o manual não trata. Buscar no catálogo do Compras.gov.br e conferir a coerência entre o código de catálogo (material ou serviço) e o elemento escolhido (30/52 para material, 36/39/40 para serviço).
14. **Vigência**: o manual foi atualizado até dezembro de 2020 (L. 261). Alterações posteriores na Portaria 163 ou nas tabelas federais não estão refletidas.
