---
titulo: "Planilha simplificada - Portaria SGD/MGI 1.070"
tipo: modelo
url_origem: https://www.gov.br/governodigital/pt-br/contratacoes-de-tic/legislacao/modelo-de-contracao-de-servicos-de-operacao-de-infraestrutura-e-de-atendimento-a-usuarios-de-tic (arquivo enviado pelo usuário)
baixado_em: 2026-10-23
situacao: vigente
---

# /tmp/claude-0/anexos-conv/5b8cf0e6-planilha-simplificada-mgi-1070-2024.xlsx

Células com `<fórmula: ...>` são calculadas: não sobrescrever. Demais células numéricas ou vazias ao lado de rótulos são de entrada.

## Aba: Estimativa_-_ITEM_<Nº>

- A1="ATENÇÃO:" | B1="A estimativa prevista nesta aba refere-se a uma única categoria de serviço. Havendo N categorias de serviço a serem contratada, devem ser replicadas N abas iguais a esta, realizando as etapas abaixo para cada uma delas. Ao final, deve-se fazer o somatório de todas as abas para encontrar o valor total estimado da contratação."
- A4="Orientações:" | B4="1. Inserir o nº do item da licitação na célula A12"
- B5="2. Selecionar uma categoria de serviço na célula B13"
- B6="3. Selecionar um perfil nas células B15 a B24 acrescentando mais linhas, se necessário"
- B7="4. Inserir o quantitativo de profissionais de cada perfil selecionado"
- B8="5. Inserir outros itens de custos, se houve, nas células B30 e B31, acrescentando mais linhas se necessário"
- B9="6. Inserir o custo mensal de cada item posto na forma acima"
- A11="Planilha Simplificada para Estimativa do Valor Mensal do Serviço"
- A12="ITEM <Nº>" | B12="Categoria de Serviço"
- B13="Perfil" | C13="Salário de referência (A)" | D13="Fator-K" | E13="Quantidade (B)" | F13="Custo unitário mensal do Perfil (C)" | G13="Custo total mensal por Perfil (D = C x B)"
- A14=1 | C14=<fórmula: =IFERROR((VLOOKUP(B14,Perfis!$C$2:$D$36,2,FALSE())),"")> | D14=<fórmula: =IFERROR((VLOOKUP(B14,Perfis!$C$2:$E$36,3,FALSE())),"")> | F14=<fórmula: =IFERROR((C14*D14),"")> | G14=<fórmula: =IFERROR((F14*E14),"")>
- A15=2 | C15=<fórmula: =IFERROR((VLOOKUP(B15,Perfis!$C$2:$D$36,2,FALSE())),"")> | D15=<fórmula: =IFERROR((VLOOKUP(B15,Perfis!$C$2:$E$36,3,FALSE())),"")> | F15=<fórmula: =IFERROR((C15*D15),"")> | G15=<fórmula: =IFERROR((F15*E15),"")>
- A16=3 | C16=<fórmula: =IFERROR((VLOOKUP(B16,Perfis!$C$2:$D$36,2,FALSE())),"")> | D16=<fórmula: =IFERROR((VLOOKUP(B16,Perfis!$C$2:$E$36,3,FALSE())),"")> | F16=<fórmula: =IFERROR((C16*D16),"")> | G16=<fórmula: =IFERROR((F16*E16),"")>
- A17=4 | C17=<fórmula: =IFERROR((VLOOKUP(B17,Perfis!$C$2:$D$36,2,FALSE())),"")> | D17=<fórmula: =IFERROR((VLOOKUP(B17,Perfis!$C$2:$E$36,3,FALSE())),"")> | F17=<fórmula: =IFERROR((C17*D17),"")> | G17=<fórmula: =IFERROR((F17*E17),"")>
- A18=5 | C18=<fórmula: =IFERROR((VLOOKUP(B18,Perfis!$C$2:$D$36,2,FALSE())),"")> | D18=<fórmula: =IFERROR((VLOOKUP(B18,Perfis!$C$2:$E$36,3,FALSE())),"")> | F18=<fórmula: =IFERROR((C18*D18),"")> | G18=<fórmula: =IFERROR((F18*E18),"")>
- A19=6 | C19=<fórmula: =IFERROR((VLOOKUP(B19,Perfis!$C$2:$D$36,2,FALSE())),"")> | D19=<fórmula: =IFERROR((VLOOKUP(B19,Perfis!$C$2:$E$36,3,FALSE())),"")> | F19=<fórmula: =IFERROR((C19*D19),"")> | G19=<fórmula: =IFERROR((F19*E19),"")>
- A20=7 | C20=<fórmula: =IFERROR((VLOOKUP(B20,Perfis!$C$2:$D$36,2,FALSE())),"")> | D20=<fórmula: =IFERROR((VLOOKUP(B20,Perfis!$C$2:$E$36,3,FALSE())),"")> | F20=<fórmula: =IFERROR((C20*D20),"")> | G20=<fórmula: =IFERROR((F20*E20),"")>
- A21=8 | C21=<fórmula: =IFERROR((VLOOKUP(B21,Perfis!$C$2:$D$36,2,FALSE())),"")> | D21=<fórmula: =IFERROR((VLOOKUP(B21,Perfis!$C$2:$E$36,3,FALSE())),"")> | F21=<fórmula: =IFERROR((C21*D21),"")> | G21=<fórmula: =IFERROR((F21*E21),"")>
- A22=9 | C22=<fórmula: =IFERROR((VLOOKUP(B22,Perfis!$C$2:$D$36,2,FALSE())),"")> | D22=<fórmula: =IFERROR((VLOOKUP(B22,Perfis!$C$2:$E$36,3,FALSE())),"")> | F22=<fórmula: =IFERROR((C22*D22),"")> | G22=<fórmula: =IFERROR((F22*E22),"")>
- A23=10 | C23=<fórmula: =IFERROR((VLOOKUP(B23,Perfis!$C$2:$D$36,2,FALSE())),"")> | D23=<fórmula: =IFERROR((VLOOKUP(B23,Perfis!$C$2:$E$36,3,FALSE())),"")> | F23=<fórmula: =IFERROR((C23*D23),"")> | G23=<fórmula: =IFERROR((F23*E23),"")>
- C24="Quantitativo Total Equipe" | E24=<fórmula: =SUM(E14:E23)> | F24="Custo Total mensal (F)" | G24=<fórmula: =IFERROR(SUM(G14:G23),"")>
- A27="Outros itens de custo"
- A28="ITEM" | B28="Descrição" | C28="Custo mensal (E)"
- A29=1
- A30=2
- B31="Custo mensal Total Outros Itens (G)" | C31=<fórmula: =IFERROR(SUM(C29:C30),"")>
- B33=<fórmula: =CONCATENATE("Valor Mensal de Referência do ",$A$12)>

## Aba: Perfis

- A1="CBO de Referência" | B1="Cód. Identificação do Perfil" | C1="Descrição do Perfil" | D1="Valor Salarial (R$)" | E1="Fator-K"
- A2="3172-10" | B2="TECSUP-01" | C2="Técnico de suporte ao usuário de tecnologia da informação Júnior" | D2=1714.27333333333 | E2=2.49
- A3="3172-10" | B3="TECSUP-02" | C3="Técnico de suporte ao usuário de tecnologia da informação Pleno" | D3=2312.19135135135 | E3=2
- A4="3172-10" | B4="TECSUP-03" | C4="Técnico de suporte ao usuário de tecnologia da informação Sênior" | D4=3216.87222222222 | E4=2
- A5="3132-20" | B5="TECMAN-01" | C5="Técnico em manutenção de equipamentos de informática Júnior" | D5=1600.32 | E5=2.49
- A6="3132-20" | B6="TECMAN-02" | C6="Técnico em manutenção de equipamentos de informática Pleno" | D6=2505.11636363636 | E6=2
- A7="3132-20" | B7="TECMAN-03" | C7="Técnico em manutenção de equipamentos de informática Sênior" | D7=3273.70785714286 | E7=2
- A8="1425-30" | B8="GERSUP" | C8="Gerente de suporte técnico de tecnologia da informação" | D8=8877.20430555556 | E8=2
- A9="2124-20" | B9="ASUPCOMP-01" | C9="Analista de suporte computacional Júnior" | D9=3067.14089783282 | E9=2.49
- A10="2124-20" | B10="ASUPCOMP-02" | C10="Analista de suporte computacional Pleno" | D10=5038.22879324619 | E10=2
- A11="2124-20" | B11="ASUPCOMP-03" | C11="Analista de suporte computacional Sênior" | D11=6491.70101307189 | E11=2
- A12="1425-5, 1425-15" | B12="GERINF" | C12="Gerente de infraestrutura de tecnologia da informação" | D12=16535.6115384615 | E12=2
- A13="2123-5" | B13="ABD-01" | C13="Administrador de banco de dados - Júnior" | D13=4553.905 | E13=2.49
- A14="2123-5" | B14="ABD-02" | C14="Administrador de banco de dados - Pleno" | D14=6371.26913636364 | E14=2
- A15="2123-5" | B15="ABD-03" | C15="Administrador de banco de dados - Sênior" | D15=10248.050475 | E15=2
- A16="2123-15" | B16="ASO-01" | C16="Administrador de sistemas operacionais Júnior" | D16=4409.69076923077 | E16=2.49
- A17="2123-15" | B17="ASO-02" | C17="Administrador de sistemas operacionais Pleno" | D17=6326.63874358974 | E17=2
- A18="2123-15" | B18="ASO-03" | C18="Administrador de sistemas operacionais Sênior" | D18=8955.40917307693 | E18=2
- A19="2124-10, 2123-10" | B19="ARED-01" | C19="Analista de redes e de comunicação de dados Júnior" | D19=4315.95965811966 | E19=2.49
- A20="2124-10, 2123-10" | B20="ARED-02" | C20="Analista de redes e de comunicação de dados Pleno" | D20=6680.21285547786 | E20=2
- A21="2124-10, 2123-10" | B21="ARED-03" | C21="Analista de redes e de comunicação de dados Sênior" | D21=9470.31895536562 | E21=2
- A22="3133-05, 3133-10" | B22="TECRED-01" | C22="Técnico de Rede (Telecomunicações) Júnior" | D22=1557.80333333333 | E22=2.49
- A23="3133-05, 3133-10" | B23="TECRED-02" | C23="Técnico de Rede (Telecomunicações) Pleno" | D23=2517.456 | E23=2
- A24="3133-05, 3133-10" | B24="TECRED-03" | C24="Técnico de Rede (Telecomunicações) Sênior" | D24=3366.245 | E24=2
- A25="3171-10, 2124-30, 2124-05" | B25="DESTEC-01" | C25="Desenvolvedor de sistemas de tecnologia da informação Júnior" | D25=5343.12066176471 | E25=2.49
- A26="3171-10, 2124-30, 2124-05" | B26="DESTEC-02" | C26="Desenvolvedor de sistemas de tecnologia da informação Pleno" | D26=8829.9343627451 | E26=2
- A27="3171-10, 2124-30, 2124-05" | B27="DESTEC-03" | C27="Desenvolvedor de sistemas de tecnologia da informação Sênior" | D27=11904.2479343682 | E27=2
- A28="2124-15, 2124-25" | B28="ASISA-01" | C28="Analista de sistemas de automação - Júnior" | D28=5036.23076923077 | E28=2.49
- A29="2124-15, 2124-25" | B29="ASISA-02" | C29="Analista de sistemas de automação - Pleno" | D29=7281.70741538462 | E29=2
- A30="2124-15, 2124-25" | B30="ASISA-03" | C30="Analista de sistemas de automação - Sênior" | D30=9558.33531468532 | E30=2
- A31="2123-20" | B31="ASEG-01" | C31="Administrador em segurança da informação - Júnior" | D31=5652.78090909091 | E31=2.49
- A32="2123-20" | B32="ASEG-02" | C32="Administrador em segurança da informação - Pleno" | D32=7933.55610576923 | E32=2
- A33="2123-20" | B33="ASEG-03" | C33="Administrador em segurança da informação - Sênior" | D33=11621.3827538462 | E33=2
- A34="1425-25" | B34="GERSEG" | C34="Gerente de segurança da informação" | D34=20264.9251111111 | E34=2
- A35="2122-15" | B35="CLOUD-01" | C35="Especialista em Cloud - Pleno" | D35=10554.8338757396 | E35=2
- A36="2122-15" | B36="CLOUD-02" | C36="Especialista em Cloud - Sênior" | D36=15608.8814102564 | E36=2

## Aba: Serviços

- A1="Serviços"
- A2="Gerenciamento de Serviços de TIC"
- A3="Sustentação de Aplicações"
- A4="Armazenamento e Backup"
- A5="Sustentação de Banco de Dados"
- A6="Administração de Dados"
- A7="Conectividade e Comunicação"
- A8="Segurança de TIC"
- A9="Monitoramento de Serviços de TI"
- A10="Suporte Técnico de Microinformática"

