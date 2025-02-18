PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Getting Started
Introduction
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
What is PraisonAI?
PraisonAI is a powerful Multi-Agent Framework for building and deploying AI agents that can understand, reason, and execute complex tasks autonomously.
## Welcome to PraisonAI
Build powerful autonomous agents that understand, decide, and execute with unprecedented capability.
# 
​
Core Components
📋 Task
🤖 AI Agent
🔧 Tools
📋 Task
🤖 AI Agent
🔧 Tools
▶ Start
⚙ Process
✓ Output
## Agents
Autonomous AI entities that can understand context and execute tasks
## Tasks
Units of work that agents can execute independently or collaboratively
## Process
Workflow management for coordinating agent activities
## Tools
Extensible capabilities that agents can leverage
## 
​
Use Cases
## Customer Service
Build intelligent support agents that can handle customer inquiries and resolve issues autonomously.
## Data Analysis
Create agents that can process, analyze, and derive insights from complex datasets.
## Content Creation
Deploy agents that can generate, edit, and optimize content across various formats.
## Process Automation
Automate complex workflows with intelligent agents that can coordinate and execute tasks.
## 
​
Getting Started is Easy
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
## 
​
Key Features
## Autonomous Agents
Create intelligent agents that can:
  * Understand natural language instructions
  * Make decisions based on context
  * Execute complex tasks autonomously


## Flexible Architecture
Build with:
  * Modular components
  * Extensible tools
  * Customizable workflows


## Advanced Capabilities
Leverage:
  * Multi-agent collaboration
  * Memory and context management
  * Tool integration


## Why Choose PraisonAI?
## Developer First
Build with modern tools and frameworks you already love. Our SDK is designed to be intuitive and powerful.
## Production Ready
Enterprise-grade reliability with built-in security features and scalable architecture.
## Open Source
PraisonAI is open source and available on GitHub.
## Low Code User Friendly
PraisonAI is designed to be easy to learn and use for non technical users.
## 
​
Chat with One Agent
  * Basic Agent
  * Agent with Tools


1
Install PraisonAI
Get started with a simple pip install:
Copy
```
pip install praisonaiagents

```

2
Initialize Your Agent
Create your first autonomous agent in just a few lines:
Copy
```
from praisonaiagents import Agent
agent = Agent(instructions="Your are a helpful AI assistant")
agent.chat("Write a movie script about a robot in Mars")

```

3
Build Amazing Things
Start building powerful AI applications with autonomous capabilities!
## 
​
Next Steps
## Installation
Complete installation guide and setup instructions
## Quick Start
Build your first AI agent in minutes
Join our community on Discord to connect with other developers and get help!
Was this page helpful?
YesNo
HomeInstallation
On this page
  * What is PraisonAI?
  * Core Components
  * Use Cases
  * Getting Started is Easy
  * Key Features
  * Chat with One Agent
  * Next Steps


