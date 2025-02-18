PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Reasoning Extract Agents
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


Input
Reasoning Agent
Reasoning Steps
Small Agent
Output
A workflow where a reasoning agent breaks down complex problems into steps, followed by a smaller agent that processes these steps to provide concise answers.
## 
​
Prerequisites
1
Install Package
Install required packages:
Copy
```
pip install "praisonaiagents[llm]"

```

praisonaiagents[llm] includes all necessary dependencies for reasoning agents
2
Set API Key
Configure your API key:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

3
Create File
Create a new file called `app.py` and add the following code:
4
Run Application
Execute the script:
Copy
```
python app.py

```

## 
​
Code
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
reasoning_agent = Agent(
  role="Helpful Assistant", 
  reasoning_steps=True, 
  llm="deepseek/deepseek-reasoner"
)
small_agent = Agent(
  role="Helpful Assistant", 
  llm="gpt-3.5-turbo"
)
reasoning_task = Task(
  description="How many r's in the word 'Strawberry'?", 
  agent=reasoning_agent
)
small_task = Task(
  description="With the provided reasoning tell me how many r's in the word 'Strawberry'?", 
  agent=small_agent
)
agents = PraisonAIAgents(
  agents=[reasoning_agent, small_agent],
  tasks=[reasoning_task, small_task]
)
agents.start()

```

## 
​
Features
## Step-by-Step Reasoning
Break down complex problems into logical steps.
## Multi-Agent Collaboration
Combine reasoning and processing agents.
## Flexible Models
Use different models for reasoning and processing.
## Task Chaining
Connect reasoning output to processing tasks.
## 
​
Understanding Reasoning Agents
## What are Reasoning Agents?
Reasoning agents enable:
  * Detailed step-by-step analysis
  * Logical problem decomposition
  * Clear reasoning paths
  * Enhanced decision making


## 
​
Troubleshooting
## Reasoning Issues
If reasoning steps aren’t clear:
  * Check reasoning_steps parameter
  * Verify model compatibility
  * Review task descriptions


## Agent Communication
If agents aren’t coordinating:
  * Ensure task order is correct
  * Check task dependencies
  * Verify agent configurations


The reasoning agent uses a specialized model (deepseek-reasoner) optimized for step-by-step analysis, while the small agent can use a more general-purpose model for processing the reasoning output.
Was this page helpful?
YesNo
RAG AgentsReasoning Agents
On this page
  * Prerequisites
  * Code
  * Features
  * Understanding Reasoning Agents
  * Troubleshooting


