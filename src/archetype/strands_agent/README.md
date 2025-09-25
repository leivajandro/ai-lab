# Strands Agent Template

Base template for creating agents with tools using Strands and local LLM.

## Installation

```bash
pip install -r requirements.txt
```

## Local LLM Setup

1. Configure your local LLM server with OpenAI compatible API
2. Ensure it's running on `http://localhost:1234/v1`

## Usage

```bash
python -u agent.py
```

## Customization

### Modify tools
```python
tools = [calculator, current_time, your_custom_tool]
```

### Change LLM configuration
```python
model = OpenAIModel(
    client_args={
        "base_url": "http://localhost:1234/v1",  # Your server
    },
    model_id="your-model-name",  # Model name
    params={
        "temperature": 0.1,  # Adjust creativity
    }
)
```

### Create custom tool
```python
@tool
def my_tool(param: str) -> str:
    """Tool description."""
    # Your logic here
    return result
```

## Structure

- `agent.py` - Main agent
- `README.md` - This documentation
- `requirements.txt` - Dependencies

## Using as Template

1. Copy the entire folder
2. Modify `agent.py` with your tools
3. Update the agent message
4. Run with `python -u agent.py`