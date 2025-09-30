from strands import tool, ToolContext

@tool(context=True)
def custom_tool(tool_context: ToolContext, message: str) -> str:
    """
    A custom tool that processes messages.
    
    Args:
        message (str): The message to process
        
    Returns:
        str: Processed message
    """
    return f"The agent name is {tool_context.agent.name} processed: {message}"