import json
from pathlib import Path

from utils.path_helpers import CAPIVARA_CONFIG_PATH


def ler_config_capivara() -> dict:
    """Lê a configuração local do Projeto Capivara."""
    with open(CAPIVARA_CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def listar_repositorios_capivara() -> dict:
    """Lista os repositórios configurados para o Projeto Capivara."""
    config = ler_config_capivara()
    return config.get("repositories", {})


def verificar_caminhos_repositorios_capivara() -> dict:
    """Verifica se os caminhos dos repositórios configurados existem."""
    repositories = listar_repositorios_capivara()

    return {
        name: {
            "path": path,
            "exists": Path(path).exists(),
        }
        for name, path in repositories.items()
    }


def listar_docs_capivara() -> dict:
    """Lista os arquivos de documentação configurados que existem em cada repositório."""
    config = ler_config_capivara()
    repositories = config.get("repositories", {})
    docs = config.get("docs", [])

    result = {}

    for repo_name, repo_path in repositories.items():
        repo_docs = []

        for doc in docs:
            doc_path = Path(repo_path) / doc
            if doc_path.exists():
                repo_docs.append(str(doc_path))

        result[repo_name] = repo_docs

    return result


def ler_context_docs_capivara() -> dict:
    """Lê o conteúdo dos arquivos CONTEXT.md encontrados nos repositórios do Capivara."""
    docs_por_repo = listar_docs_capivara()
    result = {}

    for repo_name, doc_paths in docs_por_repo.items():
        contents = {}

        for doc_path in doc_paths:
            path = Path(doc_path)
            contents[path.name] = path.read_text(encoding="utf-8")

        result[repo_name] = contents

    return result


def listar_estrutura_repositorios_capivara() -> dict:
    """Lista a estrutura de primeiro nível dos repositórios do Capivara."""
    repositories = listar_repositorios_capivara()
    result = {}

    ignored_names = {".git", "node_modules", ".next", "dist", "generated"}

    for repo_name, repo_path in repositories.items():
        path = Path(repo_path)

        if not path.exists():
            result[repo_name] = {"exists": False, "items": []}
            continue

        items = [
            item.name + ("/" if item.is_dir() else "")
            for item in path.iterdir()
            if item.name not in ignored_names
        ]

        result[repo_name] = {
            "exists": True,
            "items": sorted(items),
        }

    return result


def registrar_config_tools(mcp) -> None:
    for tool in (
        ler_config_capivara,
        listar_repositorios_capivara,
        verificar_caminhos_repositorios_capivara,
        listar_docs_capivara,
        ler_context_docs_capivara,
        listar_estrutura_repositorios_capivara,
    ):
        mcp.tool()(tool)
