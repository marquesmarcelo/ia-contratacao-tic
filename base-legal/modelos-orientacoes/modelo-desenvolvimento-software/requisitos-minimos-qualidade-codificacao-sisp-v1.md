---
titulo: "Modelo de Requisitos Mínimos de Qualidade e Padronização da Codificação do SISP v1"
tipo: modelo
url_origem: https://www.gov.br/governodigital/pt-br/contratacoes-de-tic/legislacao/modelo-de-contratacao-de-servicos-de-desenvolvimento-manutencao-e-sustentacao-de-software (arquivo enviado pelo usuário)
baixado_em: 2026-10-23
situacao: vigente
---

TEMPLATE - REQUISITOS MÍNIMOS DE QUALIDADE E PADRONIZAÇÃO DOS ASPECTOS TÉCNICOS DA CODIFICAÇÃO

**versão 1.0**

|                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Este modelo de REQUISITOS MÍNIMOS DE QUALIDADE E PADRONIZAÇÃO DOS ASPECTOS TÉCNICOS DA CODIFICAÇÃO deve ser adaptado ao ambiente de cada Instituição devendo estar anexo ao instrumento convocatório e integrar o processo de verificação da qualidade dos entregáveis derivados de contratos de serviços de desenvolvimento manutenção e sustentação de software por órgãos do Sisp. |

1\. Os requisitos mínimos de qualidade e padronização de código descritos nesse Anexo devem ser integralmente observados pela Contratada, salvo quando autorizado pela Contratante.

2\. O desenvolvimento e manutenção de softwares deverá seguir as diretrizes constantes do Roteiro de Codificação.

3\. Cada indicador de qualidade do código fonte possui meta a ser alcançada que estão relacionadas no quadro exemplificativo a seguir:

|                                                                                           |                                                                                       |                     |          |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------|----------|
| **Grupo**                                                                                 | **Indicador**                                                                         | **Unidade**         | **Meta** |
| Projeto                                                                                   | <span id="anchor"></span>Complexity / file ou equivalente                             | média total         | \<= 10   |
| Complexity / <span id="anchor-1"></span>class ou equivalente                              | média total                                                                           | \<= 10              |          |
| Complexity /function ou equivalente                                                       | média total                                                                           | \<= 5               |          |
| <span id="anchor-2"></span>Duplications ou equivalente                                    | %                                                                                     | \<= 4%              |          |
| Security <span id="anchor-3"></span>Issue Tags ou equivalente                             | unidades                                                                              | Security Hotspot=0  |          |
| Security Issue Tags ou equivalente                                                        | unidades                                                                              | Security Blocker =0 |          |
| <span id="anchor-4"></span>Technical Debt <span id="anchor-5"></span>ratio ou equivalente | %                                                                                     | \<= 2,5%            |          |
| SQALE RATING ou equivalente                                                               | Nota                                                                                  | Reliability =A      |          |
| SQALE RATING ou equivalente                                                               | Nota                                                                                  | Maintainability =A  |          |
| Violações de código (possíveis bugs, estilo de codificação, más práticas de codificação)  | <span id="anchor-6"></span>Critical Issues ou equivalente                             | unidades            | =0       |
| <span id="anchor-7"></span>Blocker Issues ou equivalente                                  | unidades                                                                              | =0                  |          |
| Indicadores relacionados a testes                                                         | Unit <span id="anchor-8"></span>Tests Coverage - camada negócio / Impl ou equivalente | %                   | \>=70%   |
| Unit Test <span id="anchor-9"></span>Success ou equivalente                               | %                                                                                     | \>=100%             |          |
| <span id="anchor-10"></span>Skipped Tests ou equivalente                                  | unidades                                                                              | =0                  |          |

4\. As metas e indicadores constantes do quadro acima poderão ser ajustados pela Contratante e adequados a cada Ordem de Serviço. Caso não seja informado novo quadro na Ordem de Serviço ou no aditivo da Ordem de Serviço, deverá ser considerado o quadro acima.

5\. O Indicador de qualidade de código (IQC) será calculado dividindo a Quantidade de requisitos de qualidade de código atendidos (ΣQrc) pela Quantidade total de requisitos de qualidade de código avaliados (ΣQtr):

**IQC = 100 \* (ΣQrc / ΣQtr)**

> Onde:

> IQC = Indicador de qualidade de código;

> **Σ**Qrc = Somatório da Quantidade de requisitos de qualidade de código atendidos;

> **Σ**Qtr = Somatório da Quantidade total de requisitos de qualidade de código avaliados.

6\. Caso algum indicador seja depreciado ou removido em futura versão da ferramenta de análise de código que venha a ser adotada pela Contratante e não seja substituído por indicador equivalente nesta mesma ferramenta, ele deixará de ser considerado para fins de aferição do IQC e substituído por um equivalente presente na nova versão ou ferramenta.

7\. Problemas de qualidade no código-fonte do software pré-existentes à abertura da OS serão desconsiderados também na aferição do indicador IQC.

8\. Havendo impossibilidade do uso da ferramenta deve-se promover a verificação manual por meio de aplicação de técnicas de amostragem conforme Roteiro de Amostragem.
