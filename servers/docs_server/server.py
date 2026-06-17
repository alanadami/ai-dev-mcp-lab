from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Dev MCP Lab - Docs Server")

from tools.basic_tools import (  # noqa: E402
    listar_ferramentas_capivara,
    ping,
    registrar_basic_tools,
)
from tools.config_tools import (  # noqa: E402
    ler_config_capivara,
    ler_context_docs_capivara,
    listar_docs_capivara,
    listar_estrutura_repositorios_capivara,
    listar_repositorios_capivara,
    registrar_config_tools,
    verificar_caminhos_repositorios_capivara,
)
from tools.file_tools import (  # noqa: E402
    buscar_arquivo_capivara,
    buscar_texto_capivara,
    ler_arquivo_capivara,
    ler_arquivo_por_caminho_capivara,
    listar_arquivos_importantes_capivara,
    registrar_file_tools,
)
from tools.inspection_tools import (  # noqa: E402
    diagnosticar_autenticacao_capivara,
    listar_endpoints_backend_capivara,
    listar_paginas_fronts_capivara,
    mapear_integracao_fronts_backend_capivara,
    registrar_inspection_tools,
)
from tools.summary_tools import (  # noqa: E402
    registrar_summary_tools,
    resumir_contexto_capivara,
    resumir_estado_basico_capivara,
)

registrar_basic_tools(mcp)
registrar_config_tools(mcp)
registrar_file_tools(mcp)
registrar_summary_tools(mcp)
registrar_inspection_tools(mcp)

__all__ = [
    "mcp",
    "ping",
    "listar_ferramentas_capivara",
    "ler_config_capivara",
    "listar_repositorios_capivara",
    "verificar_caminhos_repositorios_capivara",
    "listar_docs_capivara",
    "ler_context_docs_capivara",
    "listar_estrutura_repositorios_capivara",
    "buscar_arquivo_capivara",
    "ler_arquivo_capivara",
    "ler_arquivo_por_caminho_capivara",
    "buscar_texto_capivara",
    "listar_arquivos_importantes_capivara",
    "resumir_estado_basico_capivara",
    "resumir_contexto_capivara",
    "listar_endpoints_backend_capivara",
    "listar_paginas_fronts_capivara",
    "diagnosticar_autenticacao_capivara",
    "mapear_integracao_fronts_backend_capivara",
]

if __name__ == "__main__":
    mcp.run()
