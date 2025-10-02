"""
MCP Server with Strands Agents

Basic MCP server that can be extended with Strands agent tools.
Run with: python scripts/mcp_server.py [--transport {sse,stdio,websocket}]
"""

import argparse
from mcp.server import FastMCP

def main():
    parser = argparse.ArgumentParser(description="MCP Server with Strands Agents")
    parser.add_argument(
        "--transport", 
        choices=["sse", "stdio", "websocket"], 
        default="sse",
        help="Transport protocol (default: sse)"
    )
    
    args = parser.parse_args()
    
    mcp = FastMCP("Strands Agent Server")
    
    try:
        print(f"Starting MCP server with {args.transport} transport...")
        print("Press Ctrl+C to stop the server")
        mcp.run(transport=args.transport)
    except KeyboardInterrupt:
        print("\nServer stopped by user")

if __name__ == "__main__":
    main()