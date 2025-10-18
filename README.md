# AI Lab

Machine Learning experiments using Hugging Face Transformers with text, vision models, and AI agents.

## Project Structure

```
ai-lab/
├── .amazonq/
│   └── rules/                             # Amazon Q configuration rules
│       ├── commit_rules.md                # Git commit message standards
│       ├── interaction_rules.md           # AI interaction guidelines
│       └── project_consistency.md         # Project structure and coding standards
├── assets/
│   ├── documents/                         # PDF documents for testing
│   └── images/                            # Test images for vision models
├── models/                                # Local model storage
├── notebooks/
│   ├── transformers/
│   │   └── tasks/
│   │       ├── text_generation.ipynb      # Text generation with transformers
│   │       └── image_text_to_text.ipynb   # Vision-language models
│   ├── mlx/
│   │   └── tasks/
│   │       ├── conversion.ipynb           # Convert HF models to MLX format
│   │       ├── upload.ipynb               # Upload models to Hugging Face Hub
│   │       └── text_generation.ipynb      # MLX text generation
│   └── strands_agents/
│       ├── basics/                        # Fundamental agent examples
│       │   ├── basic.ipynb                # Simple agent with local LLM
│       │   ├── hooks.ipynb                # Agent with lifecycle hooks
│       │   ├── session.ipynb              # Agent with persistent sessions
│       │   ├── multimodal.ipynb           # Agent with vision capabilities
│       │   └── streaming.ipynb            # Agent with async streaming
│       ├── features/                      # Advanced agent features
│       │   ├── conversation_manager.ipynb # Conversation management
│       │   └── structured_output.ipynb    # Structured response generation
│       ├── tools/                         # Custom agent tools
│       │   ├── auto_tools.ipynb           # Automatic tool discovery
│       │   ├── tool_executor.ipynb        # Custom tool execution
│       │   └── [other tool files]         # Tool implementations
│       ├── multi_agent/                   # Multi-agent collaboration patterns
│       │   ├── agents_as_tools.ipynb      # Agents as tools orchestration
│       │   ├── swarm.ipynb                # Multi-agent swarm collaboration
│       │   ├── swarm_as_tool.ipynb        # Dynamic swarm creation
│       │   └── graph.ipynb                # Graph-based workflow
│       ├── mcp/                           # Model Context Protocol
│       │   └── mcp_client.ipynb           # MCP client implementation
│       └── a2a/                           # Agent-to-Agent communication
│           ├── a2a_server.ipynb           # A2A server agent
│           ├── a2a_client.ipynb           # A2A client communication
│           └── [other a2a files]          # A2A implementations
├── src/
│   ├── archetype/
│   │   └── strands_agent/                 # Agent framework source code
│   ├── a2a_lab/
│   │   ├── server.py                      # A2A server implementation
│   │   └── tools/
│   │       ├── calculator.py              # Mathematical calculator tool
│   │       └── README.md                  # Tools documentation
│   └── mcp_lab/
│       └── lab_server/
│           ├── main.py                    # MCP server implementation
│           └── tools/
│               ├── calculator.py          # Mathematical calculator tool
│               ├── text_analyzer.py       # Text analysis tool
│               ├── timestamp.py           # Timestamp tool
│               └── README.md              # Tools documentation
├── pyproject.toml     # Project configuration and dependencies
├── .gitignore        # Git ignore rules
└── LICENSE           # MIT License
```

## Setup

### Install uv

**macOS/Linux:**
```bash
brew install uv
```

**Alternative (curl):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install dependencies

**Create virtual environment and install all dependencies:**
```bash
uv sync
```

**Activate virtual environment:**
```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

**Add new dependencies:**
```bash
uv add package-name
uv add --dev package-name  # Development dependencies
```

**Install from requirements.txt:**
```bash
uv pip install -r requirements.txt
```

**Run commands with uv (without activating venv):**
```bash
uv run python script.py
uv run jupyter notebook
```

## Usage

### Notebooks
```bash
uv run jupyter notebook
```

### MCP Server
```bash
uv run mcp-server
uv run mcp-server --transport stdio
uv run mcp-server --transport websocket
uv run python -m mcp_lab.lab_server.main
```

### A2A Server
```bash
uv run a2a-server
uv run python -m a2a_lab.server
```



## Models

### Text Generation
- Lightweight language models for chat and text generation
- Optimized for Apple Silicon with MPS acceleration

### Vision-Language Models
- Multimodal models for image understanding and analysis
- Support visual question answering and image description

### MLX Models (Apple Silicon Optimized)
- Quantized language models for efficient text generation
- Native Apple Silicon acceleration with MLX framework
- Local model storage in `models/` directory

### AI Agents
- Tool-using agents with local LLM integration
- Connects to local OpenAI-compatible servers (LM Studio, etc.)
- Advanced features: sessions, hooks, streaming, structured output
- Model Context Protocol (MCP) support
- Custom tool development and execution

## Tools

### MCP Tools
The project includes MCP tools in `src/mcp_lab/lab_server/tools/`:
- **Calculator**: Mathematical expression evaluator
- **Text Analyzer**: Word, character, and sentence counter
- **Timestamp**: Current date and time provider

### A2A Tools
The project includes A2A tools in `src/a2a_lab/tools/`:
- **Calculator**: Mathematical expression evaluator

See respective `README.md` files for detailed documentation.

## Features

- **Apple Metal Support**: MPS acceleration for faster inference on Mac
- **MLX Optimization**: Native Apple Silicon acceleration with quantized models
- **Memory Efficient**: BFloat16 precision and 4-bit quantization for optimal performance
- **Chat Templates**: Proper conversation formatting with role-based messages
- **Text Generation**: Advanced language model capabilities with chat templates
- **Model Conversion**: Convert Hugging Face models to optimized MLX format
- **Model Upload**: Upload models to Hugging Face Hub for sharing
- **Agent Framework**: Tool-using AI agents with local LLM backends
- **MCP Server**: Model Context Protocol server for agent integration
- **A2A Server**: Agent-to-Agent HTTP server for multi-agent communication

Start experimenting with AI models and agents in the notebooks!