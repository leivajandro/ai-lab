# AI Lab

Machine Learning experiments using Hugging Face Transformers with text and vision models.

## Project Structure

```
ai-lab/
├── notebooks/
│   └── transformers/
│       └── tasks/
│           ├── text_generation.ipynb      # Qwen3-0.6B text generation
│           └── image_text_to_text.ipynb   # InternVL3_5-1B vision-language
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── LICENSE            # MIT License
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
source .venv/bin/activate
jupyter notebook
```

## Models

### Text Generation
- **Qwen3-0.6B**: Lightweight language model for chat and text generation
- Optimized for Apple Silicon with MPS acceleration

### Image Text to Text
- **InternVL3_5-1B**: Vision-language model for image understanding
- Supports image analysis and visual question answering

## Features

- **Apple Metal Support**: MPS acceleration for faster inference on Mac
- **Memory Efficient**: BFloat16 precision for optimal performance
- **Chat Templates**: Proper conversation formatting with role-based messages
- **Vision Capabilities**: Image understanding and multimodal interactions

Start experimenting with AI models in the notebooks!