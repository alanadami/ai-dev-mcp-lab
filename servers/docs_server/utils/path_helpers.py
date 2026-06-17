from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
CAPIVARA_CONFIG_PATH = ROOT_DIR / "projects" / "capivara.config.json"

IGNORED_DIRS = {
    ".git",
    ".next",
    ".venv",
    "__pycache__",
    "dist",
    "generated",
    "node_modules",
}

TEXT_FILE_EXTENSIONS = {
    ".css",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".prisma",
    ".ts",
    ".tsx",
}

IMPORTANT_FILES = [
    "package.json",
    "CONTEXT.md",
    "README.md",
    "schema.prisma",
    "next.config.js",
    "next.config.mjs",
    "main.ts",
    "app.module.ts",
]


def is_ignored_path(path: Path, ignored_dirs: set[str] | None = None) -> bool:
    ignored = ignored_dirs or IGNORED_DIRS
    return any(part in ignored for part in path.parts)


def resolve_repo_roots(repositories: dict) -> list[Path]:
    return [Path(path).resolve() for path in repositories.values() if path]


def is_path_inside_roots(path: Path, roots: list[Path]) -> bool:
    return any(path.is_relative_to(root) for root in roots)

