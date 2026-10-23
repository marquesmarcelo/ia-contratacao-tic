# Modelos de contratação da SGD: quando aplicar

> **Regra do projeto (definida pelo usuário):** sempre que o objeto do TR for compatível com um modelo abaixo, o modelo é aplicado: requisitos, níveis de serviço, métricas, forma de pagamento, preços referenciais e anexos do modelo entram no ETP e no TR. Desvio do modelo só com justificativa técnica registrada no ETP.
> Fundamento: IN 94, art. 8º, § 2º (observar guias, manuais e modelos do Órgão Central do SISP); art. 20, § 4º (estimativas de preço dos modelos podem ser usadas como preço estimado); art. 42, parágrafo único (norma específica do SISP afasta a aplicação subsidiária do SISG).
> Pastas relativas a `base-legal/modelos-orientacoes/`. Planilhas e documentos originais (.xlsx, .xlsm, .ods, .odt, .pdf) ficam em `<pasta>/arquivos/`; use-os quando o TCO ou o TR precisar preencher a planilha do modelo. Verifique a vigência no cabeçalho de cada arquivo antes de usar.

| Objeto (gatilho) | Modelo / orientação | Ato | Onde está na base | Faltando na base |
|---|---|---|---|---|
| Licenças de software, subscrição, serviços em nuvem (IaaS, PaaS, SaaS), migração para nuvem, nuvem de governo | Modelo de Contratação de Software e Serviços de Computação em Nuvem | Portaria SGD/MGI 5.950/2023 | `modelo-software-nuvem/` | template de estratégia (.docx), página Nuvem de Governo, catálogos por provedor |
| Notebooks, desktops, estações, PCaaS, VDI/virtualização de desktop | Modelo de Contratação e Gestão de Estações de Trabalho | Portaria SGD/MGI 2.715/2023 | `modelo-estacoes-trabalho/` (portaria com Anexos I a III, RAIR) | template de estratégia de infraestrutura computacional, orientações Windows 10 |
| Desenvolvimento, manutenção e sustentação de software; fábrica de software | Modelo de Desenvolvimento, Manutenção e Sustentação de Software | Portaria SGD/MGI 750/2023 (alt. 6.679/2024, 6.040/2025, 4.777/2026) | `modelo-desenvolvimento-software/` | subpáginas de ferramentas auxiliares e documentos relacionados |
| Medição de software (pontos de função, UST de software) | Roteiro de Métricas de Software do SISP 3.0 | Portaria SGD/MGI 3.656/2026 | `roteiro-metricas-software-sisp/` | — |
| Impressão, digitalização, outsourcing de impressão | Modelo de Outsourcing de Impressão | Portaria SGD/MGI 370/2023 | `modelo-outsourcing-impressao/` | — |
| Service desk, atendimento a usuários, operação de infraestrutura, NOC, sustentação de ambiente | Modelo de Operação de Infraestrutura e Atendimento a Usuários de TIC | Portaria SGD/MGI 1.070/2023 (alt. 6.680/2024, 6.055/2025, 5.921/2026) | `modelo-operacao-infraestrutura-atendimento/` | — |
| Contratação de empresa pública de TIC (Serpro, Dataprev etc.) | Modelo de Composição de Preços com Empresas Públicas | — (IN 94, Anexo I, item 5) | `modelo-composicao-precos-empresas-publicas/` | — |
| Links de dados, internet, comunicação de dados | Orientações para Serviços de Comunicação de Dados | Lei 14.744/2023; Decreto 12.124/2024 | `servicos-comunicacao-dados/`; `normas/leis/lei-14744-2023.md` | — |
| Qualquer contrato medido em UST (nova contratação ou renovação) | Orientações para contratos baseados em UST | — | `contratos-ust/` | Acórdãos TCU 2.037/2019 e 1.508/2020 |
| Toda pesquisa de preços | Orientações para análise crítica na pesquisa de preços (IPPC-TIC, Nota Técnica AudTI/TCU 8/2023) | IN SEGES/ME 65/2021 | `analise-critica-pesquisa-precos/` | Caderno de Pesquisa de Preços 2023 |
| Todos os objetos | Templates de artefatos e lista de verificação TIC (AGU) | IN 94 | `templates-artefatos-sgd/`, `todos-os-modelos-diretrizes-orientacoes/` | — |

## Como aplicar

1. Na triagem, o Coordenador marca o(s) modelo(s) aplicável(is) e registra no `registro-historico.md`. Objeto que se encaixa em mais de um modelo segue cada um na parcela correspondente.
2. O Técnico lê a portaria e os anexos do modelo **antes** de escrever ETP, TCO e TR, e cita no ETP o modelo adotado.
3. O que o modelo define (catálogo de serviços, métricas, níveis mínimos de serviço, fórmulas de glosa, preços referenciais, mapa salarial) entra no TR sem alteração; o que for alterado tem justificativa no ETP.
4. Se o documento do modelo estiver na coluna "Faltando na base", o Coordenador avisa o usuário antes de escrever a parte que depende dele e pede o arquivo (lista com links em `base-legal/PENDENCIAS-DOWNLOAD.md`).
5. O auditor confere a aderência ao modelo e trata desvio sem justificativa como achado relevante, ou impeditivo quando o modelo for de uso obrigatório para o órgão.
