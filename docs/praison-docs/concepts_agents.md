PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Core Concepts
Agents
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
Understanding Agents
Agents are the core building blocks of PraisonAI. Each agent is an autonomous AI entity with specific roles, goals, and capabilities.
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
Key Components
## Role & Goal
Defines the agent’s purpose and objectives through role definition and specific goals
## Capabilities
Tools and functions available to the agent for task execution
## Memory
Context retention and learning capabilities across interactions
## Language Model
The underlying AI model powering the agent’s intelligence
## 
​
Component Details
### 
​
Role and Goal
Clear role and goal definitions are crucial for optimal agent performance.
Component| Description| Example  
---|---|---  
**Role**|  Agent’s function and expertise| Research Analyst, Code Developer  
**Goal**|  Specific objectives to achieve| Analyze market trends, Generate reports  
**Backstory**|  Contextual background| Expert with 10 years of experience  
### 
​
Capabilities
Basic
Copy
```
agent = Agent(
  name="Researcher",
  role="Senior Research Analyst",
  goal="Uncover cutting-edge developments in AI",
  backstory="You are an expert at a technology research group",
  verbose=True,
  llm="gpt-4o",
  markdown=True
)

```

1
Install PraisonAI
Install the core package:
Terminal
Copy
```
pip install praisonaiagents

```

2
Configure Environment
Terminal
Copy
```
export OPENAI_API_KEY=your_openai_key

```

Generate your OpenAI API key from OpenAI Use other LLM providers like Ollama, Anthropic, Groq, Google, etc. Please refer to the Models for more information.
3
Create Agent
Create `app.py`:
Single Agent
Multi Agents
Copy
```
from praisonaiagents import Agent
agent = Agent(instructions="Your are a helpful AI assistant")
agent.start("Write a movie script about a robot in Mars")

```

4
Start Agents
Execute your script:
Terminal
Copy
```
python app.py

```

You should see:
  * Agent initialization
  * Agents progress
  * Final results
  * Generated report


## 
​
Agent Types
## Basic Agent
Overview
Perfect for straightforward tasks and direct interactions
Features
  * Single-purpose focus
  * Direct user interaction
  * Limited tool set
  * Ideal for simple tasks


## Specialized Agent
Overview
Experts in specific domains with advanced capabilities
Features
  * Domain expertise
  * Advanced capabilities
  * Custom tools
  * Deep knowledge base


## Collaborative Agent
Overview
Designed for team-based operations and complex workflows
Features
  * Team interaction
  * Task delegation
  * Shared context
  * Coordinated actions


## 
​
Best Practices
Always implement proper error handling and resource management in your agent configurations.
## Agent Design
1
Role Definition
Define clear, specific roles for each agent
2
Goal Setting
Set specific, measurable goals
3
Tool Selection
Choose relevant tools for the task
4
Memory Setup
Configure appropriate memory settings
## Agent Interaction
1
Communication
Establish clear communication protocols
2
Delegation
Define explicit delegation rules
3
Error Handling
Implement robust error handling
4
Resource Management
Set up efficient resource allocation
## 
​
Async Capabilities
## Key Features
  * Async Support
  * Parallel Execution
  * Integration


Copy
```
async def main():
  agent = Agent(name="AsyncAgent")
  result = await agent.aprocess_task()

```

  * Full async/await support
  * Non-blocking operations
  * Enhanced performance


## 
​
Advanced Features
## Memory Management
  * Short-term conversation memory
  * Long-term knowledge retention
  * Context preservation


## Tool Integration
  * Custom tool development
  * External API integration
  * Resource access control


## 
​
Async Support
Agents now support asynchronous operations through the following methods:
  * `achat`: Async version of the chat method
  * `astart`: Async version of start method
  * `aexecute_task`: Async version of execute_task method
  * `arun_task`: Async version of run_task method
  * `arun_all_tasks`: Async version of run_all_tasks method


### 
​
Example Usage:
Copy
```
import asyncio
from praisonaiagents import Agent, Task, PraisonAIAgents
async def main():
  # Create an async agent
  async_agent = Agent(
    name="AsyncAgent",
    role="Async Task Specialist",
    goal="Perform async operations",
    backstory="Expert in async operations",
    tools=[async_search_tool], # Your async tool
    verbose=True
  )
  # Create an async task
  async_task = Task(
    description="Perform async operation",
    expected_output="Async result",
    agent=async_agent,
    async_execution=True # Enable async execution
  )
  # Create and start agents with async support
  agents = PraisonAIAgents(
    agents=[async_agent],
    tasks=[async_task],
    verbose=True
  )
  
  # Start async execution
  result = await agents.astart()
  print(result)
# Run the async main function
if __name__ == "__main__":
  asyncio.run(main())

```

### 
​
Key Features:
  * Full async/await support
  * Parallel task execution
  * Async tool integration
  * Async callback support
  * Mixed sync/async operations


## 
​
Next Steps
## Create Your First Agent
Follow our quickstart guide to create your first agent
## API Reference
Explore the complete Agent API documentation
Was this page helpful?
YesNo
Quick StartTasks
On this page
  * Understanding Agents
  * Key Components
  * Component Details
  * Role and Goal
  * Capabilities
  * Agent Types
  * Best Practices
  * Async Capabilities
  * Advanced Features
  * Async Support
  * Example Usage:
  * Key Features:
  * Next Steps


