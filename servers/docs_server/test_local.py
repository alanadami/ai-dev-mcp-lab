from pprint import pprint

from server import (
    buscar_arquivo_capivara,
    buscar_texto_capivara,
    diagnosticar_autenticacao_capivara,
    ler_arquivo_capivara,
    ler_arquivo_por_caminho_capivara,
    ler_config_capivara,
    ler_context_docs_capivara,
    listar_arquivos_importantes_capivara,
    listar_docs_capivara,
    listar_endpoints_backend_capivara,
    listar_ferramentas_capivara,
    listar_paginas_fronts_capivara,
    listar_repositorios_capivara,
    listar_estrutura_repositorios_capivara,
    mapear_integracao_fronts_backend_capivara,
    ping,
    resumir_contexto_capivara,
    resumir_estado_basico_capivara,
    verificar_caminhos_repositorios_capivara,
)


def testar_ping():
    print(ping())

def testar_listar_paginas_fronts_capivara():
    pprint(listar_paginas_fronts_capivara())

def testar_diagnosticar_autenticacao_capivara():
    pprint(diagnosticar_autenticacao_capivara())

def testar_mapear_integracao_fronts_backend_capivara():
    pprint(mapear_integracao_fronts_backend_capivara())

def testar_listar_endpoints_backend_capivara():
    pprint(listar_endpoints_backend_capivara())

def testar_resumir_contexto_capivara():
    pprint(resumir_contexto_capivara())


def testar_ler_config_capivara():
    pprint(ler_config_capivara())


def testar_listar_repositorios_capivara():
    pprint(listar_repositorios_capivara())


def testar_verificar_caminhos_repositorios_capivara():
    pprint(verificar_caminhos_repositorios_capivara())


def testar_listar_docs_capivara():
    pprint(listar_docs_capivara())


def testar_ler_context_docs_capivara():
    pprint(ler_context_docs_capivara())


def testar_listar_estrutura_repositorios_capivara():
    pprint(listar_estrutura_repositorios_capivara())


def testar_buscar_arquivo_capivara():
    nome_arquivo = input("Digite o nome do arquivo: ").strip()
    pprint(buscar_arquivo_capivara(nome_arquivo))


def testar_ler_arquivo_capivara():
    nome_arquivo = input("Digite o nome do arquivo: ").strip()
    pprint(ler_arquivo_capivara(nome_arquivo))


def testar_ler_arquivo_por_caminho_capivara():
    caminho_arquivo = input("Digite o caminho completo do arquivo: ").strip()
    pprint(ler_arquivo_por_caminho_capivara(caminho_arquivo))


def testar_buscar_texto_capivara():
    termo = input("Digite o termo de busca: ").strip()

    limite = input("Digite o limite por repositório ou pressione Enter para usar 20: ").strip()
    limite_por_repo = int(limite) if limite else 20

    pprint(buscar_texto_capivara(termo, limite_por_repo))


def testar_listar_arquivos_importantes_capivara():
    pprint(listar_arquivos_importantes_capivara())


def testar_resumir_estado_basico_capivara():
    resultado = resumir_estado_basico_capivara()

    print("\n=== RESUMO BÁSICO DO PROJETO CAPIVARA ===\n")

    print("Projeto:", resultado.get("projeto"))
    print("Modo:", resultado.get("modo"))

    print("\nRepositórios:")
    pprint(resultado.get("repositorios"))

    print("\nVerificação dos caminhos:")
    pprint(resultado.get("verificacao_caminhos"))

    print("\nDocumentos encontrados:")
    pprint(resultado.get("documentos_encontrados"))

    print("\nArquivos importantes:")
    pprint(resultado.get("arquivos_importantes"))

def testar_listar_ferramentas_capivara():
    pprint(listar_ferramentas_capivara())


TESTES = {
    "1": ("ping", testar_ping),
    "2": ("ler_config_capivara", testar_ler_config_capivara),
    "3": ("listar_repositorios_capivara", testar_listar_repositorios_capivara),
    "4": ("verificar_caminhos_repositorios_capivara", testar_verificar_caminhos_repositorios_capivara),
    "5": ("listar_docs_capivara", testar_listar_docs_capivara),
    "6": ("ler_context_docs_capivara", testar_ler_context_docs_capivara),
    "7": ("listar_estrutura_repositorios_capivara", testar_listar_estrutura_repositorios_capivara),
    "8": ("buscar_arquivo_capivara", testar_buscar_arquivo_capivara),
    "9": ("ler_arquivo_capivara", testar_ler_arquivo_capivara),
    "10": ("ler_arquivo_por_caminho_capivara", testar_ler_arquivo_por_caminho_capivara),
    "11": ("buscar_texto_capivara", testar_buscar_texto_capivara),
    "12": ("listar_arquivos_importantes_capivara", testar_listar_arquivos_importantes_capivara),
    "13": ("resumir_estado_basico_capivara", testar_resumir_estado_basico_capivara),
    "14": ("listar_ferramentas_capivara", testar_listar_ferramentas_capivara),
    "15": ("resumir_contexto_capivara", testar_resumir_contexto_capivara),
    "16": ("listar_endpoints_backend_capivara", testar_listar_endpoints_backend_capivara),
    "17": ("listar_paginas_fronts_capivara", testar_listar_paginas_fronts_capivara),
    "18": ("diagnosticar_autenticacao_capivara", testar_diagnosticar_autenticacao_capivara),
    "19": ("mapear_integracao_fronts_backend_capivara", testar_mapear_integracao_fronts_backend_capivara),
}


def exibir_menu():
    print("\n=== TESTES LOCAIS - AI DEV MCP LAB ===\n")

    for numero, (nome, _) in TESTES.items():
        print(f"{numero}. {nome}")

    print("\n0. Sair")


def executar_teste(opcao):
    teste = TESTES.get(opcao)

    if not teste:
        print("\nOpção inválida.")
        return

    nome, funcao = teste

    print(f"\n=== Executando: {nome} ===\n")
    funcao()


def main():
    while True:
        exibir_menu()

        opcao = input("\nEscolha um teste: ").strip()

        if opcao == "0":
            print("\nEncerrando testes locais.")
            break

        executar_teste(opcao)

        input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main()
