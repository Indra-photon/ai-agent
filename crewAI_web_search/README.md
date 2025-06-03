# CrewAI Healthcare AI Trends Research

A multi-agent AI system built with CrewAI that researches and writes about the latest AI trends in healthcare. This project demonstrates how to create collaborative AI agents that work together to research topics and produce high-quality content.

## Features

- **Multi-Agent Collaboration**: Two specialized AI agents working in sequence
- **Web Search Integration**: Real-time research using SerperDev search tool
- **Healthcare AI Focus**: Specifically designed to analyze AI trends in healthcare
- **Customizable LLM**: Uses Nebius AI (Meta-Llama-3.1-70B-Instruct) for intelligent responses

## Agents

### 1. Senior Researcher
- **Role**: Conducts comprehensive research on AI healthcare trends
- **Tools**: Web search capabilities via SerperDevTool
- **Goal**: Uncover the latest developments and breakthroughs

### 2. Content Writer
- **Role**: Transforms research findings into engaging articles
- **Goal**: Create accessible, well-structured content for general audiences
- **Input**: Uses research findings as context for writing

## Prerequisites

- Python 3.8 or higher
- Nebius AI API key
- Serper API key (for web search)

## Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd crewAI-web-search
```

### 2. Create Virtual Environment

#### Using Python venv:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac
```

#### Using uv (recommended):
```bash
uv venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies

#### Using pip:
```bash
pip install -r requirements.txt
```

#### Using uv (faster):
```bash
uv pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
NEBIUS_API_KEY=your_nebius_api_key_here
```

#### Getting API Keys:

**Nebius AI API Key:**
1. Visit [Nebius AI Studio](https://studio.nebius.com/)
2. Sign up for an account
3. Navigate to API section
4. Generate your API key

## Usage

### Basic Usage
```bash
python main.py
```

### How It Works

1. **Research Phase**: The Senior Researcher agent searches for the latest AI trends in healthcare using web search tools
2. **Writing Phase**: The Content Writer agent takes the research findings and creates a compelling, accessible article
3. **Sequential Process**: Agents work one after another, with the writer using the researcher's output as context

### Sample Output

The system will produce:
- A comprehensive research report on AI healthcare trends
- A 3-paragraph engaging article suitable for general audiences
- Insights on recent breakthroughs and emerging technologies

## Project Structure

```
crewai-healthcare-research/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
├── .env.example        # Environment variables template
└── README.md           # Project documentation
```

## Customization

### Changing the Research Topic
Modify the `inputs` parameter in `main.py`:
```python
result = crew.kickoff(inputs={"topic": "Your custom topic here"})
```

### Using Different LLM Models
Update the LLM configuration in `main.py`:
```python
llm = LLM(
    model="your-preferred-model",
    base_url="your-api-endpoint",
    api_key=os.getenv("YOUR_API_KEY")
)
```

### Modifying Agent Behavior
Customize agent roles, goals, and backstories in the Agent definitions to suit your specific use case.

## Troubleshooting

### Common Issues

**ImportError: cannot import name 'Tokenizer'**
- Solution: Recreate your virtual environment and reinstall dependencies

**Validation Error: Agent is missing in task**
- Solution: Ensure each task has an `agent` parameter assigned

**API Key Errors**
- Solution: Verify your `.env` file exists and contains valid API keys

### Getting Help

If you encounter issues:
1. Check that all environment variables are properly set
2. Ensure you have active internet connection for web searches
3. Verify your API keys are valid and have sufficient credits
4. Review the console output for specific error messages

## Dependencies

- `crewai[tools]>=0.121.0` - Multi-agent AI framework with tools
- `python-dotenv>=1.0.0` - Environment variable management

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.