PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
LangChain Agents
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
First, install the required packages:
Copy
```
pip install praisonaiagents langchain-community wikipedia

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
Single Tool
Multiple Tools
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
from langchain_community.utilities import WikipediaAPIWrapper
# Create an agent with Wikipedia tool
agent = Agent(
  name="WikiAgent",
  role="Research Assistant",
  goal="Search Wikipedia for accurate information",
  backstory="I am an AI assistant specialized in Wikipedia research",
  tools=[WikipediaAPIWrapper],
  self_reflect=False
)
# Create a research task
task = Task(
  name="wiki_search",
  description="Research 'Artificial Intelligence' on Wikipedia",
  expected_output="Comprehensive information from Wikipedia articles",
  agent=agent
)
# Create and start the workflow
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  verbose=True
)
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
  * OpenAI API key. Generate OpenAI API key here
  * LangChain compatible tools and utilities


## 
​
Understanding LangChain Integration
## What is LangChain Integration?
LangChain integration enables agents to:
  * Use LangChain’s extensive tool ecosystem
  * Access various data sources and APIs
  * Leverage pre-built utilities and wrappers
  * Combine multiple tools in a single agent
  * Extend agent capabilities with community tools


## 
​
Features
## Tool Integration
Seamlessly use LangChain tools with PraisonAI agents.
## Multiple Sources
Access various data sources through LangChain utilities.
## Community Tools
Leverage the extensive LangChain community ecosystem.
## Custom Tools
Create and integrate custom LangChain tools.
## 
​
Next Steps
## Memory Integration
Learn how to combine LangChain tools with agent memory
## Custom Tools
Create your own custom tools for agents
For optimal results, ensure all required dependencies are installed and API keys are properly configured for each tool.
Was this page helpful?
YesNo
Multimodal AgentsAsync Agents
On this page
  * Quick Start
  * Understanding LangChain Integration
  * Features
  * Next Steps


