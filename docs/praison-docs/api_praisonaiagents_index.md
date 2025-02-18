PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
API Reference
API Reference
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


## Agent
Documentation for individual AI agents and their capabilities
## Agents
Documentation for managing multiple agents and their interactions
## Task
Documentation for defining and managing tasks
## Process
Documentation for handling task execution flows
# 
​
Module praisonaiagents
## 
​
Sub-modules
  * praisonaiagents.agent - Agent module for defining individual AI agents
  * praisonaiagents.agents - Agents module for managing multiple agents
  * praisonaiagents.task - Task module for defining and managing tasks
  * praisonaiagents.process - Process module for handling task execution flows
  * praisonaiagents.main - Main module containing utility functions


## 
​
Functions
### 
​
clean_triple_backticks(text: str) → str
Clean triple backticks from text output.
### 
​
display_error(message: str, console=None)
Display error messages in the console.
### 
​
display_generating(content: str = ”, start_time: float | None = None)
Display generation status with optional timing information.
### 
​
display_instruction(message: str, console=None)
Display instruction messages in the console.
### 
​
display_interaction(message, response, markdown=True, generation_time=None, console=None)
Display interaction between user and agent.
### 
​
display_self_reflection(message: str, console=None)
Display agent self-reflection messages.
### 
​
display_tool_call(message: str, console=None)
Display tool call messages.
Was this page helpful?
YesNo
Auto Generation ModeAgent Module
On this page
  * Module praisonaiagents
  * Sub-modules
  * Functions
  * clean_triple_backticks(text: str) → str
  * display_error(message: str, console=None)
  * display_generating(content: str = ”, start_time: float | None = None)
  * display_instruction(message: str, console=None)
  * display_interaction(message, response, markdown=True, generation_time=None, console=None)
  * display_self_reflection(message: str, console=None)
  * display_tool_call(message: str, console=None)


