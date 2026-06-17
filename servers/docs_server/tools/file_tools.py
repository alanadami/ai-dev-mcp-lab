from pathlib import Path

from tools.config_tools import listar_repositorios_capivara
from utils.path_helpers import (
    IGNORED_DIRS,
    IMPORTANT_FILES,
    TEXT_FILE_EXTENSIONS,
    is_ignored_path,
    is_path_inside_roots,
    resolve_repo_roots,
)


def buscar_arquivo_capivara(nome_arquivo: str) -> dict:
    """Busca arquivos pelo nome dentro dos repositórios do Capivara."""
    repositories = listar_repositorios_capivara()
    result = {}

    for repo_name, repo_path in repositories.items():
        matches = []

        for path in Path(repo_path).rglob(nome_arquivo):
            if is_ignored_path(path):
                continue

            matches.append(str(path))

        result[repo_name] = matches

    return result


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
                    "content": path.read_text(encoding="utf-8"),
                })
            except UnicodeDecodeError:
                contents.append({
                    "path": str(path),
                    "error": "Arquivo encontrado, mas não pôde ser lido como texto UTF-8.",
                })

        result[repo_name] = contents

    return result


def ler_arquivo_por_caminho_capivara(caminho_arquivo: str) -> dict:
    """Lê um arquivo por caminho, permitindo apenas arquivos dentro dos repositórios configurados."""
    repositories = listar_repositorios_capivara()
    file_path = Path(caminho_arquivo).resolve()
    allowed_roots = resolve_repo_roots(repositories)

    if not is_path_inside_roots(file_path, allowed_roots):
        return {
            "allowed": False,
            "error": "Arquivo fora dos repositórios permitidos.",
        }

    if not file_path.exists():
        return {
            "allowed": True,
            "exists": False,
            "error": "Arquivo não encontrado.",
        }

    if not file_path.is_file():
        return {
            "allowed": True,
            "exists": True,
            "error": "O caminho informado não é um arquivo.",
        }

    try:
        return {
            "allowed": True,
            "exists": True,
            "path": str(file_path),
            "content": file_path.read_text(encoding="utf-8"),
        }
    except UnicodeDecodeError:
        return {
            "allowed": True,
            "exists": True,
            "path": str(file_path),
            "error": "Arquivo encontrado, mas não pôde ser lido como texto UTF-8.",
        }


def buscar_texto_capivara(termo: str, limite_por_repo: int = 20) -> dict:
    """Busca um termo em arquivos de texto dos repositórios do Capivara, retornando arquivo, linha e trecho."""
    repositories = listar_repositorios_capivara()
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

            if is_ignored_path(path):
                continue

            if not path.is_file() or path.suffix not in TEXT_FILE_EXTENSIONS:
                continue

            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue

            for line_number, line in enumerate(lines, start=1):
                if termo.lower() in line.lower():
                    matches.append({
                        "path": str(path.relative_to(root_path)),
                        "line": line_number,
                        "excerpt": line.strip()[:200],
                    })

                    if len(matches) >= limite_por_repo:
                        break

        result[repo_name] = matches

    return result


def listar_arquivos_importantes_capivara() -> dict:
    """Lista arquivos importantes encontrados nos repositórios do Capivara."""
    result = {}

    for arquivo in IMPORTANT_FILES:
        result[arquivo] = buscar_arquivo_capivara(arquivo)

    return result


def registrar_file_tools(mcp) -> None:
    for tool in (
        buscar_arquivo_capivara,
        ler_arquivo_capivara,
        ler_arquivo_por_caminho_capivara,
        buscar_texto_capivara,
        listar_arquivos_importantes_capivara,
    ):
        mcp.tool()(tool)
