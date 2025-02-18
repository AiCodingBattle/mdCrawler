PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Models
Google Gemini Agents
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
Google API
Gemini
Basic Agent
Multi-Agents
No-Code
Output
Output
Output
## 
​
Prerequisites
1
Install Package
First, install PraisonAI Agents:
Copy
```
pip install "praisonaiagents[llm]"

```

praisonaiagents[llm] includes all Google Gemini dependencies. For No-Code implementation, also install: pip install langchain-google-genai
2
Set API Key
Set your Gemini API key:
Copy
```
export GEMINI_API_KEY=xxxxxxxxxxx

```

3
Code
Copy
```
from praisonaiagents import Agent
agent = Agent(
  instructions="You are a helpful assistant",
  llm="gemini/gemini-1.5-flash-8b",
  self_reflect=True,
  verbose=True
)
agent.start("Why sky is Blue?")

```

## 
​
Code Implementation
### 
​
Basic Usage
The simplest way to use Gemini with PraisonAI Agents:
Copy
```
from praisonaiagents import Agent
agent = Agent(
  instructions="You are a helpful assistant",
  llm="gemini/gemini-1.5-flash-8b",
  self_reflect=True,
  verbose=True
)
agent.start("Why sky is Blue?")

```

### 
​
Multi-Agent Setup
Create multiple agents working together:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
agent = Agent(
  instructions="You are a helpful assistant",
  llm="gemini/gemini-1.5-flash-8b",
  self_reflect=True,
  verbose=True
)
task = Task(
  description="Why sky is Blue?",
  agent=agent,
)
agents = PraisonAIAgents(
 agents=[agent],
 tasks=[task],
)
agents.start()

```

This uses Litellm to connect to Google Gemini.
## 
​
Gemini 2.0 Flash Thinking
### 
​
LLM Configuration
Copy
```
llm_config = {
 "model": "gemini/gemini-2.0-flash-thinking-exp-01-21",
 "response_format": {"type": "text"} # type is text, because json_object is not supported
}

```

1
Install Package
Install required packages:
Copy
```
pip install "praisonaiagents[llm]"

```

2
Set API Key
Set your Gemini API key:
Copy
```
export GEMINI_API_KEY=xxxxxxxxxxx

```

3
Code
Copy
```
from praisonaiagents import Agent
llm_config = {"model": "gemini/gemini-2.0-flash-thinking-exp-01-21","response_format": {"type": "text"}}
agent = Agent(
  instructions="You are a helpful assistant",
  llm=llm_config
)
result = agent.start("Why sky is Blue?")
print(result)

```

## 
​
Alternative Setup
### 
​
Using Environment Variables
Google Gemini
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxx
export OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/

```

## 
​
No-Code Implementation
### 
​
Setup
Copy
```
pip install langchain-google-genai
export GOOGLE_API_KEY=xxxxxxxxxx

```

### 
​
YAML Configuration
Create an `agents.yaml` file:
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
   model: "google/gemini-1.5-flash-001"
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
Additional Resources
PraisonAI Chat| PraisonAI Code| PraisonAI (Multi-Agents)  
---|---|---  
Litellm| Litellm| Models  
Was this page helpful?
YesNo
GroqOpenRouter
On this page
  * Prerequisites
  * Code Implementation
  * Basic Usage
  * Multi-Agent Setup
  * Gemini 2.0 Flash Thinking
  * LLM Configuration
  * Alternative Setup
  * Using Environment Variables
  * No-Code Implementation
  * Setup
  * YAML Configuration
  * Additional Resources


