PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Self Reflection AI Agents
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


In
AI Agent
Self Reflection
Out
Self-reflection enables agents to evaluate and improve their own responses before delivering them.
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
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create an agent with self-reflection
agent = Agent(
  role="Senior Research Analyst",
  goal="Analyze and provide insights on given topics",
  backstory="You are an expert analyst with strong critical thinking skills",
  self_reflect=True # Enable self-reflection
)
# Create a task
task = Task(
  description="Analyze recent developments in AI",
  expected_output="A detailed analysis report",
  agent=agent
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  process="sequential",
  verbose=2
)
# Start execution
agents.start()

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


## 
​
Understanding Self-Reflection
## What is Self-Reflection?
Self-reflection enables agents to:
  * Evaluate their own responses before delivery
  * Check for completeness and accuracy
  * Improve output quality through iteration
  * Ensure task requirements are met
  * Make conscious decisions about their responses


## 
​
Features
## Quality Assurance
Evaluates and improves response quality through self-review.
## Iterative Improvement
Refines responses through multiple reflection cycles.
## Task Validation
Ensures all aspects of the task are properly addressed.
## Conscious Decision Making
Enables thoughtful evaluation of responses.
## 
​
Multi-Agent Self-Reflection
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
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create first agent with self-reflection
researcher = Agent(
  role="Senior Research Analyst",
  goal="Research and analyze AI developments",
  backstory="Expert analyst specializing in AI trends and impacts",
  self_reflect=True,
  verbose=True
)
# Create second agent with self-reflection
writer = Agent(
  role="Technical Writer",
  goal="Transform research into clear documentation",
  backstory="Experienced in creating technical content and documentation",
  self_reflect=True,
  verbose=True
)
# Create first task
research_task = Task(
  description="Research and analyze recent AI developments",
  expected_output="Comprehensive analysis of AI trends",
  agent=researcher
)
# Create second task
documentation_task = Task(
  description="Create technical documentation from research findings",
  expected_output="Well-structured technical documentation",
  agent=writer
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[researcher, writer],
  tasks=[research_task, documentation_task],
  process="sequential"
)
# Start execution
agents.start()

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
# Create an agent with advanced self-reflection configuration
agent = Agent(
  role="Research Analyst",
  goal="Provide comprehensive analysis",
  backstory="Expert analyst with critical thinking skills",
  self_reflect=True, # Enable self-reflection
  verbose=True, # Enable detailed logging
  llm="gpt-4o", # Language model to use
  allow_delegation=True # Allow task delegation
)

```

## 
​
Troubleshooting
## Response Issues
If responses are not meeting expectations:
  * Enable verbose mode for debugging
  * Review agent configuration
  * Check task description clarity


## Quality Issues
If output quality is insufficient:
  * Enable verbose mode
  * Review agent role and goal
  * Clarify expected output


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, configure reflection parameters based on your specific use case requirements.
Was this page helpful?
YesNo
Image GenerationRAG Agents
On this page
  * Quick Start
  * Understanding Self-Reflection
  * Features
  * Multi-Agent Self-Reflection
  * Configuration Options
  * Troubleshooting
  * Next Steps


