PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Getting Started (No Code)
TL;DR
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
Quick Start with PraisonAI Agents
Copy
```
# Install with CrewAI support
pip install praisonai
# Set your API key
export OPENAI_API_KEY="Enter your API key"
# Initialize and run
praisonai --init "create a movie script about dog in moon"
praisonai

```

## 
​
Quick Start with CrewAI
Copy
```
# Install with CrewAI support
pip install "praisonai[crewai]"
# Set your API key
export OPENAI_API_KEY="Enter your API key"
# Initialize and run
praisonai --framework crewai --init "create a movie script about dog in moon"
praisonai --framework crewai

```

## 
​
Quick Start with AutoGen
Copy
```
# Install with AutoGen support
pip install "praisonai[autogen]"
# Set your API key
export OPENAI_API_KEY="Enter your API key"
# Initialize and run
praisonai --framework autogen --init "create a movie script about dog in moon"
praisonai --framework autogen

```

## 
​
User Interface
Copy
```
# Install UI support
pip install "praisonai[ui]"
# Set up environment
export OPENAI_API_KEY="Enter your API key"
chainlit create-secret
export CHAINLIT_AUTH_SECRET=xxxxxxxx
# Run UI
praisonai ui

```

Was this page helpful?
YesNo
IntroductionInstallation
On this page
  * Quick Start with PraisonAI Agents
  * Quick Start with CrewAI
  * Quick Start with AutoGen
  * User Interface


