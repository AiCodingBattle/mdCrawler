Django
The web framework for perfectionists with deadlines.
Alternar tema (tema atual: automático)
Alternar tema (tema atual: claro)
Alternar tema (tema atual: escuro)
Toggle Light / Dark / Auto color theme
Menu
  * Overview
  * Download
  * Documentation
  * News
  * Community
  * Code
  * Issues
  * About
  * ♥ Donate
  * Alternar tema (tema atual: automático)
Alternar tema (tema atual: claro)
Alternar tema (tema atual: escuro)
Toggle Light / Dark / Auto color theme


# Documentação
Search: Buscar
  * Getting Help


  * el
  * en
  * es
  * fr
  * id
  * it
  * ja
  * ko
  * pl
  * zh-hans
  * Idioma: **pt-br**


  * 1.10
  * 1.11
  * 2.0
  * 2.1
  * 2.2
  * 3.0
  * 3.1
  * 3.2
  * 4.0
  * 4.1
  * 4.2
  * 5.0
  * dev
  * Versão da Documentação **5.1**


  * 

# Documentação do Django¶
Tudo o que você precisa saber sobre Django.
## Primeiros passos¶
Você é novo no Django ou na programação? Este é o lugar para começar!
  * **Do início:** Visão geral | Instalação
  * **Tutorial:** Parte 1: Requisições e respostas | Parte 2: Modelos e o site Admin | Parte 3: Views e templates | Parte 4: Forms e views genéricas | Parte 5: Testes | Parte 6: Arquivos estáticos | Parte 7: Personalizando o site admin | Parte 8: Adicionando pacotes de terceiros
  * **Tutoriais avançados:** Como escrever aplicações reutilizáveis | Escrevendo sua primeira contribuição para o Django


## Obtendo ajuda¶
Está com problemas? Nós gostaríamos de ajudar!
  * Tente o FAQ – para obter respostas para muitas perguntas comuns.
  * Procurando por alguma informação específica? Tente o Índice, Índice do Módulo ou the tabela detalhada de conteúdos.
  * Não encontrou nada? Veja o FAQ: Obtendo ajuda para informações sobre como obter suporte e pergunte a comunidade.
  * Relate bugs do Django no nosso ticket tracker.


## Como a documentação é organizada¶
Django tem uma grande quantidade de documentação. Uma visão geral de como ele é organizado vai te ajudar a saber aonde procurar para certas coisas:
  * Tutoriais conduzem você pela mão através de uma série de passos para criar uma aplicação web. Comece aqui se você é novo no Django ou no desenvolvimento de aplicações web. Veja também o “Primeiros passos”.
  * Guia de tópicos discute temas-chave e conceitos em um nível relativamente alto, fornece explicaçõesde modo de funcionamento e informações úteis.
  * Guiaa de referências contém referência técnica para APIs e outros aspectos do maquinário do Django. Eles descrevem como isso funciona e como usá-los, mas assume que você tem um entendimento básico dos conceitos chaves.
  * Guias ‘How-to’ são receitas. Eles guiam você através de passos baseados na abordagem de problemas chave e casos de uso. Eles são mais avançados que os tutoriais e assumem que você já tem algum conhecimento de como o Django trabalha.


## A camada de modelo¶
O Django fornece uma camada de abstração (os “modelos”) para estruturar e manipular os dados de sua aplicação web. Saiba mais sobre isso abaixo:
  * **Models:** Introdução ao “Models” | Tipos de campos | Índices | Opções da Meta | A classe Model
  * **QuerySets:** Fazendo consultas | Referência do método QuerySet | Expressões de pesquisa
  * **Instâncias de modelo:** Métodos de instâncias | Acessando objetos relacionados
  * **Migração:** Introdução a Migrações | Referência de operação | SchemaEditor | Escrevendo migrações
  * **Avançado:** Managers | Raw SQL | Transações | Agregação | Busca | Campos personalizados | Vários bancos de dados | Pesquisas personalizadas | Expressões de consulta | Expressões condicionais | Funções de banco de dados
  * **Outros:** Banco de dados suportados | Bancos de dados legados | Provendo dados iniciais | Otimizando acesso ao banco de dados | Características específicas do PostgreSQL


## A camada de visão¶
Django tem o conceito de “views” para encapsular a lógica responsável pelo processamento de um request de um usuário e para retornar o response. Encontre tudo que você precisa saber sobre views através dos links abaixo:
  * **O básico:** URLconfs | Funções de view | Atalhos | Decorators | Suporte assíncrono
  * **Referência:** Views nativas | Objetos request/response | Objetos TemplateResponse
  * **File uploads:** Visão Geral | File objects | Storage API | Managing files | Custom storage
  * **Class-based views:** Visão Geral | modo interno para views | edição interna para views | Usando mixins | API referência | index plana
  * **Avançado:** Gerando CSV | Gerando PDF
  * **Middleware:** Visão geral | Classes de Middleware embutidas


## A camada de template¶
A camada de template fornece uma sintaxe amigável para designers para o processamento de informações a serem apresentadas para o usuário. Aprenda como essa sintaxe pode ser usada por designers e como ela pode ser estendida por programadores:
  * **O basico:** Visão geral
  * **Para designers:** Visão geral da linguagem | Tags e filtros incluídos | Humanização
  * **Para programadores:** API de Template | Tags e filtros personalizados | Backend de template personalizado


## Formulários¶
Django fornece um framework rico para facilitar a criação de formulários de a manipulacação de dados do formulário.
  * **O básico:** Visão geral | Formulário API | Built-in fields | Widgets embutidos
  * **Avançado:** Forms para models | integrando media | Formsets | Customizando a validação


## O processo de desenvolvimento¶
Aprenda sobre os vários componentes e ferramentas para ajudá-lo no desenvolvimento e teste de aplicações Django:
  * **Configurações:** Visão global | Lista completa de configurações
  * **Aplicações:** Visão geral
  * **Exceções:** Visão global
  * **django-admin e manage.py:** Visão geral | Adicionando comandos personalizados
  * **Testando:** Introdução | Escrevendo e rodando testes | Ferramentas de testes inclusas | Tópicos avançados
  * **Implantação:** Visão Geral | Servidores WSGI | Implantando arquivos estáticos | Reportando códigos de erros por e-mail


## O Admin¶
Encontre tudo o que você precisa para conhecer sobre a interface automatizada de administração, uma das funcionalidades mais popular do Django:
  * Site Admin
  * Ações do Admin
  * Gerador de documentação do Admin


## Segurança¶
A segurança é um tema de suma importância no desenvolvimento de aplicações web e o Django oferece múltiplas ferramentas e mecanismos de proteção:
  * Visão geral sobre segurança
  * Questões de segurança divulgadas no Django
  * Proteção Clickjacking
  * Proteção contra Cross Site Request Forgery
  * Assinatura criptográfica
  * Middleware de segurança


## Internacionalização e localização¶
Django oferece um robusto framework para internacionalização e localização para a auxiliá-lo no desenvolvimento de aplicações para vários idiomas e regiões do mundo:
  * Visão geral | Internacionalização | Localização | Formato de localização da Web UI e entrada de formulário
  * Fusos horários


## Performance e otimização¶
Há uma variedade de técnicas e ferramentas que podem ajudar a fazer com que o seu código execute com mais eficiência - mais rápido e usando menos recursos do sistema.
  * Visão geral do desempenho e otimização


## Framework geográfico¶
GeoDjango pretende ser um framework web geográfico de classe mundial. Seu objetivo é facilitar ao máximo a construção de aplicativos web GIS e aproveitar o poder dos dados habilitados espacialmente.
## Ferramentas comuns de aplicação web¶
O Django oferece várias ferramentas comumente necessárias no desenvolvimento de aplicações web:
  * **Autenticação:** Visão feral | Usando o sistemas de autenticação | gerenciamento de senhas | Autenticação personalizada | API de referencia
  * Cacheamento
  * Logging
  * Enviando emails
  * Feeds (RSS/Atom)
  * Paginação
  * Framework de mensagens
  * Serialização
  * Sessões
  * Sitemaps
  * Gerenciamento de arquivos estáticos
  * Validação de dados


## Outras funcionalidades¶
Saiba mais sobre algumas outras funcionalidades do núcleo do Django framework:
  * Processamento condicional de conteúdo
  * Tipos de conteúdos e relações genéricas
  * Flatpages
  * Redirecionamentos
  * Signals
  * Framework de verificação do sistema
  * O framework Sites
  * Unicode no Django


## O projeto de código-aberto Django¶
Saiba mais sobre o processo de desenvolvimento do próprio Django e como você pode contribuir:
  * **Community:** Contributing to Django | The release process | Team organization | The Django source code repository | Security policies | Mailing lists and Forum
  * **Filosofias de design:** Visão geral
  * **Documentação:** Sobre esta documentação
  * **Distribuição de terceiros:** Visão geral
  * **Django ao longo do tempo:** Estabilidade da AP | Notas de lançamento e instruções de atualização | Cronograma de depreciação


Documentação do Django - conteúdo
Introdução 
Back to Top
# Informações Adicionais
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * slf software GmbH donated to the Django Software Foundation to support Django development. Donate today! 


## Navegar
  * Próx: Documentação do Django - conteúdo
  * Ant: Introdução
  * Tabela de conteúdos
  * Índice Geral
  * Índice de Módulos Python


## Você está aqui:
  * Documentação do Django 5.1
    * Documentação do Django


## Conseguindo ajuda
FAQ
    Tente o FAQ — lá tem a resposta para várias perguntas comuns.
Íindice, Índice do módulo, or Tabela de conteúdos
    Útil ao procurar por uma informação especifica.
Django Discord Server
    Join the Django Discord Community.
Official Django Forum
    Join the community on the Django Forum.
Ticket tracker
    Reporte bugs no Django ou na Documentação do Django em nosso ticket tracker.
## Download:
Offline (Django 5.1): HTML | PDF | ePub Oferecido por Leia o Doc. 
# Django Links
## Learn More
  * About Django
  * Getting Started with Django
  * Team Organization
  * Django Software Foundation
  * Code of Conduct
  * Diversity Statement


## Get Involved
  * Join a Group
  * Contribute to Django
  * Submit a Bug
  * Report a Security Issue
  * Individual membership


## Get Help
  * Getting Help FAQ
  * Django Discord
  * Official Django Forum


## Follow Us
  * GitHub
  * Twitter
  * Fediverse (Mastodon)
  * News RSS


## Support Us
  * Sponsor Django
  * Corporate membership
  * Official merchandise store
  * Benevity Workplace Giving Program


Django
  * Hosting by In-kind donors
  * Design by Threespot & andrevv


© 2005-2025  Django Software Foundation and individual contributors. Django is a registered trademark of the Django Software Foundation. 
