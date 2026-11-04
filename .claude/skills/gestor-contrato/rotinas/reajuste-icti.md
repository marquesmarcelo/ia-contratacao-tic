# Rotina: reajuste por índice (ICTI) e repactuação

Fundamentos conferidos na base: Lei 14.133, arts. 25, § 7º, 92, §§ 3º e 4º, e 136, I; IN SGD/ME 94/2022, art. 24.

## Qual regra vale

- **Serviço de TI sem dedicação exclusiva de mão de obra:** reajuste em sentido estrito por índice (art. 92, § 4º, I), e o índice é o ICTI (IN 94, art. 24).
- **Serviço com dedicação exclusiva ou predominância de mão de obra:** repactuação, com demonstração analítica da variação dos custos (art. 92, § 4º, II). Não é ICTI.
- **Compra e ata de registro de preços:** o índice previsto no edital e no contrato (art. 25, § 7º; padrão do projeto: ICTI).

## Passo a passo

1. **Data-base:** a data do orçamento estimado, que é a data do Mapa de Preços (art. 92, § 3º). Interregno mínimo de 1 ano a partir dela (art. 92, § 4º). Reajustes seguintes contam 1 ano do último.
2. **Pedido:** confira se a contratada pediu, quando o contrato exigir pedido, e se pediu dentro do prazo do contrato. Pedido fora do prazo pode levar à preclusão, conforme a cláusula.
3. **Índice:** o usuário anexa a série do ICTI (IPEA) do período, com a fonte e a data de consulta. Não use número de memória.
4. **Cálculo** em Python: `fator = ICTI(mês final) / ICTI(mês da data-base)`; `novo preço unitário = preço vigente × fator`, item a item; arredondamento como o contrato mandar. Mostre a conta e grave a planilha.
5. **Efeito financeiro:** a partir de quando o novo preço vale (data do aniversário) e diferenças de meses já pagos, se houver. Lance a diferença em `controle-financeiro.md` como pagamento à parte.
6. **Empenho:** confira se o saldo cobre o novo valor; se não, alerta de reforço.
7. **Formalização:** reajuste previsto no contrato é registrado por apostila, sem termo aditivo (art. 136, I).

Saída: `contrato/reajuste/<aaaa>/calculo-reajuste.xlsx` e `Apostila-Reajuste-<aaaa>.docx` (minuta).
