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
uv add --dev bedrock-agentcore-starter-toolkit
```

## Files

- `agentcore_archetype.py` - Production agent for AWS deployment
- `requirements.txt` - Dependencies required by Amazon Bedrock AgentCore
- `pyproject.toml` - Modern dependency management

## AWS Deployment

### Set AWS credentials
```bash
export AWS_PROFILE=personal
export AWS_DEFAULT_REGION=us-east-1
```

### Configure agent
```bash
agentcore configure --entrypoint agentcore_archetype.py --region us-east-1
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

### Production Agent (`agentcore_archetype.py`)
- Uses default Strands configuration
- Ready for AWS deployment
- No local dependencies
- Optimized for cloud deployment

## Dependencies

- **strands-agents**: AI agent framework
- **bedrock-agentcore**: AWS deployment SDK