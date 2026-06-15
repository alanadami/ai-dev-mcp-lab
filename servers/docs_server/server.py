import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Dev MCP Lab - Docs Server")

ROOT_DIR = Path(__file__).resolve().parents[2]
CAPIVARA_CONFIG_PATH = ROOT_DIR / "projects" / "capivara.config.json"


@mcp.tool()
def ping() -> str:
    """Testa se o servidor MCP está respondendo."""
    return "pong"


@mcp.tool()
def ler_config_capivara() -> dict:
    """Lê a configuração local do Projeto Capivara."""
    with open(CAPIVARA_CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
    
@mcp.tool()
def listar_repositorios_capivara() -> dict:
    """Lista os repositórios configurados para o Projeto Capivara."""
    config = ler_config_capivara()
    return config.get("repositories", {})

@mcp.tool()
def verificar_caminhos_repositorios_capivara() -> dict:
    """Verifica se os caminhos dos repositórios configurados existem."""
    repositories = listar_repositorios_capivara()

    return {
        name: {
            "path": path,
            "exists": Path(path).exists()
        }
        for name, path in repositories.items()
    }

@mcp.tool()
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


if __name__ == "__main__":
    mcp.run()

