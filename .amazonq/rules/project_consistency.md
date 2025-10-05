# Project Consistency Rules

## Code Structure Standards
- Always follow existing patterns and conventions from the project
- Before creating new files, review similar existing files for structure and style
- Maintain consistency across notebooks, scripts, and modules

## Notebook Standards
- **Structure**: Title → Configuration → Helper Functions → Main Logic → Test/Usage
- **Imports**: Group by standard library, third-party, local imports
- **Model Configuration**: Always use OpenAI local model pattern:
  ```python
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
  ```
- **Metadata**: Use consistent kernel and language info across all notebooks

## Script Standards
- **Imports**: Follow same grouping as notebooks
- **Model Configuration**: Use identical OpenAI local model setup
- **Logging**: Always include `logging.basicConfig(level=logging.INFO)`
- **Main Function**: Use `def main():` pattern with `if __name__ == "__main__":`

## Tool Standards
- **Location**: Tools in respective `tools/` directories
- **Documentation**: Include README.md in tools directories
- **Naming**: Use descriptive, consistent naming patterns

## File Organization
- **Notebooks**: Group by functionality in appropriate subdirectories
- **Source Code**: Mirror notebook structure in `src/` directory
- **Tools**: Separate tools by project type (mcp_lab, a2a_lab, etc.)

## Configuration Consistency
- **Local LLM**: Always use localhost:1234 for LM Studio
- **Ports**: MCP server (stdio/websocket), A2A server (9000)
- **Model Names**: Use "local-model" as model_id consistently

## Documentation
- **README Updates**: Always update main README.md when adding new features
- **Comments**: Minimal, self-documenting code preferred
- **Examples**: Include usage examples in notebooks and scripts