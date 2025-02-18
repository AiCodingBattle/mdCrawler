PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Image Generation AI Agents
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


Start
Image Description
Image Agent
Image URL
Image Generation in PraisonAI allows you to create high-quality images using natural language descriptions. The Image Agent supports both synchronous and asynchronous operations, making it flexible for various use cases.
## 
​
Quick Start
  * Code
  * Async


1
Install Package
First, install the PraisonAI Agents package with LLM support:
Copy
```
pip install "praisonaiagents[llm]"

```

2
Set API Key
Set your OpenAI API key as an environment variable:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

3
Create Agent
Create a new file `image_gen.py` with the basic setup:
Copy
```
from praisonaiagents.agent.image_agent import ImageAgent
# Create an image agent
agent = ImageAgent(
  llm="dall-e-3",
  verbose=True
)
# Generate an image
result = agent.chat("A cute baby sea otter playing with a laptop")
print("Image generation result:", result)

```

## 
​
Features
## DALL-E Integration
Seamless integration with DALL-E for high-quality image generation.
## Async Support
Asynchronous operations for better performance in concurrent environments.
## Natural Style
Generate images with natural, realistic styling options.
## Verbose Mode
Detailed output logging for better debugging and monitoring.
## 
​
Next Steps
## Agents Overview
Learn more about PraisonAI Agents and their capabilities
## API Reference
View the complete API documentation
Was this page helpful?
YesNo
AutoAgentsSelf Reflection Agents
On this page
  * Quick Start
  * Features
  * Next Steps


