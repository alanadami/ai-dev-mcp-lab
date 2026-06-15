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

@mcp.tool()
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

@mcp.tool()
def listar_estrutura_repositorios_capivara() -> dict:
    """Lista a estrutura de primeiro nível dos repositórios do Capivara."""
    repositories = listar_repositorios_capivara()
    result = {}

    for repo_name, repo_path in repositories.items():
        path = Path(repo_path)

        if not path.exists():
            result[repo_name] = {"exists": False, "items": []}
            continue

        items = [
            item.name + ("/" if item.is_dir() else "")
            for item in path.iterdir()
            if item.name not in [".git", "node_modules", ".next", "dist", "generated"]
        ]

        result[repo_name] = {
            "exists": True,
            "items": sorted(items)
        }

    return result

@mcp.tool()
def buscar_arquivo_capivara(nome_arquivo: str) -> dict:
    """Busca arquivos pelo nome dentro dos repositórios do Capivara."""
    repositories = listar_repositorios_capivara()
    result = {}

    ignored_dirs = {".git", "node_modules", ".next", "dist", "generated", "__pycache__"}

    for repo_name, repo_path in repositories.items():
        matches = []

        for path in Path(repo_path).rglob(nome_arquivo):
            if any(part in ignored_dirs for part in path.parts):
                continue

            matches.append(str(path))

        result[repo_name] = matches

    return result

@mcp.tool()
def ler_arquivo_capivara(nome_arquivo: str) -> dict:
    """Busca e lê arquivos pelo nome dentro dos repositórios do Capivara."""
    arquivos_encontrados = buscar_arquivo_capivara(nome_arquivo)
    result = {}

    for repo_name, paths in arquivos_encontrados.items():
        contents = []

        for file_path in paths:
            path = Path(file_path)

            try:
                contents.append({
                    "path": str(path),
                    "content": path.read_text(encoding="utf-8")
                })
            except UnicodeDecodeError:
                contents.append({
                    "path": str(path),
                    "error": "Arquivo encontrado, mas não pôde ser lido como texto UTF-8."
                })

        result[repo_name] = contents

    return result

@mcp.tool()
def ler_arquivo_por_caminho_capivara(caminho_arquivo: str) -> dict:
    """Lê um arquivo por caminho, permitindo apenas arquivos dentro dos repositórios configurados."""
    repositories = listar_repositorios_capivara()
    file_path = Path(caminho_arquivo).resolve()

    allowed_roots = [Path(path).resolve() for path in repositories.values()]

    if not any(file_path.is_relative_to(root) for root in allowed_roots):
        return {
            "allowed": False,
            "error": "Arquivo fora dos repositórios permitidos."
        }

    if not file_path.exists():
        return {
            "allowed": True,
            "exists": False,
            "error": "Arquivo não encontrado."
        }

    if not file_path.is_file():
        return {
            "allowed": True,
            "exists": True,
            "error": "O caminho informado não é um arquivo."
        }

    try:
        return {
            "allowed": True,
            "exists": True,
            "path": str(file_path),
            "content": file_path.read_text(encoding="utf-8")
        }
    except UnicodeDecodeError:
        return {
            "allowed": True,
            "exists": True,
            "path": str(file_path),
            "error": "Arquivo encontrado, mas não pôde ser lido como texto UTF-8."
        }
    
@mcp.tool()
def buscar_texto_capivara(termo: str, limite_por_repo: int = 20) -> dict:
    """Busca um termo em arquivos de texto dos repositórios do Capivara, retornando arquivo, linha e trecho."""
    repositories = listar_repositorios_capivara()
    ignored_dirs = {".git", "node_modules", ".next", "dist", "generated", "__pycache__", ".venv"}
    allowed_extensions = {".md", ".js", ".jsx", ".ts", ".tsx", ".json", ".prisma", ".css"}

    result = {}

    for repo_name, repo_path in repositories.items():
        matches = []
        root_path = Path(repo_path)

        if not root_path.exists():
            result[repo_name] = []
            continue

        for path in root_path.rglob("*"):
            if len(matches) >= limite_por_repo:
                break

            if any(part in ignored_dirs for part in path.parts):
                continue

            if not path.is_file():
                continue

            if path.suffix not in allowed_extensions:
                continue

            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue

            for line_number, line in enumerate(lines, start=1):
                if termo.lower() in line.lower():
                    excerpt = line.strip()

                    matches.append({
                        "path": str(path.relative_to(root_path)),
                        "line": line_number,
                        "excerpt": excerpt[:200]
                    })

                    if len(matches) >= limite_por_repo:
                        break

        result[repo_name] = matches

    return result


if __name__ == "__main__":
    mcp.run()

