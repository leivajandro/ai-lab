import logging
from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands.models.openai import OpenAIModel
from .tools.calculator import calculator

def main():
    logging.basicConfig(level=logging.INFO)
    
    model = OpenAIModel(
        client_args={
            "api_key": "none",
            "base_url": "http://localhost:1234/v1",
        },
        model_id="local-model",
        params={
            "temperature": 0.1,
            "top_p": 0.9,
            "frequency_penalty": 0.0
        }
    )
    
    strands_agent = Agent(
        name="Calculator Agent",
        description="A calculator agent that can perform basic arithmetic operations.",
        model=model,
        tools=[calculator],
        callback_handler=None
    )
    
    a2a_server = A2AServer(agent=strands_agent)
    a2a_server.serve()

if __name__ == "__main__":
    main()