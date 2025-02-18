PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Command Line Interface
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


🚀
CLI Command
AI Agent
Config/YAML
🏁
PraisonAI CLI provides a simple way to interact with AI agents directly from your terminal. You can run quick commands, specify LLM options, or use YAML configuration files for more complex scenarios.
![PraisonAI CLI Demo](https://docs.praison.ai/demo/praisonai-cli-demo.gif)
## 
​
Quick Start
1
Install Package
Install the PraisonAI package:
Copy
```
pip install praisonai

```

2
Set API Key
Set your OpenAI API key as an environment variable:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

## 
​
Usage Examples
Simple Command
Run a simple command directly:
Copy
```
praisonai "write a movie script in 3 lines"

```

With LLM Option
Specify a different LLM model:
Copy
```
praisonai "write a movie script in 3 lines" --llm gpt-4o-mini

```

Using YAML Config
Run agents defined in a YAML file:
Copy
```
praisonai agents.yaml

```

## 
​
Configuration
  * Create Config
  * Auto Mode


Initialize a new agents.yaml file for your project:
Copy
```
praisonai --init "Create a movie script about AI"

```

This will create an `agents.yaml` file with predefined configuration for your task.
## 
​
Features
## Simple Commands
Run AI tasks directly from your terminal with simple commands.
## LLM Options
Choose from different LLM models for your specific needs.
## YAML Support
Use YAML files for complex agent configurations and workflows.
## Auto Configuration
Automatic agent setup based on task requirements.
## 
​
Next Steps
## YAML Configuration
Learn more about YAML configuration options
## API Reference
View the complete API documentation
Was this page helpful?
YesNo
Repetitive AgentsAutoAgents
On this page
  * Quick Start
  * Usage Examples
  * Configuration
  * Features
  * Next Steps


