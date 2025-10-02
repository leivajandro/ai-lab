from setuptools import setup, find_packages

setup(
    name="ai-lab",
    version="0.1.0",
    description="Machine Learning experiments with AI agents and MCP",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "mcp-server=mcp_lab.lab_server.main:main",
        ],
    },
    install_requires=[
        "accelerate",
        "ipykernel",
        "huggingface_hub[cli]",
        "jupyter",
        "mcp[server]",
        "mcp[streamable-http]",
        "mlx",
        "mlx-lm",
        "mlx-vlm",
        "nest-asyncio",
        "openai",
        "Pillow",
        "strands-agents",
        "strands-agents-tools",
        "torch",
        "torchvision",
        "transformers",
    ],
)