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


if __name__ == "__main__":
    mcp.run()