# MCP Dev Lab

Laboratório pessoal para estudar e experimentar o uso de **Model Context Protocol (MCP)** no desenvolvimento de software com apoio de Inteligência Artificial.

Este projeto tem como objetivo criar uma camada local de ferramentas para que assistentes de IA possam consultar, analisar e revisar projetos de código de forma mais organizada, segura e contextualizada.

## Objetivo

O objetivo principal deste laboratório é aprender a usar MCP na prática, criando servidores e ferramentas que permitam à IA acessar informações reais de projetos locais, como documentação, estrutura de pastas, arquivos de código, status do Git, diffs e planejamentos técnicos.

A proposta inicial é usar o **Projeto Capivara** como primeiro caso de estudo, sem alterar o fluxo oficial da equipe e sem exigir que outros desenvolvedores utilizem esta ferramenta.

## Escopo inicial

Na primeira fase, este laboratório será usado apenas como uma central de consulta e análise.

A IA poderá:

- ler documentação do projeto;
- consultar arquivos `.md`;
- identificar estrutura dos repositórios;
- analisar o funcionamento geral do código;
- verificar o que já foi implementado;
- apontar o que ainda falta fazer;
- consultar status do Git;
- ler diffs e commits;
- apoiar revisões antes de Pull Requests.

Nesta fase, a IA não deverá:

- alterar arquivos;
- criar commits;
- executar comandos destrutivos;
- modificar branches;
- fazer `git push`;
- apagar arquivos;
- acessar credenciais;
- acessar arquivos `.env`.

## Uso com o Projeto Capivara

O Projeto Capivara será utilizado como primeiro ambiente de teste para o laboratório.

Os repositórios analisados serão configurados por caminho local, por exemplo:

```txt
capivara-backend
capivara-front-user
capivara-front-admin
