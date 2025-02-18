PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Getting Started
Quick Start
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


# 
​
Basic
  * Code
  * No Code
  * JavaScript


1
Install Package
Install the PraisonAI Agents package:
Copy
```
pip install praisonaiagents

```

2
Set API Key
Copy
```
export OPENAI_API_KEY=your_openai_key

```

Generate your OpenAI API key from OpenAI. Use other LLM providers like Ollama, Anthropic, Groq, Google, etc. Please refer to the Models for more information.
3
Create Agents
Create `app.py`:
Single Agent
Multiple Agents
Copy
```
from praisonaiagents import Agent, PraisonAIAgents
# Create a simple agent
summarise_agent = Agent(instructions="Summarise Photosynthesis")
# Run the agent
agents = PraisonAIAgents(agents=[summarise_agent])
agents.start()

```

4
Run Agents
Execute your script:
Copy
```
python app.py

```

You’ll see:
  * Agent initialization
  * Task execution progress
  * Final results


You have successfully CreatedAI Agents and made them work for you!
**Prerequisites**
  * Python 3.10 or higher
  * OpenAI API key (get it here)
  * For other LLM providers, see Models


# 
​
Advanced
## 
​
Providing Detailed Tasks to Agents (Optional)
  * Code
  * No Code


1
Install PraisonAI
Install the core package:
Terminal
Copy
```
pip install praisonaiagents

```

2
Configure Environment
Terminal
Copy
```
export OPENAI_API_KEY=your_openai_key

```

Generate your OpenAI API key from OpenAI Use other LLM providers like Ollama, Anthropic, Groq, Google, etc. Please refer to the Models for more information.
3
Create Agent
Create `app.py`:
Single Agent
Multiple Agents
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create an agent
researcher = Agent(
  name="Researcher",
  role="Senior Research Analyst",
  goal="Uncover cutting-edge developments in AI",
  backstory="You are an expert at a technology research group",
  verbose=True,
  llm="gpt-4o"
)
# Define a task
task = Task(
  name="research_task",
  description="Analyze 2024's AI advancements",
  expected_output="A detailed report",
  agent=researcher
)
# Run the agents
agents = PraisonAIAgents(
  agents=[researcher],
  tasks=[task],
  verbose=False
)
result = agents.start()

```

4
Start Agents
Execute your script:
Terminal
Copy
```
python app.py

```

You should see:
  * Agent initialization
  * Agents progress
  * Final results
  * Generated report


## 
​
Creating Custom Tool for Agents (Optional)
Tools makes the Agent powerful.
More information about tools can be found in the Tools section.
  * Code
  * No Code


1
Install PraisonAI
Install the core package and duckduckgo_search package:
Terminal
Copy
```
pip install praisonai duckduckgo_search

```

2
Create Tools and Agents
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
from duckduckgo_search import DDGS
from typing import List, Dict
# 1. Tool
def internet_search_tool(query: str) -> List[Dict]:
  """
  Perform Internet Search
  """
  results = []
  ddgs = DDGS()
  for result in ddgs.text(keywords=query, max_results=5):
    results.append({
      "title": result.get("title", ""),
      "url": result.get("href", ""),
      "snippet": result.get("body", "")
    })
  return results
# 2. Agent
data_agent = Agent(
  name="DataCollector",
  role="Search Specialist",
  goal="Perform internet searches to collect relevant information.",
  backstory="Expert in finding and organising internet data.",
  tools=[internet_search_tool],
  self_reflect=False
)
# 3. Tasks
collect_task = Task(
  description="Perform an internet search using the query: 'AI job trends in 2024'. Return results as a list of title, URL, and snippet.",
  expected_output="List of search results with titles, URLs, and snippets.",
  agent=data_agent,
  name="collect_data",
)
# 4. Start Agents
agents = PraisonAIAgents(
  agents=[data_agent],
  tasks=[collect_task],
  process="sequential"
)
agents.start()

```

3
Start Agents
Run your script:
Terminal
Copy
```
python app.py

```

## 
​
Next Steps
## Core Concepts
Learn about agents, tasks, and processes
## API Reference
Explore detailed API documentation
Was this page helpful?
YesNo
InstallationAgents
On this page
  * Basic
  * Advanced
  * Providing Detailed Tasks to Agents (Optional)
  * Creating Custom Tool for Agents (Optional)
  * Next Steps


