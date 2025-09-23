# AI Lab

Machine Learning experiments using Hugging Face Transformers.

## Project Structure

```
ai-lab/
├── notebooks/
│   └── transformers/
│       └── tasks/
│           └── text_generation.ipynb
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── LICENSE            # MIT License
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

```bash
source .venv/bin/activate
jupyter notebook notebooks/transformers/tasks/text_generation.ipynb
```

Start experimenting with transformers in the text generation notebook!