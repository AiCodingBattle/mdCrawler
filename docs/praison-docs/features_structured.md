PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Structured AI Agents
DocumentationExamplesAgentsUIToolsJS
PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
  * Home


##### Getting Started
  * Introduction
  * Installation
  * Quick Start


##### Core Concepts
  * Agents
  * Tasks
  * Process
  * Tools
  * Memory
  * Knowledge


##### Workflows
  * Agentic Routing
  * Orchestrator Worker
  * Autonomous Workflow
  * Parallelization
  * Prompt Chaining
  * Evaluator Optimizer
  * Repetitive Agents


##### Features
  * CLI
  * AutoAgents
  * Image Generation
  * Self Reflection Agents
  * RAG Agents
  * Reasoning Extract Agents
  * Reasoning Agents
  * Multimodal Agents
  * LangChain Agents
  * Async Agents
  * Mini AI Agents
  * Generate Reasoning Data
  * Code Agent
  * Math Agent
  * Structured AI Agents
  * Callbacks Agent
  * Chat with PDF


##### Models
  * Models in PraisonAI
  * OpenAI ChatGPT
  * Ollama
  * Groq
  * Google Gemini
  * OpenRouter
  * Anthropic
  * Cohere
  * Mistral
  * DeepSeek Agents
  * Other Models


##### Tools
  * Firecrawl PraisonAI Integration


##### Other Features
  * PraisonAI Train
  * CrewAI with PraisonAI
  * AutoGen with PraisonAI
  * PraisonAI Agents


##### Monitoring
  * AgentOps PraisonAI Monitoring


##### Developers
  * Test
  * Agents Playbook
  * PraisonAI Package Integration
  * Integrate with Tools
  * Google Colab Integration
  * Google Colab Tools
  * Local Development
  * Deploy


##### Getting Started (No Code)
  * Introduction
  * TL;DR
  * Installation
  * Initialise
  * Run
  * Auto Generation Mode


##### API Reference
  * API Reference
  * Agent Module
  * Agents Module
  * AutoAgents Module
  * Task Module
  * Process Module


## 
​
Quick Start
  * Code
  * No Code


1
Install Package
First, install the PraisonAI Agents package:
Copy
```
pip install praisonaiagents

```

2
Set API Key
Set your OpenAI API key as an environment variable in your terminal:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

3
Create a file
Create a new file `app.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents, Tools
from pydantic import BaseModel
# Define your data structure
class AnalysisReport(BaseModel):
  title: str
  findings: str
  summary: str
# Create agent
analyst = Agent(
  role="Data Analyst",
  goal="Analyze data and provide structured insights",
  backstory="Expert in data analysis and insights generation",
  tools=[Tools.internet_search],
  verbose=True
)
# Create task with structured output
task = Task(
  description="Analyze recent AI developments",
  expected_output="Structured analysis report",
  agent=analyst,
  output_pydantic=AnalysisReport
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[analyst],
  tasks=[task],
  process="sequential",
  verbose=2
)
# Start execution
result = agents.start()
print(result.pydantic.title)
print(result.pydantic.findings)
print(result.pydantic.summary)

```

4
Start Agents
Type this in your terminal to run your agents:
Copy
```
python app.py

```

**Requirements**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.
  * Basic understanding of Python and Pydantic


## 
​
Understanding Structured Outputs
## What are Structured Outputs?
Structured outputs allow you to:
  * Define exact shape of data using Pydantic models
  * Get type-safe, validated responses
  * Choose between Pydantic objects or JSON
  * Ensure consistent output format across agent responses


## 
​
Features
## Pydantic Models
Define exact data structures with validation.
## JSON Output
Get structured JSON responses.
## Type Safety
Ensure type-safe, validated outputs.
## Format Options
Choose between Pydantic or JSON.
## 
​
Multi-Agent Structured Analysis
  * Code
  * No Code


1
Install Package
First, install the PraisonAI Agents package:
Copy
```
pip install praisonaiagents

```

2
Set API Key
Set your OpenAI API key as an environment variable in your terminal:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

3
Create a file
Create a new file `app.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents, Tools
from pydantic import BaseModel
# Define output structures
class ResearchReport(BaseModel):
  topic: str
  findings: str
  sources: list[str]
class Analysis(BaseModel):
  key_points: list[str]
  implications: str
  recommendations: str
# Create first agent for research
researcher = Agent(
  role="Research Analyst",
  goal="Gather and structure research data",
  backstory="Expert in research and data collection",
  tools=[Tools.internet_search],
  verbose=True
)
# Create second agent for analysis
analyst = Agent(
  role="Data Analyst",
  goal="Analyze research and provide structured insights",
  backstory="Expert in data analysis and insights generation",
  verbose=True
)
# Create first task
research_task = Task(
  description="Research quantum computing developments",
  expected_output="Structured research findings",
  agent=researcher,
  output_pydantic=ResearchReport
)
# Create second task
analysis_task = Task(
  description="Analyze research implications",
  expected_output="Structured analysis report",
  agent=analyst,
  output_pydantic=Analysis
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[researcher, analyst],
  tasks=[research_task, analysis_task],
  process="sequential"
)
# Start execution
result = agents.start()

```

4
Start Agents
Type this in your terminal to run your agents:
Copy
```
python app.py

```

### 
​
Configuration Options
Copy
```
# Create an agent with structured output configuration
agent = Agent(
  role="Data Analyst",
  goal="Provide structured analysis",
  backstory="Expert in data analysis",
  tools=[Tools.internet_search],
  verbose=True, # Enable detailed logging
  llm="gpt-4o" # Language model to use
)
# Task with Pydantic output
task = Task(
  description="Analyze data",
  expected_output="Structured report",
  agent=agent,
  output_pydantic=AnalysisReport # Use Pydantic model
  # or output_json=AnalysisReport # Use JSON output
)

```

## 
​
Troubleshooting
## Validation Errors
If model validation fails:
  * Check data types match model
  * Verify required fields
  * Enable verbose mode for debugging


## Output Format
If output format is incorrect:
  * Verify model definition
  * Check output_pydantic vs output_json
  * Review field specifications


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your Pydantic models accurately represent your desired output structure.
Was this page helpful?
YesNo
Math AgentCallbacks Agent
On this page
  * Quick Start
  * Understanding Structured Outputs
  * Features
  * Multi-Agent Structured Analysis
  * Configuration Options
  * Troubleshooting
  * Next Steps


