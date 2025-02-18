PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
Integrate with Tools
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
Integrate with Tools
Copy
```
from praisonai import PraisonAI
from duckduckgo_search import DDGS
from praisonai_tools import BaseTool
class InternetSearchTool(BaseTool):
  name: str = "InternetSearchTool"
  description: str = "Search Internet for relevant information based on a query or latest news"
  def _run(self, query: str):
    ddgs = DDGS()
    results = ddgs.text(keywords=query, region='wt-wt', safesearch='moderate', max_results=5)
    return results
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
  tools:
   - "InternetSearchTool"
"""
# Create a PraisonAI instance with the agent_yaml content
praisonai = PraisonAI(agent_yaml=agent_yaml)
# Run PraisonAI
result = praisonai.run()
# Print the result
print(result)

```

Was this page helpful?
YesNo
PraisonAI Package IntegrationGoogle Colab Integration
On this page
  * Integrate with Tools


