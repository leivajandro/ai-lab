# MCP Lab Server Tools

Collection of tools for the MCP Lab Server implementation.

## Available Tools

### Calculator
Mathematical expression evaluator that supports basic arithmetic operations.

```python
from mcp_lab.lab_server.tools import calculator
result = calculator("2 + 3 * 4")  # Returns: "Result: 14"
```

### Text Analyzer
Analyzes text content and provides statistics about words, characters, and sentences.

```python
from mcp_lab.lab_server.tools import text_analyzer
stats = text_analyzer("Hello world. This is a test.")
# Returns: {"word_count": 6, "char_count": 28, "sentences": 2}
```

### Timestamp
Returns the current date and time in ISO format.

```python
from mcp_lab.lab_server.tools import timestamp
current_time = timestamp()  # Returns: "2024-01-15T10:30:45.123456"
```

## Usage in MCP Server

These tools are automatically registered when the MCP server starts:

```bash
mcp-server
# Available tools: calculator, text_analyzer, timestamp
```

## Usage from Client

Connect to the MCP server and use tools remotely:

```python
from mcp.client.sse import sse_client
from strands.tools.mcp import MCPClient

# Connect to server
sse_mcp_client = MCPClient(lambda: sse_client("http://localhost:8000/sse"))

with sse_mcp_client:
    tools = sse_mcp_client.list_tools_sync()
    # Use tools with Strands agents
```

## Adding New Tools

1. Create a new Python file in this directory
2. Define your tool function with proper type hints
3. Add docstring describing the tool's purpose
4. Update `__init__.py` to include the new tool
5. Register the tool in `main.py` using `@mcp.tool()` decorator
6. Update this README with usage examples

## Tool Requirements

- Functions should have clear type hints
- Include proper error handling
- Return serializable data types (str, dict, list, int, float)
- Add descriptive docstrings
- Keep functions stateless and thread-safe