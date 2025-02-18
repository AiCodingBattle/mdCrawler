PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Models
OpenAI ChatGPT
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
Add OPENAI ChatGPT to Praison AI
## 
​
Using Single Agent
Copy
```
export OPENAI_API_KEY=xxxxxxxxxx
export OPENAI_MODEL_NAME=gpt-4o

```

### 
​
agents.yaml file
Copy
```
framework: crewai
topic: create movie script about cat in mars
roles:
 researcher:
  backstory: Skilled in finding and organizing information, with a focus on research
   efficiency.
  goal: Gather information about Mars and cats
  role: Researcher
  tasks:
   gather_research:
    description: Research and gather information about Mars, its environment,
     and cats, including their behavior and characteristics.
    expected_output: Document with research findings, including interesting facts
     and information.
  tools:
  - ''

```

You can also mention the model name in the agents.yaml file
### 
​
agents.yaml file
Copy
```
framework: crewai
topic: create movie script about cat in mars
roles:
 researcher:
  backstory: Skilled in finding and organizing information, with a focus on research
   efficiency.
  goal: Gather information about Mars and cats
  role: Researcher
  llm: 
   model: "gpt-4o"
  tasks:
   gather_research:
    description: Research and gather information about Mars, its environment,
     and cats, including their behavior and characteristics.
    expected_output: Document with research findings, including interesting facts
     and information.
  tools:
  - ''

```

## 
​
Using Multi Agents
Copy
```
pip install langchain-openai

```

Copy
```
export OPENAI_API_KEY=xxxxxxxxxx

```

### 
​
agents.yaml file
Copy
```
framework: crewai
topic: create movie script about cat in mars
roles:
 researcher:
  backstory: Skilled in finding and organizing information, with a focus on research
   efficiency.
  goal: Gather information about Mars and cats
  role: Researcher
  llm: 
   model: "openai/gpt-4o"
  tasks:
   gather_research:
    description: Research and gather information about Mars, its environment,
     and cats, including their behavior and characteristics.
    expected_output: Document with research findings, including interesting facts
     and information.
  tools:
  - ''

```

PraisonAI Chat| PraisonAI Code| PraisonAI (Multi-Agents)  
---|---|---  
Litellm| Litellm| Models  
Was this page helpful?
YesNo
Models in PraisonAIOllama
On this page
  * Add OPENAI ChatGPT to Praison AI
  * Using Single Agent
  * agents.yaml file
  * agents.yaml file
  * Using Multi Agents
  * agents.yaml file


