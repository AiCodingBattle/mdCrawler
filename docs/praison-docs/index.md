PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Praison AI
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


![PraisonAI Logo](https://docs.praison.ai/images/praisonai-logo-black.png)![PraisonAI Logo](https://docs.praison.ai/images/praisonai-logo-light.png)
![Total Downloads](https://static.pepy.tech/badge/PraisonAI)
![GitHub Stars](https://img.shields.io/github/stars/MervinPraison/PraisonAI?style=social)
![GitHub Forks](https://img.shields.io/github/forks/MervinPraison/PraisonAI?style=social)
![MervinPraison/PraisonAI | Trendshift](https://trendshift.io/api/badge/repositories/9130)
## 
​
Key Features
## AI Agents Creation
Automated creation and management of AI agents with self-reflection capabilities
## Framework Integration
Seamless integration with CrewAI and AutoGen frameworks
## LLM Support
Support for 100+ Language Learning Models
## Code Integration
Chat with your entire codebase using advanced context understanding
## Interactive UI
Rich, interactive user interfaces for better control and monitoring
## Configuration
YAML-based configuration for easy setup and customization
## Tool Integration
Custom tool integration for extended functionality
## Search Capability
Internet search using Crawl4AI and Tavily
## 
​
Install
  * Code
  * No Code
  * JavaScript


1
Install Package
Copy
```
pip install praisonaiagents

```

2
Set API Key
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxx

```

3
Create File
Create `app.py` file
## Code Example
Single Agent
Multi Agents
Copy
```
from praisonaiagents import Agent
agent = Agent(instructions="Your are a helpful AI assistant")
agent.start("Write a movie script about a robot in Mars")

```

4
Run Script
Copy
```
python app.py

```

## 
​
AI Agents Flow
📋 Task
🤖 AI Agent
🔧 Tools
📋 Task
🤖 AI Agent
🔧 Tools
▶ Start
⚙ Process
✓ Output
## 
​
AI Agents with Tools
Create AI agents that can use tools to interact with external systems and perform actions.
Agents
Tools
Agent 1
Agent 2
Agent 3
Internet Search
Code Execution
Formatting
Input
Output
## 
​
AI Agents with Memory
Create AI agents with memory capabilities for maintaining context and information across tasks.
Agents
Agent 1
Agent 2
Agent 3
Store
Vector DB
Memory
Short Term
Long Term
Input
Output
## 
​
AI Agents with Different Processes
### 
​
Sequential Process
The simplest form of task execution where tasks are performed one after another.
Agents
Agent 3
Agent 2
Agent 1
Input
Output
### 
​
Hierarchical Process
Uses a manager agent to coordinate task execution and agent assignments.
Agents
Workers
Manager Agent
Worker 1
Worker 2
Worker 3
Input
Output
### 
​
Workflow Process
Advanced process type supporting complex task relationships and conditional execution.
Workflow
Yes
No
Condition
Start
Agent 1
Agent 2
Join
Agent 3
Input
Output
#### 
​
Agentic Routing Workflow
Create AI agents that can dynamically route tasks to specialized LLM instances.
In
LLM Call Router
LLM Call 1
LLM Call 2
LLM Call 3
Out
#### 
​
Agentic Orchestrator Worker
Create AI agents that orchestrate and distribute tasks among specialized workers.
In
LLM Call Router
LLM Call 1
LLM Call 2
LLM Call 3
Synthesizer
Out
#### 
​
Agentic Autonomous Workflow
Create AI agents that can autonomously monitor, act, and adapt based on environment feedback.
ACTION
FEEDBACK
Human
LLM Call
Environment
Stop
#### 
​
Agentic Parallelization
Create AI agents that can execute tasks in parallel for improved performance.
In
LLM Call 2
LLM Call 1
LLM Call 3
Aggregator
Out
#### 
​
Agentic Prompt Chaining
Create AI agents with sequential prompt chaining for complex workflows.
Pass
Output 2
Fail
In
LLM Call 1
Gate
LLM Call 2
LLM Call 3
Out
Exit
#### 
​
Agentic Evaluator Optimizer
Create AI agents that can generate and optimize solutions through iterative feedback.
SOLUTION
ACCEPTED
REJECTED + FEEDBACK
In
LLM Call Generator
LLM Call Evaluator
Out
#### 
​
Repetitive Agents
Create AI agents that can efficiently handle repetitive tasks through automated loops.
Next iteration
Done
Input
Looping Agent
Task
Output
## 
​
Integration Options
Ollama Integration
Copy
```
export OPENAI_BASE_URL=http://localhost:11434/v1

```

Groq Integration
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxx
export OPENAI_BASE_URL=https://api.groq.com/openai/v1

```

Logging Configuration
Copy
```
# Basic logging
export LOGLEVEL=info
# Advanced logging
export LOGLEVEL=debug

```

## 
​
Use Cases
## Customer Service
Build intelligent support agents that can handle customer inquiries and resolve issues autonomously.
## Data Analysis
Create agents that can process, analyze, and derive insights from complex datasets.
## Content Creation
Deploy agents that can generate, edit, and optimize content across various formats.
## Process Automation
Automate complex workflows with intelligent agents that can coordinate and execute tasks.
## 
​
Praison AI Package Overall Features
![PraisonAI Features](https://docs.praison.ai/images/architecture-light.png)![PraisonAI Features](https://docs.praison.ai/images/architecture-dark.png)
PraisonAI Features Overview
## 
​
Features
## Self-Reflection
Agents that evaluate and improve their own responses for higher accuracy
## Reasoning
Multi-step logical reasoning and autonomous problem solving
## CrewAI Framework
Build collaborative AI teams with CrewAI integration
## AutoGen Framework
Create autonomous agent networks using AutoGen
## Multimodal Agents
Work with agents that can process text, images, and other data types
## Train
Train and fine-tune your LLMs for specific tasks and domains. Then use it as an AI Agent.
## 
​
User Interfaces
## Multi Agents UI
Work with CrewAI or AutoGen multi-agent systems
## Chat Interface
Chat with 100+ LLMs using a single AI Agent
## Code Interface
Interact with your entire codebase
Welcome to PraisonAI - Your comprehensive solution for building and managing multi-agent LLM systems with self-reflection capabilities.
![Total Downloads](https://static.pepy.tech/badge/PraisonAI)
![Latest Stable Version](https://img.shields.io/github/v/release/MervinPraison/PraisonAI)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub Stars](https://img.shields.io/github/stars/MervinPraison/PraisonAI?style=social)
![GitHub Forks](https://img.shields.io/github/forks/MervinPraison/PraisonAI?style=social)
## 
​
Video Tutorials
Topic| Video  
---|---  
AI Agents with Self Reflection| ![Self Reflection](https://img.youtube.com/vi/vLXobEN2Vc8/0.jpg)  
Reasoning Data Generating Agent| ![Reasoning Data](https://img.youtube.com/vi/fUT332Y2zA8/0.jpg)  
AI Agents with Reasoning| ![Reasoning](https://img.youtube.com/vi/KNDVWGN3TpM/0.jpg)  
Multimodal AI Agents| ![Multimodal](https://img.youtube.com/vi/hjAWmUT1qqY/0.jpg)  
AI Agents Workflow| ![Workflow](https://img.youtube.com/vi/yWTH44QPl2A/0.jpg)  
Async AI Agents| ![Async](https://img.youtube.com/vi/VhVQfgo00LE/0.jpg)  
Mini AI Agents| ![Mini](https://img.youtube.com/vi/OkvYp5aAGSg/0.jpg)  
AI Agents with Memory| ![Memory](https://img.youtube.com/vi/1hVfVxvPnnQ/0.jpg)  
Repetitive Agents| ![Repetitive](https://img.youtube.com/vi/dAYGxsjDOPg/0.jpg)  
Introduction| ![Introduction](https://img.youtube.com/vi/Fn1lQjC0GO0/0.jpg)  
Tools Overview| ![Tools Overview](https://img.youtube.com/vi/XaQRgRpV7jo/0.jpg)  
Custom Tools| ![Custom Tools](https://img.youtube.com/vi/JSU2Rndh06c/0.jpg)  
Firecrawl Integration| ![Firecrawl](https://img.youtube.com/vi/UoqUDcLcOYo/0.jpg)  
User Interface| ![UI](https://img.youtube.com/vi/tg-ZjNl3OCg/0.jpg)  
Crawl4AI Integration| ![Crawl4AI](https://img.youtube.com/vi/KAvuVUh0XU8/0.jpg)  
Chat Interface| ![Chat](https://img.youtube.com/vi/sw3uDqn2h1Y/0.jpg)  
Code Interface| ![Code](https://img.youtube.com/vi/_5jQayO-MQY/0.jpg)  
Mem0 Integration| ![Mem0](https://img.youtube.com/vi/KIGSgRxf1cY/0.jpg)  
Training| ![Training](https://img.youtube.com/vi/aLawE8kwCrI/0.jpg)  
Realtime Voice Interface| ![Realtime](https://img.youtube.com/vi/frRHfevTCSw/0.jpg)  
Call Interface| ![Call](https://img.youtube.com/vi/m1cwrUG2iAk/0.jpg)  
Reasoning Extract Agents| ![Reasoning Extract](https://img.youtube.com/vi/2PPamsADjJA/0.jpg)  
Was this page helpful?
YesNo
Introduction
On this page
  * Key Features
  * Install
  * AI Agents Flow
  * AI Agents with Tools
  * AI Agents with Memory
  * AI Agents with Different Processes
  * Sequential Process
  * Hierarchical Process
  * Workflow Process
  * Agentic Routing Workflow
  * Agentic Orchestrator Worker
  * Agentic Autonomous Workflow
  * Agentic Parallelization
  * Agentic Prompt Chaining
  * Agentic Evaluator Optimizer
  * Repetitive Agents
  * Integration Options
  * Use Cases
  * Praison AI Package Overall Features
  * Features
  * User Interfaces
  * Video Tutorials


![Total Downloads](https://static.pepy.tech/badge/PraisonAI)
![GitHub Stars](https://img.shields.io/github/stars/MervinPraison/PraisonAI?style=social)
![GitHub Forks](https://img.shields.io/github/forks/MervinPraison/PraisonAI?style=social)
![MervinPraison/PraisonAI | Trendshift](https://trendshift.io/api/badge/repositories/9130)
![Total Downloads](https://static.pepy.tech/badge/PraisonAI)
![Latest Stable Version](https://img.shields.io/github/v/release/MervinPraison/PraisonAI)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub Stars](https://img.shields.io/github/stars/MervinPraison/PraisonAI?style=social)
![GitHub Forks](https://img.shields.io/github/forks/MervinPraison/PraisonAI?style=social)
![PraisonAI Logo](https://docs.praison.ai/images/praisonai-logo-black.png)
![PraisonAI Features](https://docs.praison.ai/images/architecture-light.png)
![Self Reflection](https://img.youtube.com/vi/vLXobEN2Vc8/0.jpg)
![Reasoning Data](https://img.youtube.com/vi/fUT332Y2zA8/0.jpg)
![Reasoning](https://img.youtube.com/vi/KNDVWGN3TpM/0.jpg)
![Multimodal](https://img.youtube.com/vi/hjAWmUT1qqY/0.jpg)
![Workflow](https://img.youtube.com/vi/yWTH44QPl2A/0.jpg)
![Async](https://img.youtube.com/vi/VhVQfgo00LE/0.jpg)
![Mini](https://img.youtube.com/vi/OkvYp5aAGSg/0.jpg)
![Memory](https://img.youtube.com/vi/1hVfVxvPnnQ/0.jpg)
![Repetitive](https://img.youtube.com/vi/dAYGxsjDOPg/0.jpg)
![Introduction](https://img.youtube.com/vi/Fn1lQjC0GO0/0.jpg)
![Tools Overview](https://img.youtube.com/vi/XaQRgRpV7jo/0.jpg)
![Custom Tools](https://img.youtube.com/vi/JSU2Rndh06c/0.jpg)
![Firecrawl](https://img.youtube.com/vi/UoqUDcLcOYo/0.jpg)
![UI](https://img.youtube.com/vi/tg-ZjNl3OCg/0.jpg)
![Crawl4AI](https://img.youtube.com/vi/KAvuVUh0XU8/0.jpg)
![Chat](https://img.youtube.com/vi/sw3uDqn2h1Y/0.jpg)
![Code](https://img.youtube.com/vi/_5jQayO-MQY/0.jpg)
![Mem0](https://img.youtube.com/vi/KIGSgRxf1cY/0.jpg)
![Training](https://img.youtube.com/vi/aLawE8kwCrI/0.jpg)
![Realtime](https://img.youtube.com/vi/frRHfevTCSw/0.jpg)
![Call](https://img.youtube.com/vi/m1cwrUG2iAk/0.jpg)
![Reasoning Extract](https://img.youtube.com/vi/2PPamsADjJA/0.jpg)
