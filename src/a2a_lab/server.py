import logging
from strands import Agent
from strands.multiagent.a2a import A2AServer
from .tools.calculator import calculator

def main():
    logging.basicConfig(level=logging.INFO)
    
    strands_agent = Agent(
        name="Calculator Agent",
        description="A calculator agent that can perform basic arithmetic operations.",
        tools=[calculator],
        callback_handler=None
    )
    
    a2a_server = A2AServer(agent=strands_agent)
    a2a_server.serve()

if __name__ == "__main__":
    main()