from tools.config_tools import (
    ler_config_capivara,
    ler_context_docs_capivara,
    listar_docs_capivara,
    listar_repositorios_capivara,
    verificar_caminhos_repositorios_capivara,
)
from tools.file_tools import listar_arquivos_importantes_capivara


def resumir_estado_basico_capivara() -> dict:
    """
    Resume o estado básico do Projeto Capivara com base na configuração,
    repositórios, caminhos, documentos e arquivos importantes.
    Ferramenta somente leitura.
    """
    config = ler_config_capivara()
    repositorios = listar_repositorios_capivara()
    caminhos = verificar_caminhos_repositorios_capivara()
    docs = listar_docs_capivara()
    arquivos_importantes = listar_arquivos_importantes_capivara()

    return {
        "projeto": "Projeto Capivara",
        "modo": "somente leitura",
        "configuracao": config,
        "repositorios": repositorios,
        "verificacao_caminhos": caminhos,
        "documentos_encontrados": docs,
        "arquivos_importantes": arquivos_importantes,
    }


def resumir_contexto_capivara() -> dict:
    """
    Resume os arquivos CONTEXT.md encontrados nos repositórios do Capivara.
    Ferramenta somente leitura.
    """
    contextos = ler_context_docs_capivara()
    result = {}

    for repo_name, docs in contextos.items():
        context_md = docs.get("CONTEXT.md")

        if not context_md:
            result[repo_name] = {
                "encontrado": False,
                "resumo": "CONTEXT.md não encontrado.",
            }
            continue

        linhas = [linha.strip() for linha in context_md.splitlines() if linha.strip()]
        titulos = [linha for linha in linhas if linha.startswith("#")]
        tecnologias = [
            linha
            for linha in linhas
            if any(
                termo in linha.lower()
                for termo in ["next", "nestjs", "prisma", "postgres", "passport", "jwt", "docker", "rancher"]
            )
        ]
        portas = [
            linha
            for linha in linhas
            if "localhost" in linha.lower() or "porta" in linha.lower()
        ]

        result[repo_name] = {
            "encontrado": True,
            "titulos": titulos[:20],
            "possiveis_tecnologias": tecnologias[:20],
            "possiveis_portas": portas[:20],
            "total_linhas_relevantes": len(linhas),
        }

    return result


def registrar_summary_tools(mcp) -> None:
    for tool in (resumir_estado_basico_capivara, resumir_contexto_capivara):
        mcp.tool()(tool)
