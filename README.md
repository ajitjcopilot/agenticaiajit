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

1. Install dependencies:
```bash
pip install -r requirements.txt
```

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
python main.py
```

## Project Structure

- `main.py` - Main entry point with OpenAI integration
- `gemini.py` - Google Gemini client example
- `geminiOpenaiClient.py` - OpenAI client configured for Gemini API compatibility
- `docker-compose.yml` - Docker services configuration

