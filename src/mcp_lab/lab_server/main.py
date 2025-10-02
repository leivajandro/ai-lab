"""
MCP Server with Strands Agents

Basic MCP server that can be extended with Strands agent tools.
Run with: python -m mcp_lab.lab_server.main [--transport {sse,stdio,websocket}]
"""

import argparse
from mcp.server import FastMCP
from mcp_lab.lab_server.tools import calculator, text_analyzer, timestamp

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
    
    mcp.tool(description="Calculator that evaluates mathematical expressions")(calculator)
    mcp.tool(description="Text analyzer that counts words, characters and sentences")(text_analyzer)
    mcp.tool(description="Get current timestamp")(timestamp)
    
    try:
        print(f"Starting MCP server with {args.transport} transport...")
        print("Available tools: calculator, text_analyzer, timestamp")
        print("Press Ctrl+C to stop the server")
        mcp.run(transport=args.transport)
    except KeyboardInterrupt:
        print("\nServer stopped by user")

if __name__ == "__main__":
    main()