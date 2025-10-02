"""
MCP Server with Strands Agents

Basic MCP server that can be extended with Strands agent tools.
Run with: python scripts/mcp_server.py
"""

from mcp.server import FastMCP

mcp = FastMCP("Strands Agent Server")

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="sse")