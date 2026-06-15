from pprint import pprint
from server import (
    ler_config_capivara,
    listar_repositorios_capivara,
    ping,
    verificar_caminhos_repositorios_capivara,
    listar_docs_capivara,
    ler_context_docs_capivara,
    listar_estrutura_repositorios_capivara,
    buscar_arquivo_capivara,
    ler_arquivo_capivara,
    ler_arquivo_por_caminho_capivara,
    buscar_texto_capivara,
)

# pprint(ping())
# pprint(ler_config_capivara())
# pprint(ping())
# pprint(listar_repositorios_capivara())
# pprint(ping())
# pprint(verificar_caminhos_repositorios_capivara())
# pprint(ping())
# pprint(listar_docs_capivara())
# pprint(ping())
# pprint(ler_context_docs_capivara())
# pprint(ping())
# pprint(listar_estrutura_repositorios_capivara())
# print(ping())
# pprint(buscar_arquivo_capivara("package.json"))
# print(ping())
# pprint(ler_arquivo_capivara("package.json"))
# print(ping())
# pprint(
#     ler_arquivo_por_caminho_capivara(
#         r"C:\projeto_unisinos\capivara\capivara-backend\CONTEXT.md"
#     )
# )
print(ping())
pprint(buscar_texto_capivara("contents"))
