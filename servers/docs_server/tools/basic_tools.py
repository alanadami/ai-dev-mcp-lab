TOOL_DESCRIPTIONS = [
    {
        "nome": "ping",
        "descricao": "Testa se o servidor MCP está respondendo.",
        "exemplo": "Call ping.",
    },
    {
        "nome": "listar_ferramentas_capivara",
        "descricao": "Lista as ferramentas MCP disponíveis para consulta ao Projeto Capivara.",
        "exemplo": "Call listar_ferramentas_capivara.",
    },
    {
        "nome": "ler_config_capivara",
        "descricao": "Lê a configuração local do Projeto Capivara.",
        "exemplo": "Call ler_config_capivara.",
    },
    {
        "nome": "listar_repositorios_capivara",
        "descricao": "Lista os repositórios configurados do Projeto Capivara.",
        "exemplo": "Call listar_repositorios_capivara.",
    },
    {
        "nome": "verificar_caminhos_repositorios_capivara",
        "descricao": "Verifica se os caminhos dos repositórios existem.",
        "exemplo": "Call verificar_caminhos_repositorios_capivara.",
    },
    {
        "nome": "listar_docs_capivara",
        "descricao": "Lista os documentos configurados encontrados nos repositórios.",
        "exemplo": "Call listar_docs_capivara.",
    },
    {
        "nome": "ler_context_docs_capivara",
        "descricao": "Lê os arquivos CONTEXT.md encontrados nos repositórios.",
        "exemplo": "Call ler_context_docs_capivara.",
    },
    {
        "nome": "listar_estrutura_repositorios_capivara",
        "descricao": "Lista a estrutura de primeiro nível dos repositórios.",
        "exemplo": "Call listar_estrutura_repositorios_capivara.",
    },
    {
        "nome": "buscar_arquivo_capivara",
        "descricao": "Busca arquivos pelo nome nos repositórios do Capivara.",
        "parametros": ["nome_arquivo"],
        "exemplo": "Call buscar_arquivo_capivara with nome_arquivo='package.json'.",
    },
    {
        "nome": "ler_arquivo_capivara",
        "descricao": "Busca e lê arquivos pelo nome.",
        "parametros": ["nome_arquivo"],
        "exemplo": "Call ler_arquivo_capivara with nome_arquivo='README.md'.",
    },
    {
        "nome": "ler_arquivo_por_caminho_capivara",
        "descricao": "Lê um arquivo por caminho, desde que esteja dentro dos repositórios permitidos.",
        "parametros": ["caminho_arquivo"],
        "exemplo": "Call ler_arquivo_por_caminho_capivara with caminho_arquivo='...'.",
    },
    {
        "nome": "buscar_texto_capivara",
        "descricao": "Busca um termo nos arquivos de texto dos repositórios.",
        "parametros": ["termo", "limite_por_repo"],
        "exemplo": "Call buscar_texto_capivara with termo='auth' and limite_por_repo=20.",
    },
    {
        "nome": "listar_arquivos_importantes_capivara",
        "descricao": "Lista arquivos importantes encontrados nos repositórios.",
        "exemplo": "Call listar_arquivos_importantes_capivara.",
    },
    {
        "nome": "resumir_contexto_capivara",
        "descricao": "Resume os arquivos CONTEXT.md dos repositórios do Capivara.",
        "exemplo": "Call resumir_contexto_capivara.",
    },
    {
        "nome": "resumir_estado_basico_capivara",
        "descricao": "Resume o estado básico do Projeto Capivara.",
        "exemplo": "Call resumir_estado_basico_capivara.",
    },
    {
        "nome": "listar_endpoints_backend_capivara",
        "descricao": "Lista possíveis endpoints do backend NestJS do Capivara.",
        "exemplo": "Call listar_endpoints_backend_capivara.",
    },
    {
        "nome": "listar_paginas_fronts_capivara",
        "descricao": "Lista possíveis páginas e rotas dos frontends Next.js do Capivara.",
        "exemplo": "Call listar_paginas_fronts_capivara.",
    },
    {
        "nome": "diagnosticar_autenticacao_capivara",
        "descricao": "Busca indícios de autenticação, JWT, guards, login e token nos repositórios.",
        "exemplo": "Call diagnosticar_autenticacao_capivara.",
    },
    {
        "nome": "mapear_integracao_fronts_backend_capivara",
        "descricao": "Mapeia chamadas de API encontradas nos fronts e relaciona com possíveis endpoints do backend.",
        "exemplo": "Call mapear_integracao_fronts_backend_capivara.",
    },
]


def ping() -> str:
    """Testa se o servidor MCP está respondendo."""
    return "pong"


def listar_ferramentas_capivara() -> list[dict]:
    """
    Lista as ferramentas MCP disponíveis para consulta ao Projeto Capivara.
    Ferramenta somente leitura.
    """
    return [dict(item) for item in TOOL_DESCRIPTIONS]


def registrar_basic_tools(mcp) -> None:
    for tool in (ping, listar_ferramentas_capivara):
        mcp.tool()(tool)
