# CrewAI Research Agent

A Python application that uses CrewAI framework to create an AI-powered research agent capable of identifying and analyzing the next big trends in artificial intelligence technology.

## 🚀 Features

- **Senior Researcher Agent**: An AI agent specialized in discovering groundbreaking technologies
- **Automated Research Tasks**: Intelligent task execution for trend analysis
- **LLaMA Integration**: Powered by Meta-Llama-3.1-70B-Instruct model via Nebius AI
- **Structured Output**: Generates comprehensive 5-paragraph reports on AI trends

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## 🛠️ Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd crewAI_starter
```

### Step 2: Install Dependencies

#### Using pip
```bash
pip install crewai python-dotenv
```

#### Using UV (Recommended)
```bash
uv add crewai python-dotenv
```

Then install:
```bash
# With pip
pip install -r requirements.txt

# With UV
uv pip install -r requirements.txt
```

## 🔐 Environment Setup

### Step 1: Get Nebius AI API Key

1. Visit [Nebius AI Studio](https://studio.nebius.com/)
2. Sign up for an account or log in
3. Navigate to the API section
4. Generate a new API key
5. Copy your API key

### Step 2: Create Environment File

Create a `.env` file in the root directory of your project:

```bash
touch .env
```

Add your API key to the `.env` file:

```env
NEBIUS_API_KEY=your_nebius_api_key_here
```

**Important**: Never commit your `.env` file to version control. Add it to your `.gitignore`:

```bash
echo ".env" >> .gitignore
```

## 📁 Project Structure

```
crewai-research-agent/
│
├── main.py                 # Main application file
├── .env                    # Environment variables (not in git)
├── .env.example           # Example environment file
├── requirements.txt       # Project dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 🚀 Running the Application

### Basic Execution

1. **Ensure your virtual environment is activated**:
   ```bash
   # Check if activated (you should see the environment name in your prompt)
   which python  # Should point to your virtual environment
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

### Expected Output

The application will:
1. Initialize the CrewAI framework
2. Create a Senior Researcher agent
3. Execute the research task
4. Generate a detailed 5-paragraph report on the next big AI trend

Example output structure:
```
Starting Crew execution...
[Agent] Senior Researcher: Starting task...
[Task] Researching next big trend in AI...
[Output] Generated 5-paragraph analysis...
```

## 🔧 Configuration Options

### Customizing the LLM

You can modify the LLM configuration in `main.py`:

```python
# Change model
llm=LLM(
    model="openai/meta-llama/Meta-Llama-3.1-405B-Instruct",  # Different model
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)

# Add temperature and other parameters
llm=LLM(
    model="openai/meta-llama/Meta-Llama-3.1-70B-Instruct",
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY"),
    temperature=0.7,
    max_tokens=2000
)
```

### Modifying Agent Behavior

Customize the researcher agent:

```python
researcher = Agent(
    role='Senior Researcher',
    goal='Your custom research goal',
    verbose=True,
    backstory='Your custom backstory',
    llm=default_llm,
    # Additional parameters
    allow_delegation=False,
    max_iter=3,
    memory=True
)
```

### Changing Research Tasks

Modify the research task:

```python
research_task = Task(
    description='Your custom research description',
    expected_output='Your expected output format',
    agent=researcher,
    # Additional parameters
    context=[],  # Add context from other tasks
    tools=[]     # Add custom tools
)
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Import Error: No module named 'crewai'
```bash
# Ensure virtual environment is activated and dependencies are installed
pip install crewai python-dotenv
```

#### 2. API Key Error
```bash
# Check if .env file exists and contains correct API key
cat .env
# Ensure no extra spaces or quotes around the API key
```

#### 3. Connection Error to Nebius API
```bash
# Test your internet connection
# Verify API key is valid
# Check Nebius AI service status
```

#### 4. Python Version Compatibility
```bash
# Check Python version
python --version
# CrewAI requires Python 3.8+
```

### Debug Mode

Enable verbose logging by setting the agent's `verbose=True` (already enabled in the code) or add additional logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Advanced Usage

### Adding Multiple Agents

```python
# Create additional agents
writer = Agent(
    role='Technical Writer',
    goal='Transform research into readable content',
    backstory='Expert at making complex topics accessible',
    llm=default_llm
)

# Add to crew
tech_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential
)
```

### Adding Custom Tools

```python
from crewai_tools import SerperDevTool, WebsiteSearchTool

# Add tools to agent
researcher = Agent(
    # ... other parameters
    tools=[SerperDevTool(), WebsiteSearchTool()]
)
```

### Sequential vs Hierarchical Process

```python
# Sequential (current)
tech_crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential
)

# Hierarchical (with manager)
tech_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.hierarchical,
    manager_llm=default_llm
)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. **Check the troubleshooting section** above
2. **Review CrewAI documentation**: [https://docs.crewai.com/](https://docs.crewai.com/)
3. **Check Nebius AI documentation**: [https://docs.nebius.com/](https://docs.nebius.com/)
4. **Open an issue** in this repository with:
   - Your Python version
   - Your operating system
   - Complete error message
   - Steps to reproduce

## 🔗 Useful Links

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
- [Nebius AI Platform](https://studio.nebius.com/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [UV Package Manager](https://github.com/astral-sh/uv)

## 📊 Performance Tips

1. **Use UV for faster package management** instead of pip
2. **Enable caching** in production environments
3. **Monitor API usage** to stay within Nebius AI limits
4. **Use appropriate model sizes** based on your needs
5. **Implement retry logic** for API calls in production

---

**Happy Researching!** 🚀

If you find this project useful, please consider giving it a ⭐ on GitHub!