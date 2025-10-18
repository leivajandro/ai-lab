"""Bedrock AgentCore server with Strands agent integration.

Deploys a Strands agent as an HTTP service using the Bedrock AgentCore Runtime SDK.
The server accepts JSON payloads with a 'prompt' key and returns agent responses.

Usage:
    python -m bedrock.agentcore.strands_agent

Endpoint:
    POST /invocations
    Content-Type: application/json
    Body: {"prompt": "Your message here"}
"""

import logging
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

logging.basicConfig(level=logging.INFO)

agent = Agent()
app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """Process agent invocation requests.
    
    Args:
        payload (dict): Request payload containing 'prompt' key
        
    Returns:
        dict: Response with 'result' key containing agent message
    """
    user_message = payload.get("prompt", "Hello")
    result = agent(user_message)
    return {"result": result.message}

def main():
    """Start the Bedrock AgentCore HTTP server."""
    app.run()

if __name__ == "__main__":
    main()