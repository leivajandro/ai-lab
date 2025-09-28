from strands import tool

@tool
def custom_tool(message: str) -> str:
    """
    A custom tool that processes messages.
    
    Args:
        message (str): The message to process
        
    Returns:
        str: Processed message
    """
    return f"Processed: {message}"