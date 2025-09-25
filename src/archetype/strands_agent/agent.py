from strands import Agent, tool
from strands.models.openai import OpenAIModel
from strands_tools import calculator, current_time

@tool
def custom_tool(input_param: str) -> str:
    """
    Custom tool description.
    
    Args:
        input_param (str): Parameter description
        
    Returns:
        str: Return description
    """
    print(f"Custom tool called with input: {input_param}")
    # TODO: Implement custom logic here
    return f"Processed: {input_param}"

model = OpenAIModel(
    client_args={
        "api_key": "none",
        "base_url": "http://localhost:1234/v1",
    },
    model_id="local-model",
    params={
        "temperature": 0.1,
        "top_p": 0.95,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
    }
)

tools = [calculator, current_time, custom_tool]
agent = Agent(tools=tools)

message = """
Your agent prompt here.
"""

if __name__ == "__main__":
    agent(message)