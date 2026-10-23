---
titulo: "Planilha modelo de compensação de franquia - Outsourcing de Impressão"
tipo: modelo
url_origem: https://www.gov.br/governodigital/pt-br/contratacoes-de-tic/legislacao/modelo-de-contratacao-de-servicos-de-outsourcing-de-impressao (arquivo enviado pelo usuário)
baixado_em: 2026-10-23
situacao: vigente
---

# /mnt/user-data/attachments/2a8a48aa-b29e-58de-840e-06cb105913ae/ec6249f4-anexoorientacoesoutsourcingdeimpressao_planilhamodelo_com.xlsx

Células com `<fórmula: ...>` são calculadas: não sobrescrever. Demais células numéricas ou vazias ao lado de rótulos são de entrada.

## Aba: Modelo compensação franquia

- A1="PLANILHA MODELO PARA COMPENSAÇÃO DE FRANQUIA DE OUTSOURCING DE IMPRESSÃO - Compensação Semestral"
- A2="*Campos a serem preenchidos estão na cor branca" | H2="INSTRUÇÕES:"
- A3="Quantidade Mensal de páginas contratadas na franquia mensal" | D3=6000 | H3="1 - Insira a quantidade mensal de páginas contratadas (Campo D3)"
- A4="Valor fixo da Franquia Mensal" | D4=600 | H4="2 - Insira o valor fixo da franquia mensal contratado (Campo D4)"
- A5="Valor da página impressa Excedente à Franquia Mensal" | D5=0.07 | H5="3 - Insira o valor a ser pago por página excedente contratado (Campo D5)"
- B6="Franquia Mensal" | C6="Produzido" | D6="Valor Franquia" | E6="Valor Excedente" | F6="Valor mensal" | H6="4 - Preencha a coluna de quantidade de páginas produzidas em cada mês (Coluna C)"
- A7="Mês 1" | B7=<fórmula: =$D$3> | C7=6412 | D7=<fórmula: =$D$4> | E7=<fórmula: =IF(C7-B7<0,0,(C7-B7)*$D$5)> | F7=<fórmula: =E7+D7> | H7="5 - O valor a ser pago mensalmente estará na coluna "Valor Mensal""
- A8="Mês 2" | B8=<fórmula: =$D$3> | C8=5412 | D8=<fórmula: =$D$4> | E8=<fórmula: =IF(C8-B8<0,0,(C8-B8)*$D$5)> | F8=<fórmula: =E8+D8> | H8="6 - No último mês do período de compensação (Mês 6) o valor a ser pago será o resultado apresentado no campo "Novo Valor Pago". Se esse valor estiver negativo, o órgão deverá gerar uma Guia de Recolhimento da União (GRU) a ser recolhida pela empresa contratada."
- A9="Mês 3" | B9=<fórmula: =$D$3> | C9=6104 | D9=<fórmula: =$D$4> | E9=<fórmula: =IF(C9-B9<0,0,(C9-B9)*$D$5)> | F9=<fórmula: =E9+D9>
- A10="Mês 4" | B10=<fórmula: =$D$3> | C10=4953 | D10=<fórmula: =$D$4> | E10=<fórmula: =IF(C10-B10<0,0,(C10-B10)*$D$5)> | F10=<fórmula: =E10+D10>
- A11="Mês 5" | B11=<fórmula: =$D$3> | C11=9524 | D11=<fórmula: =$D$4> | E11=<fórmula: =IF(C11-B11<0,0,(C11-B11)*$D$5)> | F11=<fórmula: =E11+D11> | G11="Redução" | H11="Novo Valor Pago"
- A12="Mês 6" | B12=<fórmula: =$D$3> | C12=9863 | D12=<fórmula: =$D$4> | E12=<fórmula: =IF(C12-B12<0,0,(C12-B12)*$D$5)> | F12=<fórmula: =E12+D12> | G12=<fórmula: =IF(C13>B13,E13-C15,E13)> | H12=<fórmula: =F12-G12>
- A13="Total" | B13=<fórmula: =SUM(B7:B12)> | C13=<fórmula: =SUM(C7:C12)> | D13=<fórmula: =SUM(D7:D12)> | E13=<fórmula: =SUM(E7:E12)> | F13="TOTAL A SER PAGO" | H13=<fórmula: =SUM(F7:F11)+H12>
- A14="Delta Excedente (∆ Exc = ∑ P - ∑ F)" | C14=<fórmula: =C13-B13>
- C15=<fórmula: =IF(C14<0,0,C14*$D$5)>
- B17="∑ F" | C17="Somatório das Franquias Mensais (em páginas)" | F17="*Franqua Mensal = somas das franquias dos tipos de equipamentos, separando-se monocromáticas e policromáticas"
- B18="∑ P" | C18="Somatório das páginas produzidas no semestre (em páginas)"
- B19="∑ VE" | C19="Somatório Valor Excedente (R$)"
- B20="∆ Exc" | C20="Delta Excedente (páginas)" | E20="∆ Exc = ∑ P - ∑ F   (diferença entre o somatório produzido e o somatório das franquias mensais no semestre)"
- B21="Valor ∆ Exc" | C21="Valor Delta Excedente (R$)" | E21="Valor ∆ Exc = ∆ Exc * Valor Unitário Excedente"
- B22="Redução" | C22="Valor da Redução (R$)" | E22="Valor da Redução = ∑ VE - Valor Delta Excedente"
- B23="Novo Valor Pago" | C23="(R$)" | E23="Novo Valor Pago = Valor mensal do último mês da apuração semestral - Valor da Redução"

