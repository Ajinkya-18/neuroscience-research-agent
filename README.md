---
title: Neuroscience Research Assistant
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: streamlit
main: "app.py"
python_version: "3.10" 

---

# Neuroscience Research Assistant

A small agentic research assistant project that wires a LangChain-based agent to a web-search tool and a Streamlit UI.

This repository contains the minimal components used to construct and run an agent backed by Gemini (via the `langchain-google-genai` integration) and a Tavily search tool (via `langchain-tavily`). The project includes a Streamlit app to interact with the agent.

## HuggingFace Space
[Neuroscience Research Agent](https://huggingface.co/spaces/Infernus-18/neuroscience-research-agent)

## What’s in this repository

- `agents/agent.py` — Builds and returns a configured LangChain agent using:
  - `init_chat_model` with `gemini-3.1-pro-preview` from `google_genai`
  - A system prompt for neuroscience research assistance
  - The `tavily_search` tool (imported from `tools.tools`)
  - The agent is created with temperature=0.45.

- `tools/tools.py` — Defines a `tavily_search` tool using `langchain_tavily`:
  - A `TavilySearch` instance is created with `max_results=5`, `topic="general"`, `search_depth="advanced"`, `include_raw_content=False`, `include_answer=False`.

- `app.py` — A Streamlit front-end that:
  - Imports the agent from `agents.agent`
  - Provides a chat UI to send user prompts to the agent and display responses.
  - Streams responses from the agent.

- `requirements.txt` — Lists runtime dependencies observed in the repository:
  - `streamlit`
  - `langchain`
  - `langchain-google-genai`
  - `langchain-tavily`
  - `python-dotenv`

- `LICENSE` — MIT License (copyright 2025 Ajinkya A Tamhankar).

## Environment and configuration

- The code expects API keys to be provided via environment variables or a `.env` file and uses `python-dotenv` to load them. The project references the following environment variables in multiple files:
  - `TAVILY_API_KEY` (or `TAVILLY_API_KEY` in a couple of places in the code — check for the exact spelling in your environment)
  - `GOOGLE_API_KEY`
  
  Note: The repository sets these environment variables from `os.getenv(...)` in the code before creating client instances. Ensure the appropriate API keys are available in your environment.

## How to run (local)

1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Create a `.env` file (or set environment variables) with the expected API keys.
4. Run the Streamlit app.

Example (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# create a .env file with TAVILY_API_KEY and GOOGLE_API_KEY (or set environment variables)
streamlit run app.py
```

## Notes and caveats

- The README only documents code and files present in the repository. It does not claim any hosted service or external infrastructure.
- The Streamlit UI attempts to import and load the agent and will stop with an error message if imports fail or API keys are missing.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
