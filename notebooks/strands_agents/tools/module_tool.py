"""Module Tool Example

Demonstrates how to create a modular tool for Strands agents with:
- Custom tool specification (TOOL_SPEC)
- Structured input schema with validation
- Tool function that processes parameters and returns structured responses

This pattern allows tools to be defined as standalone Python modules
that can be imported and used across different agent configurations.
"""

from typing import Any

TOOL_SPEC = {
    "name": "module_tool",
    "description": "Modular tool with custom specification for text processing.",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "input_text": {
                    "type": "string",
                    "description": "Text input to process"
                },
                "operation": {
                    "type": "string",
                    "description": "Operation to perform",
                    "enum": ["uppercase", "lowercase", "reverse"],
                    "default": "uppercase"
                }
            },
            "required": ["input_text"]
        }
    }
}

def module_tool(tool, **kwargs: Any):
    """Process text input with specified operation.
    
    Args:
        tool: Tool invocation data containing toolUseId and input parameters
        **kwargs: Additional keyword arguments
        
    Returns:
        dict: Structured response with toolUseId, status, and processed content
    """
    tool_use_id = tool["toolUseId"]
    tool_input = tool["input"]

    input_text = tool_input.get("input_text", "")
    operation = tool_input.get("operation", "uppercase")
    if operation == "uppercase":
        result = input_text.upper()
    elif operation == "lowercase":
        result = input_text.lower()
    elif operation == "reverse":
        result = input_text[::-1]
    else:
        result = input_text

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": f"Processed text: {result}"}]
    }