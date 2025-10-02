"""Timestamp tool for MCP server"""

from datetime import datetime

def timestamp() -> str:
    return datetime.now().isoformat()