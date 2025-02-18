PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
PraisonAI Package Integration
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
Include praisonai package in your project
## 
​
Option 1: Using RAW YAML
Copy
```
from praisonai import PraisonAI
# Example agent_yaml content
agent_yaml = """
framework: "crewai"
topic: "Space Exploration"
roles:
 astronomer:
  role: "Space Researcher"
  goal: "Discover new insights about {topic}"
  backstory: "You are a curious and dedicated astronomer with a passion for unraveling the mysteries of the cosmos."
  tasks:
   investigate_exoplanets:
    description: "Research and compile information about exoplanets discovered in the last decade."
    expected_output: "A summarized report on exoplanet discoveries, including their size, potential habitability, and distance from Earth."
"""
# Create a PraisonAI instance with the agent_yaml content
praisonai = PraisonAI(agent_yaml=agent_yaml)
# Run PraisonAI
result = praisonai.run()
# Print the result
print(result)

```

## 
​
Option 2: Using separate agents.yaml file
Note: Please create agents.yaml file before hand.
Copy
```
from praisonai import PraisonAI
def basic(): # Basic Mode
  praisonai = PraisonAI(agent_file="agents.yaml")
  praisonai.run()
if __name__ == "__main__":
  basic()

```

## 
​
Other options
Copy
```
from praisonai import PraisonAI
def basic(): # Basic Mode
  praisonai = PraisonAI(agent_file="agents.yaml")
  praisonai.run()
  
def advanced(): # Advanced Mode with options
  praisonai = PraisonAI(
    agent_file="agents.yaml",
    framework="autogen",
  )
  praisonai.run()
  
def auto(): # Full Automatic Mode
  praisonai = PraisonAI(
    auto="Create a movie script about car in mars",
    framework="autogen"
  )
  print(praisonai.framework)
  praisonai.run()
if __name__ == "__main__":
  basic()
  advanced()
  auto()

```

Was this page helpful?
YesNo
Agents PlaybookIntegrate with Tools
On this page
  * Include praisonai package in your project
  * Option 1: Using RAW YAML
  * Option 2: Using separate agents.yaml file
  * Other options


