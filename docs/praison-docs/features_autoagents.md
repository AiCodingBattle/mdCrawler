PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
AutoAgents
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


Execution
Automatic Tool Assignment
Automatic Agent Creation
AI Agent 2
AI Agent 1
AI Agent 3
Tools 1
Tools 2
Tools 3
AI Agent 1
Plan Tasks
AI Agent 2
AI Agent 3
In
Out
AutoAgents automatically creates and manages AI agents and tasks based on high-level instructions.
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
pip install praisonaiagents duckduckgo_search

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
from praisonaiagents import AutoAgents
from praisonaiagents.tools import duckduckgo
# Create AutoAgents instance
agents = AutoAgents(
  instructions="Search for information about AI Agents",
  tools=[duckduckgo],
  process="sequential",
  verbose=True,
  max_agents=3 # Maximum number of agents to create
)
# Start the agents
result = agents.start()
print(result)

```

4
Start AutoAgents
Run your AutoAgents:
Copy
```
python app.py

```

**Requirements**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.


## 
​
Understanding AutoAgents
## What are AutoAgents?
AutoAgents automatically:
  * Creates appropriate AI agents based on your instructions
  * Assigns relevant tools to each agent
  * Breaks down tasks into manageable steps
  * Manages execution flow between agents
  * Handles agent coordination and task delegation


## 
​
Features
## Automatic Agent Creation
Creates specialized agents based on task requirements.
## Smart Tool Assignment
Automatically assigns relevant tools to each agent.
## Task Management
Breaks down complex tasks into manageable steps.
## Process Optimization
Chooses optimal execution process (sequential/hierarchical).
Basic
Advanced
Copy
```
# Basic usage with default settings
agents = AutoAgents(
  instructions="Your high-level task description",
  tools=[tool1, tool2]
)

```

## 
​
Advanced Usage
### 
​
Configuration Options
Copy
```

# Create AutoAgents with advanced configuration
agents = AutoAgents(
  instructions="Research and summarize recent AI developments",
  tools=[SerperDevTool, WikipediaTools],
  max_agents=3, # Maximum number of agents to create
  verbose=True, # Enable detailed logging
  process="hierarchical", # Use hierarchical process
  memory=True, # Enable memory for agents
  allow_delegation=True, # Allow task delegation
  max_rpm=60, # Maximum requests per minute
  max_execution_time=300, # Maximum execution time in seconds
  allow_code_execution=True, # Allow code execution
  code_execution_mode="safe", # Use safe mode for code execution
  self_reflect=True, # Enable agent self-reflection
  markdown=True # Enable markdown formatting
)

```

### 
​
Process Types
Sequential Process
Copy
```
# Tasks are executed in sequence
agents = AutoAgents(
  instructions="Your task",
  process="sequential"
)

```

Hierarchical Process
Copy
```
# Manager agent coordinates other agents
agents = AutoAgents(
  instructions="Your task",
  process="hierarchical",
  manager_llm="gpt-4o" # Specify LLM for manager
)

```

## 
​
Best Practices
Clear Instructions
Copy
```
# Good instruction example
agents = AutoAgents(
  instructions="""
  Research the latest developments in AI for 2024:
  1. Focus on breakthrough technologies
  2. Include real-world applications
  3. Consider future implications
  """
)

```

Tool Selection
Copy
```
# Provide relevant tools for the task
agents = AutoAgents(
  instructions="Research task",
  tools=[
    SerperDevTool, # For web search
    WikipediaTools, # For background info
    CustomTool # Your custom tool
  ]
)

```

Resource Management
Copy
```
# Configure resource limits
agents = AutoAgents(
  instructions="Your task",
  max_rpm=60, # Rate limiting
  max_execution_time=300, # Timeout
  max_agents=3 # Agent limit
)

```

## 
​
Troubleshooting
## Tool Assignment Issues
If tools aren’t being assigned correctly:
  * Check tool compatibility
  * Verify tool names
  * Enable verbose mode for debugging


## Performance Issues
If execution is slow:
  * Reduce max_agents
  * Adjust max_rpm
  * Consider process type


## 
​
API Reference
### 
​
Main Parameters
instructions
str
required
High-level task description for the agents
tools
List[Any]
List of tools available to the agents
max_agents
int
default: "3"
Maximum number of agents to create
process
str
default: "sequential"
Process type: “sequential” or “hierarchical”
### 
​
Optional Parameters
verbose
bool
default: "False"
Enable detailed logging
memory
bool
default: "True"
Enable agent memory
allow_delegation
bool
default: "False"
Allow agents to delegate tasks
### 
​
Methods
start()
method
Start the agents synchronously
astart()
method
Start the agents asynchronously
## 
​
Next Steps
## Examples
Explore more examples in our examples directory
## Custom Tools
Learn how to create custom tools for your agents
For optimal results, provide clear instructions and appropriate tools for your use case.
Was this page helpful?
YesNo
CLIImage Generation
On this page
  * Quick Start
  * Understanding AutoAgents
  * Features
  * Advanced Usage
  * Configuration Options
  * Process Types
  * Best Practices
  * Troubleshooting
  * API Reference
  * Main Parameters
  * Optional Parameters
  * Methods
  * Next Steps


