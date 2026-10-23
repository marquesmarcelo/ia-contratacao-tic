---
titulo: "Modelo de Roteiro de Codificação do SISP v1"
tipo: modelo
url_origem: https://www.gov.br/governodigital/pt-br/contratacoes-de-tic/legislacao/modelo-de-contratacao-de-servicos-de-desenvolvimento-manutencao-e-sustentacao-de-software (arquivo enviado pelo usuário)
baixado_em: 2026-10-23
situacao: vigente
---

**TEMPLATE - ROTEIRO DE CODIFICAÇÃO – versão 1.0**

|                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Este modelo de roteiro de codificação deve ser adaptado ao ambiente de cada Instituição devendo estar anexo ao Termo de Referência e integrar o processo de verificação da qualidade dos entregáveis derivados de contratos desserviços de desenvolvimento manutenção e sustentação de software por órgãos do Sisp. |

**1. INTRODUÇÃO**

1.1 O presente Roteiro dispõe sobre as melhores práticas de codificação com vistas a assegurar uma codificação enxuta, limpa, clara e eficiente, observando as diretrizes de codificação segura publicadas pela Secretaria de Governo Digital.

**2. DIRETRIZES GERAIS **

2.1 Além das diretrizes constantes deste Roteiro, deve-se adotar no que couber as orientações constantes dos:

> a\. Guia de Requisitos e Obrigações quanto a Privacidade e à Segurança da Informação, disponível em:  
> https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi/guia_requisitos_obrigacoes.pdf  
>   
> b. Guia de Requisitos Mínimos de Privacidade e Segurança da Informação para Aplicações Web, disponível em:  
> https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi/guia_requisitos_minimos_web.pdf  
>   
> c. Guia de Requisitos Mínimos de Privacidade e Segurança da Informação para APIs, disponível em:  
> https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi/guia_requisitos_minimos_apis.pdf  
>   
> d. Guia de Requisitos Mínimos de Privacidade e Segurança da Informação para Aplicativos Móveis, disponível em:  
> https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi/guia_requisitos_minimos_apps.pdf

**3. ESCRITA DE CÓDIGO**

**3.1 Nomes Significativos**

3.1.1 Os nomes utilizados para variáveis, funções, classes e métodos devem ser autoexplicativos, ou seja deve responder as seguintes perguntas: "Por que ele existe?", "o que ele faz?" e "como é usado?".

3.1.2 Não se deve incluir no código informações inverídicas ou falas para mascarar o código ou dificultar sua manutenção.

3.1.3 Os nomes devem ser pronunciáveis e ter significado adequado ao contexto em língua portuguesa.

3.1.4 Evite codificações ou encriptações em nomes de variáveis, classes, funções e métodos.

3.1.5 Os nomes devem ser de fácil entendimento associado ao contexto do domínio do negócio.

**3.2 Funções e Classes**

3.2.1 As funções e classes devem ter o mínimo de linhas possível, mantendo-se a clareza e implementando o código necessário para traduzir o objetivo esperado da função ou da classe.

3.2.2 As funções e classes devem ter objetivos específicos possuindo um nível de abstração (deve ter apenas uma responsabilidade ou objetivo, ou seja, deve fazer coisa).

3.2.3 A escrita do código deve seguir uma narrativa top-<span id="anchor"></span>down.

3.2.4 As funções e classes não devem possuir efeitos escondidos ou colaterais, ou seja, não devem produzir efeitos distintos daqueles que se propõe a realizar.

3.2.5 Deve-se evitar níveis de herança exagerados, superior a 4 (quatro).

**3.3 Comentários**

3.3.1 O código útil deve ser autoexplicativo, limpo e eficiente, devendo possuir apenas os mínimos de comentário possível.

3.3.2 Evite comentários redundantes ou óbvios, que descrevem o que o código faz sem acrescentar nenhuma informação útil.

**3.4 Estruturas**

3.4.1 Não se deve criar estruturas de código redundantes ou sem efetiva geração de valor à finalidade pretendida.

3.4.2 Não se deve replicar linhas de códigos ou estruturas tornando-as redundantes.

3.4.3 Deve-se evitar duplicar ou replicar funções ou classes que possuam a mesma responsabilidade ou objetivo.

**3.5 Identação**

3.5.1 Deve-se adotar a identação adequada para melhor entendimento e clareza do código, evitando-se identações exageradas ou nenhuma identação.

**3.6 Complexidade ciclomática**

3.6.1. Deve-se adotar a menor complexidade ciclomática possível por algoritmo.

3.6.2 Deve-se evitar o aninhamento excessivo de instruções de condições (If's dentro de If''s).

3.6.3 Deve-se evitar o exagero de condições ("Case") dentro de instruções de escolha ("switch")

3.6.4 Deve-se remover construções desnecessárias, ou seja, aquelas que podem ser removidas sem alterar a semântica e a finalidade do código.

3.6.5 A complexidade ciclomática do código deve ser igual ou inferior a 10, salvo se aprovado pela contratante.

**4. DIRETRIZES DE SEGURANÇA DA INFORMAÇÃO**

**4.1 Armazenamento de dados**

4.1.1 Nos casos de armazenamento de dados abertos (Dados públicos), não se deve utilizar meio de armazenamento que não possua acesso para escrita restrito por senha.

4.1.2 Nos casos de armazenamento de dados fechados (Dados cujo acesso é restrito a um grupo específico de pessoas), não se deve utilizar meio de armazenamento que não possua acesso para leitura e escrita restrito por senha.

4.1.3 Não se deve disponibilizar à aplicações acesso à algum banco de dados utilizando login de usuário com permissões de root.

4.1.4 Não se deve utilizar o armazenamento de senhas em código-fonte.

4.1.5 Não se deve utilizar as mesmas senhas para ambientes de desenvolvimento ou homologação e produção

4.1.6 Deve-se armazenar de forma segura os dados de usuários e os sistemas que utilizam cada senha fornecida.

**4.2 Gerenciamento de Acessos e Permissões de Usuários**

4.2.1 Não se deve armazenar senhas em texto plano sem utilizar um algoritmo de <span id="anchor-1"></span>hash seguro e salt.

4.2.2 Deve-se utilizar controle de usuário e senha nominais para determinar a identidade do usuário.

4.2.3 Deve-se utilizar HTTPS para controle de autenticação ao menos nas telas de login do sistema web.

**4.3 Comunicação **

4.3.1 Deve-se empregar canal de comunicação com controle de duplicação e perda de informações/mensagens.

4.3.2 Deve-se empregar canal de comunicação com controle de autenticação (<span id="anchor-2"></span>eg, HTTPS, certificados digitais gerados por autoridades confiáveis, VPNs).

4.3.3 Deve-se empregar canal de comunicação que provenha confidencialidade dos dados transmitidos (eg, HTTPS, VPNs).

4.4 Medidas contra-ataques

4.4.1 Deve-se prevenir ataques de injeção de SQL (SQL <span id="anchor-3"></span>Injection), a exemplo das seguintes medidas mínimas:

> a\) Não se deve criar <span id="anchor-4"></span>SQLs concatenando parâmetros textuais de origem não-segura, como parâmetros preenchidos pelo usuário ou mesmo armazenados no banco de dados.

> b\) Deve-se restringir permissões de acesso ao banco de dados para o usuário da aplicação.

> c\) Deve-se, sempre que possível, passar parâmetros em comandos SQL (DML ou DDL) utilizando <span id="anchor-5"></span>prepared statements.

> d\) Consultas que não podem ser parametrizadas deverão receber tratamento especial, como escapes ou codificação em hexadecimal.

4.4.2 Deve-se prevenir ataques de injeção de HTML e Javascript.

4.4.3 Deve-se prevenir ataques do tipo <span id="anchor-6"></span>cross-site scripting (XSS).

4.4.4 Deve-se prevenir ataques de quebra de autenticação e gerenciamento de sessão (Broken <span id="anchor-7"></span>Authentication and <span id="anchor-8"></span>Session Management).

**4.5 Auditoria, rastreamento e Logs**

4.5.1 Permitir que eventos sejam registrados a exemplo de:

> a\) operações de login e logout;

> b\) acessos a determinadas telas ou seções do sistema;

> c\) acesso a informações com alguma restrição (eg, documentos sigilosos, processos em segredo de justiça, dados pessoais ou bancários);

> d\) operações de inclusão, alteração ou exclusão de registros no banco de dados;

> e\) alteração de perfil de acesso (para sistemas que possuem acesso com diferentes perfis); e -

> f\) execução de <span id="anchor-9"></span>jobs e tarefas automatizadas.

4.5.2 Permitir que informações sejam auditáveis para cada tipo de evento selecionado para monitoramento:

1)  data e hora;

2)  usuário que efetuou a operação;

3)  endereço IP;

4)  identificador da sessão do usuário (quando aplicável, eg, cookie);

5)  tela (página) do sistema de onde a operação foi realizada;

6)  identificador da instância (para sistemas <span id="anchor-10"></span>clusterizados);

7)  para operações de inserção, alteração ou exclusão, o tipo da operação, nome da tabela que foi manipulada, ID do registro e, se for o caso, valores anterior e atual de cada campo;

8)  parâmetros informados pelo usuário (eg, parâmetros GET ou POST), tomando cuidado de não armazenar dados sensíveis, como senhas;

9)  tempo de resposta do sistema;

10) para execução de jobs e tarefas automatizadas, armazenar o resultado da operação; falha, sucesso, cancelada, etc.

4.5.3 Permitir formas de <span id="anchor-11"></span>captura dos dados para auditoria, a exemplo:

1)  alterações aplicadas no banco de dados podem ser auditadas via triggers;

2)  auditar as alterações a partir da própria aplicação, sendo que algumas informações poderão não ser registradas (eg, operações SQL realizadas por fora da aplicação).

3)  Em sistemas web desenvolvidos em Java, um Filtro pode interceptar as requisições feitas à aplicação.

4.5.4 Deve-se definir no documento de especificação de requisitos do sistema quais informações deverão ser registradas e o local de armazenamento dos dados da auditoria.

**4.6 Cópias de Segurança (Backups)**

4.6.1 Deve-se incluir no plano de projeto a especificação da necessidade e a atribuição da responsabilidade de realização de backups do banco de dados e dos códigos-fonte do sistema, bem como as políticas de acesso a este backup.

4.6.2 Deve-se definir um procedimento estruturado para a restauração de backups.

4.6.3 Deve-se definir e capacitar responsáveis pela recuperação dos backups.

**4.7 Testes**

4.7.1 Deve-se realizar testes manuais de segurança antes de cada versão do software que modifique sua estrutura (telas de login, serviços não autenticados, novos formulários com interação com o usuário, etc.).

4.7.2 Deve-se garantir, através de testes automatizados, que os serviços e dados sigilosos estão protegidos e disponíveis apenas para os usuários detentores das informações.

4.7.3 Deve-se elaborar uma política de testes, automatizados ou não, visando a garantia de não vulnerabilidade aos principais ataques conhecidos em sistemas.

4.7.4 Deve-se definir cenários de testes voltados à garantia dos requisitos não funcionais do software, preferencialmente realizado por uma equipe de testes diferente da equipe de desenvolvimento do software, com intuito de se evitar vícios.

4.7.5 Deve-se definir cenários de testes, principalmente nos aspectos de segurança, para os casos de atualizações na arquitetura do sistema (servidores de aplicação, banco de dados, versões de browser, versões de sistema operacional, etc.).

**4.8 Medidas contra falhas de segurança**

4.8.1 Deve-se manter procedimento planejado para imediata indisponibilização do sistema e realização de manutenção corretiva.

4.8.2 Deve-se definir uma política de acompanhamento pós-correção de ocorrências de falha de segurança.

**4.9 Diretrizes para a instalação, configuração e gerenciamento de ambientes de desenvolvimento de sistemas**

4.9.1 Deve-se utilizar um controle de versão distribuído, que mantém um repositório completo em cada máquina de desenvolvimento, Eg, Git , Mercurial .

4.9.2 Deve-se utilizar bancos de dados distintos para cada ambiente (Desenvolvimento, produção).

4.9.3 Deve-se utilizar servidores de aplicação/web distintos para cada ambiente (Desenvolvimento, produção).

4.9.4 Deve-se prover acesso ao ambiente de desenvolvimento/testes/homologação apenas aos integrantes da equipe de desenvolvimento e aos interessados no projeto (stakeholders).

4.9.5 Deve-se realizar testes periódicos para assegurar a segurança do ambiente de desenvolvimento/testes/homologação.

**4.10 Diretrizes para a configuração de proteção a dados sensíveis**

4.10.1 Deve-se utilizar um método criptográfico que siga o princípio de <span id="anchor-12"></span>Kerckhoffs; o método de encriptação e seus parâmetros devem ser públicos e estar documentados, somente a chave criptográfica deve ser mantida em sigilo.

4.10.2 Não se deve utilizar um cifrador que admita um método conhecido para quebra da chave criptográfica melhor do que a força bruta, baseada em tentativa e erro.

4.10.3 Não se deve utilizar o modo de cifrador de bloco <span id="anchor-13"></span>electronic codebook (ECB) ou modos menos seguros.

4.10.4 Não se deve utilizar um tamanho da chave menor que 128 bits (cifrador simétrico) ou 1024 bits (cifrador assimétrico).

4.10.5 Não se deve utilizar função de hash sem algum tipo de salt.

4.10.6 Não se deve utilizar algoritmos considerados obsoletos para criptografia e hash criptográfico. Exemplos: MD5, SHA1, DES/3DES, RC2, RC4, MD4.

4.10.7 Não se deve utilizar um tamanho da chave menor que 192 bits (cifrador simétrico) ou 2048 bits (cifrador assimétrico).

4.10.8 Não se deve distribuir chaves criptográficas sem a utilização de uma infraestrutura de chave pública e, portanto, sem a utilização de um cifrador assimétrico.

**4.11 Geração de Senhas**

4.11.1 Não se deve utilizar senhas com menos de 8 caracteres.

4.11.2 Não se deve utilizar somente um tipo de caractere (letras, dígitos e símbolos).

4.11.3 Não se deve utilizar palavras comumente utilizadas para senhas (ou variantes destas), como, por exemplo: nome do animal de estimação, membro da família ou pessoa significativa; datas de aniversário; nome do feriado favorito; algo relacionado ao time esportivo favorito; e as palavras “senha” e “<span id="anchor-14"></span>password”.

4.11.4 Não se deve utilizar periodicidade de troca superior a 1 ano.

4.11.5 Não se deve armazenar senhas em claro.

4.11.6 Deve-se armazenar ao menos o hash criptográfico com salt.

4.11.7 Não se deve usar um canal em claro para a transmissão da senha ou elemento correspondente.

4.11.8 Não se deve utilizar método de conferência menos seguro que desafios baseados em hash ou o uso de <span id="anchor-15"></span>hashes armazenados.

4.11.9 Não se deve permitir uma taxa de tentativas de validação de senha superior a 5 tentativas por minuto.

4.11.10 Não se deve mostrar diretamente a senha quando esta necessita ser digitada pelo usuário; deve haver opção de habilitar e desabilitar a visualização da senha digitada até então.

**4.12 Diretrizes para reforço da segurança de software nas fases de especificação, projeto e design**

4.12.1 Deve-se empregar modelo de projeto de software que contemple, no mínimo:

> a\) a etapa de modelagem de ameaças;

> b\) definição clara dos riscos de segurança; e

> c\) nível de severidade que o comprometimento de dados sensíveis traria ao sistema e à instituição.

4.12.2 Não se deve omitir, durante o projeto de desenvolvimento de sistema e sua execução, a definição de responsabilidades pela segurança de dados do sistema e como essa responsabilidade será verificada.

4.12.3 Deve-se utilizar cronograma de projeto que contemple pontos de verificação de segurança do sistema desenvolvido ao longo de sua construção.

**4.13 Atualização de softwares**

4.13.1 Não se deve habilitar as atualizações automáticas de software ou componentes utilizados na construção de um sistema, sob pena de introdução indevida de falhas de segurança.

4.13.2 Somente utilize código de terceiros que sejam confiáveis.
