import re
from pathlib import Path
from urllib.parse import urlparse

from tools.config_tools import listar_repositorios_capivara
from tools.file_tools import buscar_texto_capivara
from utils.path_helpers import IGNORED_DIRS, is_ignored_path

HTTP_METHOD_PREFIXES = {
    "@Delete": "DELETE",
    "@Get": "GET",
    "@Patch": "PATCH",
    "@Post": "POST",
    "@Put": "PUT",
}

FRONT_ROUTE_LITERAL_RE = re.compile(r"['\"`]([^'\"`]+)['\"`]")


def _extrair_rota_decorator(decorator_line: str) -> str:
    match = re.search(r"\((.*?)\)", decorator_line)
    if not match:
        return ""

    raw_value = match.group(1).strip()
    if not raw_value:
        return ""

    return raw_value.strip("'\"`").strip()


def _normalizar_rota(path: str) -> str:
    cleaned = (path or "").strip().strip("'\"`")
    if not cleaned:
        return "/"

    if cleaned.startswith(("http://", "https://")):
        cleaned = urlparse(cleaned).path or "/"

    cleaned = cleaned.replace("\\", "/")
    cleaned = re.sub(r"/+", "/", cleaned)

    if cleaned != "/" and cleaned.endswith("/"):
        cleaned = cleaned[:-1]

    if not cleaned.startswith("/"):
        cleaned = f"/{cleaned}"

    return cleaned or "/"


def _combinar_rotas(controller_path: str, method_path: str) -> str:
    base = _normalizar_rota(controller_path)
    method = _normalizar_rota(method_path)

    if base == "/":
        return method
    if method == "/":
        return base

    return _normalizar_rota(f"{base}/{method.lstrip('/')}")


def _coletar_endpoints_backend(backend_path: Path) -> list[dict]:
    if not backend_path.exists():
        return []

    endpoints = []

    for path in backend_path.rglob("*.controller.ts"):
        if is_ignored_path(path):
            continue

        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        controller_decorator = ""
        controller_route = ""

        for line_number, line in enumerate(lines, start=1):
            stripped = line.strip()

            if stripped.startswith("@Controller"):
                controller_decorator = stripped
                controller_route = _extrair_rota_decorator(stripped)
                continue

            method_name = next(
                (name for prefix, name in HTTP_METHOD_PREFIXES.items() if stripped.startswith(prefix)),
                None,
            )

            if not method_name:
                continue

            method_route = _extrair_rota_decorator(stripped)
            endpoints.append({
                "arquivo": str(path.relative_to(backend_path)),
                "linha": line_number,
                "controller": controller_decorator,
                "rota": stripped,
                "metodo": method_name,
                "rota_normalizada": _combinar_rotas(controller_route, method_route),
            })

    return endpoints


def listar_endpoints_backend_capivara() -> list[dict]:
    """
    Lista possíveis endpoints do backend NestJS do Capivara.
    Ferramenta somente leitura.
    """
    repositories = listar_repositorios_capivara()
    backend_path = Path(repositories.get("backend", ""))
    return _coletar_endpoints_backend(backend_path)


def listar_paginas_fronts_capivara() -> dict:
    """
    Lista possíveis páginas e rotas dos frontends Next.js do Capivara.
    Ferramenta somente leitura.
    """
    repositories = listar_repositorios_capivara()
    result = {}

    for repo_name in ["frontUser", "frontAdmin"]:
        repo_path = Path(repositories.get(repo_name, ""))

        if not repo_path.exists():
            result[repo_name] = []
            continue

        pages = []

        for path in repo_path.rglob("page.js"):
            if is_ignored_path(path):
                continue

            relative_path = path.relative_to(repo_path)
            route_parts = list(relative_path.parts)

            if "app" not in route_parts:
                continue

            app_index = route_parts.index("app")
            route = route_parts[app_index + 1:-1]
            route_path = "/" + "/".join(route) if route else "/"

            pages.append({
                "arquivo": str(relative_path),
                "rota": route_path,
            })

        result[repo_name] = sorted(pages, key=lambda item: item["rota"])

    return result


def diagnosticar_autenticacao_capivara() -> dict:
    """
    Busca indícios de autenticação, JWT, guards, login e token nos repositórios do Capivara.
    Ferramenta somente leitura.
    """
    termos = [
        "auth",
        "jwt",
        "passport",
        "guard",
        "login",
        "token",
        "Authorization",
        "Bearer",
        "sessionStorage",
    ]

    result = {}

    for termo in termos:
        result[termo] = buscar_texto_capivara(termo, limite_por_repo=10)

    return result


def mapear_integracao_fronts_backend_capivara() -> dict:
    """
    Mapeia chamadas de API encontradas nos frontends e relaciona com possíveis endpoints do backend.
    Ferramenta somente leitura.
    """
    repositories = listar_repositorios_capivara()
    backend_endpoints = listar_endpoints_backend_capivara()
    result = {
        "backend_endpoints": len(backend_endpoints),
        "fronts": {},
    }

    searchable_extensions = {".js", ".jsx", ".ts", ".tsx"}
    markers = ("fetch(", "axios", "http://", "https://", "/api/", "Authorization", "Bearer ")

    for repo_name in ["frontUser", "frontAdmin"]:
        repo_path = Path(repositories.get(repo_name, ""))
        integrations = []

        if not repo_path.exists():
            result["fronts"][repo_name] = integrations
            continue

        for path in repo_path.rglob("*"):
            if is_ignored_path(path, IGNORED_DIRS) or not path.is_file() or path.suffix not in searchable_extensions:
                continue

            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue

            for line_number, line in enumerate(lines, start=1):
                if not any(marker in line for marker in markers):
                    continue

                route_candidates = []
                for literal in FRONT_ROUTE_LITERAL_RE.findall(line):
                    normalized = _normalizar_rota(literal)
                    if normalized == "/" and "/" not in literal:
                        continue
                    if "/" not in normalized and normalized != "/":
                        normalized = _normalizar_rota(f"/{normalized.lstrip('/')}")
                    if normalized not in route_candidates:
                        route_candidates.append(normalized)

                if not route_candidates:
                    continue

                possible_backend_matches = []
                for frontend_route in route_candidates:
                    matched = []

                    for endpoint in backend_endpoints:
                        backend_route = endpoint.get("rota_normalizada", "/")

                        if frontend_route == backend_route:
                            matched.append(endpoint)
                            continue

                        if frontend_route.endswith(backend_route) or backend_route.endswith(frontend_route):
                            matched.append(endpoint)
                            continue

                        front_segments = [part for part in frontend_route.split("/") if part]
                        backend_segments = [part for part in backend_route.split("/") if part]

                        if front_segments and backend_segments and front_segments[0] == backend_segments[0]:
                            matched.append(endpoint)

                    possible_backend_matches.append({
                        "rota_front": frontend_route,
                        "possiveis_endpoints_backend": matched[:10],
                    })

                integrations.append({
                    "arquivo": str(path.relative_to(repo_path)),
                    "linha": line_number,
                    "trecho": line.strip()[:200],
                    "rotas_encontradas": possible_backend_matches,
                })

        result["fronts"][repo_name] = integrations

    return result


def registrar_inspection_tools(mcp) -> None:
    for tool in (
        listar_endpoints_backend_capivara,
        listar_paginas_fronts_capivara,
        diagnosticar_autenticacao_capivara,
        mapear_integracao_fronts_backend_capivara,
    ):
        mcp.tool()(tool)
