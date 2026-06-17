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
```

## MCP com opencode

Este laboratório já possui um servidor MCP local em Python para consulta ao Projeto Capivara.

Servidor configurado:

- Nome: `ai-dev-mcp-lab-docs`
- Arquivo: `servers/docs_server/server.py`
- Cliente testado: `opencode`
- Modo atual: somente leitura

Ferramentas validadas via MCP:

- `ping`
- `listar_repositorios_capivara`
- `resumir_estado_basico_capivara`

Observação: o arquivo global do opencode em `AppData/Roaming` não deve ser versionado. Chaves de API nunca devem ser salvas no repositório.

## Ferramentas MCP disponíveis

Ferramentas gerais:

- `ping`
- `listar_ferramentas_capivara`

Ferramentas de configuração e estrutura:

- `ler_config_capivara`
- `listar_repositorios_capivara`
- `verificar_caminhos_repositorios_capivara`
- `listar_docs_capivara`
- `ler_context_docs_capivara`
- `listar_estrutura_repositorios_capivara`

Ferramentas de arquivos e busca:

- `buscar_arquivo_capivara`
- `ler_arquivo_capivara`
- `ler_arquivo_por_caminho_capivara`
- `buscar_texto_capivara`
- `listar_arquivos_importantes_capivara`

Ferramentas de resumo e diagnóstico:

- `resumir_estado_basico_capivara`
- `resumir_contexto_capivara`
- `listar_endpoints_backend_capivara`
- `listar_paginas_fronts_capivara`
- `diagnosticar_autenticacao_capivara`
- `mapear_integracao_fronts_backend_capivara`

Todas as ferramentas atuais são somente leitura.
