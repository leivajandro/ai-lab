# Strands Agent - Local Development

Local development server for Strands agent with localhost LLM integration.

## Setup

### Install dependencies
```bash
uv sync
```

## Usage

### Run local server
```bash
uv run python strands_agent.py
```

### Test server
```bash
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'
```

## Configuration

- **LLM Server**: localhost:1234 (LM Studio)
- **Model**: local-model
- **Port**: 8080

## Dependencies

- **strands-agents**: AI agent framework
- **bedrock-agentcore**: HTTP server SDK
- **openai**: Client for local LLM server