PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Getting Started (No Code)
Auto Generation Mode
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


PraisonAI supports automatic agent generation with PraisonAI Agents, CrewAI and AutoGen frameworks.
## 
​
Installation
Choose your preferred framework:
Copy
```
# For PraisonAI Agents
pip install praisonai
# For CrewAI
pip install "praisonai[crewai]"
# For AutoGen
pip install "praisonai[autogen]"
# For both frameworks
pip install "praisonai[crewai,autogen]"

```

## 
​
Usage
### 
​
With PraisonAI Agents
Copy
```
praisonai --auto "create a movie script about Dog in Moon"

```

### 
​
With CrewAI
Copy
```
praisonai --framework crewai --auto "create a movie script about Dog in Moon"

```

### 
​
With AutoGen
Copy
```
praisonai --framework autogen --auto "create a movie script about Dog in Moon"

```

## 
​
Framework-specific Features
### 
​
CrewAI
  * Task delegation capabilities
  * Sequential and parallel task execution
  * Built-in tools integration
  * Structured agent-task relationships


### 
​
AutoGen
  * Multi-agent conversation capabilities
  * Code execution environment
  * Built-in tools integration
  * Flexible agent interactions


Copy
```
praisonai --auto "create a movie script about Dog in Moon"

```

Was this page helpful?
YesNo
RunAPI Reference
On this page
  * Installation
  * Usage
  * With PraisonAI Agents
  * With CrewAI
  * With AutoGen
  * Framework-specific Features
  * CrewAI
  * AutoGen


