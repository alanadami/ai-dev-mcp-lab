from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Dev MCP Lab - Docs Server")


@mcp.tool()
def ping() -> str:
    """Testa se o servidor MCP está respondendo."""
    return "pong"


if __name__ == "__main__":
    mcp.run()