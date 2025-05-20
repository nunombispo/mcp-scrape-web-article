# MCP Web Article Scraper

A Python-based web scraping tool that uses Bright Data's MCP (Machine Control Protocol) to extract and process web articles. This project combines the power of Mistral AI's language model with Bright Data's web scraping capabilities to create an intelligent web scraping agent.

## Features

- Interactive chat interface for web scraping tasks
- Powered by Mistral AI's large language model
- Uses Bright Data's MCP for reliable web scraping
- Asynchronous operation for better performance
- Environment variable based configuration
- Fast dependency management with uv

## Prerequisites

- Python 3.8 or higher
- Node.js and npm
- Bright Data account and API credentials
- Mistral AI API key
- uv (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mcp-scrape-web-article.git
cd mcp-scrape-web-article
```

2. Install uv if you haven't already:

```bash
# On Windows
curl -sSf https://astral.sh/uv/install.ps1 | powershell
# On Unix or MacOS
curl -sSf https://astral.sh/uv/install.sh | sh
```

3. Create and activate a virtual environment:

```bash
# Create virtual environment with uv
uv venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

4. Install Python dependencies:

```bash
uv pip install -r requirements.txt
```

5. Create a `.env` file in the project root with the following variables:

```env
MISTRALAI_API_KEY=your_mistral_ai_api_key
API_TOKEN=your_brightdata_api_token
BROWSER_AUTH=your_browser_auth
WEB_UNLOCKER_ZONE=your_web_unlocker_zone
```

## Usage

1. Make sure your virtual environment is activated and all dependencies are installed.

2. Run the script:

```bash
uv run main.py
```

3. The interactive chat interface will start. You can:
   - Type your web scraping requests
   - Type 'exit' or 'quit' to end the session

## Project Structure

- `main.py`: Main application file containing the chat interface and agent setup
- `requirements.txt`: Python package dependencies
- `pyproject.toml`: UV package dependencies
- `.env`: Environment variables configuration (not tracked in git)

## Dependencies

- mcp: Bright Data's Machine Control Protocol client
- langchain-mcp-adapters: Tools for integrating MCP with LangChain
- langgraph: For creating the agent workflow
- langchain-mistralai: Mistral AI integration for LangChain
- python-dotenv: For environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Bright Data for providing the MCP infrastructure
- Mistral AI for the language model capabilities
- The LangChain community for the framework and tools
- uv for fast Python package management
