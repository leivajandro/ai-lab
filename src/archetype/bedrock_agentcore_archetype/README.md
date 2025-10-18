# Strands Agent - Bedrock AgentCore Deployment

Deploy a Strands agent to AWS using Bedrock AgentCore Runtime SDK.

## Setup

### Install uv
```bash
brew install uv
```

### Create independent project
```bash
uv init . --no-workspace
```

### Add dependencies
```bash
uv add strands-agents bedrock-agentcore
```

## Files

- `main.py` - Production agent for AWS deployment
- `requirements.txt` - Legacy requirements file
- `pyproject.toml` - Modern dependency management

## AWS Deployment

### Configure agent
```bash
agentcore configure --entrypoint main.py --region us-east-1
```

### Test deployment locally
```bash
agentcore launch --local
```

### Deploy to AWS
```bash
agentcore launch
```

### Check status
```bash
agentcore status
```

### Test deployed agent
```bash
agentcore invoke '{"prompt": "Hello"}'
```

## Agent Configuration

### Production Agent (`main.py`)
- Uses default Strands configuration
- Ready for AWS deployment
- No local dependencies
- Optimized for cloud deployment

## Dependencies

- **strands-agents**: AI agent framework
- **bedrock-agentcore**: AWS deployment SDK