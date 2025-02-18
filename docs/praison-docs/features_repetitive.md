PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Workflows
Repetitive Agents
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


Next iteration
Done
Input
Looping Agent
Task
Output
A workflow optimization pattern where agents handle repetitive tasks through automated loops, processing multiple instances efficiently while maintaining consistency.
## 
​
Quick Start
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
Create a new file `repetitive_agent.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
agent = Agent(
  instructions="You are a loop agent that creating a loop of tasks."
)
task = Task(
  description="Create the list of tasks to be looped through.",
  agent=agent,
  task_type="loop",
  input_file="tasks.csv"
)
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  process="workflow",
  max_iter=30
)
agents.start()

```

4
Start Agents
Type this in your terminal to run your agents:
Copy
```
python repetitive_agent.py

```

**Requirements**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.


## 
​
Understanding Repetitive Agents
## What are Repetitive Agents?
Repetitive agents enable:
  * Automated task loops
  * Batch processing
  * Consistent task execution
  * Efficient handling of multiple similar tasks


## 
​
Features
## Task Looping
Process multiple tasks through automated loops.
## Batch Processing
Handle multiple similar tasks efficiently.
## Input Management
Process tasks from structured input files.
## Progress Tracking
Monitor task completion and progress.
## 
​
Troubleshooting
## Loop Issues
If loops aren’t working as expected:
  * Verify input file format
  * Check task configurations
  * Enable verbose mode for debugging


## Performance Issues
If processing is slow:
  * Check batch sizes
  * Verify resource allocation
  * Monitor memory usage


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your input files are properly formatted and your task configurations are appropriate for your use case.
Was this page helpful?
YesNo
Evaluator OptimizerCLI
On this page
  * Quick Start
  * Understanding Repetitive Agents
  * Features
  * Troubleshooting
  * Next Steps


