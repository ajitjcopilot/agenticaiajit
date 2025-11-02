# AgenticaIAjit

A Python project for experimenting with GenAI models including OpenAI GPT and Google Gemini, with Qdrant vector database integration.

## Features

- OpenAI GPT integration with token counting
- Google Gemini integration
- Qdrant vector database support via Docker
- Valkey (Redis-compatible) cache support

## Requirements

- Python 3.x
- Docker and Docker Compose

## Setup

### Prerequisites

Install `uv` if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or with pip:
```bash
pip install uv
```

### Installation

1. Install dependencies with uv:
```bash
uv sync
```

This will:
- Create a virtual environment automatically (`.venv/`)
- Install all project dependencies
- Generate a `uv.lock` file for reproducible installs

**Note:** The `uv.lock` file should be committed to version control for reproducible builds.

2. Set up environment variables in a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

3. Start services with Docker Compose:
```bash
docker-compose up -d
```

This will start:
- Qdrant vector database on port 6333
- Valkey cache on port 6379

## Usage

Run the main script:
```bash
uv run python main.py
```

Or activate the virtual environment first:
```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
python main.py
```

## Managing Dependencies

- Add a new dependency: `uv add package-name`
- Remove a dependency: `uv remove package-name`
- Update dependencies: `uv lock --upgrade`
- Sync dependencies: `uv sync`

## Project Structure

- `main.py` - Main entry point with OpenAI integration
- `gemini.py` - Google Gemini client example
- `geminiOpenaiClient.py` - OpenAI client configured for Gemini API compatibility
- `docker-compose.yml` - Docker services configuration

