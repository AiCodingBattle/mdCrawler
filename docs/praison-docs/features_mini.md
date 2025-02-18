PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Mini AI Agents
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
Create multiple AI agents that can work together in just a few lines of code!
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
Create Your Agents
Single Agent
Multiple Agents
Copy
```
from praisonaiagents import Agent, PraisonAIAgents
summarise_agent = Agent(instructions="Summarise Photosynthesis")
agents = PraisonAIAgents(agents=[summarise_agent])
agents.start()

```

4
Run Your Agents
Execute your agents by running:
Copy
```
python app.py

```

**Prerequisites**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.


## 
​
Understanding Mini AI Agents
## What are Mini AI Agents?
Mini AI Agents are simplified yet powerful AI agents that can:
  * Work together to accomplish tasks
  * Use tools like internet search
  * Process and summarize information
  * Execute tasks sequentially


## 
​
Key Components
## Agent
Individual AI agents with specific roles and capabilities
Copy
```
Agent(instructions="Your agent's role description")

```

## Tools
Built-in tools that agents can use
Copy
```
tools=[Tools.internet_search]

```

## Agents Manager
Coordinates multiple agents
Copy
```
Agents(agents=[agent1, agent2])

```

## Sequential Flow
Agents work in sequence, passing results to each other
## 
​
Available Tools
## Internet Search
Copy
```
Tools.internet_search

```

Search the internet using DuckDuckGo
Requires: `pip install duckduckgo_search`
## 
​
Custom Instructions
Basic
Advanced
Copy
```
# Simple instructions
research_agent = Agent(
  instructions="Research about climate change"
)

```

## 
​
Best Practices
Agent Instructions
Write clear and specific instructions:
Copy
```
# Good
Agent(instructions="Research and analyze the latest AI developments in 2024")
# Too vague
Agent(instructions="Research AI")

```

Tool Usage
Provide tools only to agents that need them:
Copy
```
# Research agent needs search
research_agent = Agent(
  instructions="Research AI",
  tools=[Tools.internet_search]
)
# Summary agent doesn't need search
summary_agent = Agent(
  instructions="Summarize findings"
)

```

## 
​
Common Patterns
### 
​
Research and Analysis
Copy
```
# Research agent
researcher = Agent(
  instructions="Research latest developments in quantum computing",
  tools=[Tools.internet_search]
)
# Analysis agent
analyst = Agent(
  instructions="Analyze and explain the research findings in simple terms"
)
agents = Agents(agents=[researcher, analyst])

```

### 
​
Information Processing
Copy
```
# Data collector
collector = Agent(
  instructions="Collect information about renewable energy",
  tools=[Tools.internet_search]
)
# Summarizer
summarizer = Agent(
  instructions="Create a concise summary of the collected information"
)
# Report writer
writer = Agent(
  instructions="Write a detailed report based on the summary"
)
agents = Agents(agents=[collector, summarizer, writer])

```

## 
​
Troubleshooting
## Tool Not Available
If using `Tools.internet_search`, install required package:
Copy
```
pip install duckduckgo_search

```

## Agent Communication
Ensure agent instructions are clear and complementary
## 
​
Next Steps
## Advanced Agents
Learn about advanced agent configurations
## Custom Tools
Create your own agent tools
Mini AI Agents are designed to be simple yet powerful. They’re perfect for quick prototypes and straightforward automation tasks.
Was this page helpful?
YesNo
Async AgentsGenerate Reasoning Data
On this page
  * Quick Start
  * Understanding Mini AI Agents
  * Key Components
  * Available Tools
  * Custom Instructions
  * Best Practices
  * Common Patterns
  * Research and Analysis
  * Information Processing
  * Troubleshooting
  * Next Steps


