PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
API Reference
Process Module
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
Module praisonaiagents.process.process
## 
​
Classes
### 
​
Process
The main class for handling task execution processes in different modes (sequential, hierarchical, workflow).
#### 
​
Parameters
  * `tasks: Dict[str, Task]` - Dictionary of tasks to be executed
  * `agents: List[Agent]` - List of available agents
  * `manager_llm: Optional[str] = None` - Language model for manager agent in hierarchical process
  * `verbose: bool = False` - Enable verbose logging


#### 
​
Methods
  * `workflow(self)` - Execute tasks in a workflow pattern with support for loops and conditions
  * `sequential(self)` - Execute tasks in sequential order
  * `hierarchical(self)` - Execute tasks in hierarchical order with a manager agent


#### 
​
Async Methods
  * `aworkflow(self) -> AsyncGenerator[str, None]` - Async version of workflow process
  * `asequential(self) -> AsyncGenerator[str, None]` - Async version of sequential process
  * `ahierarchical(self) -> AsyncGenerator[str, None]` - Async version of hierarchical process


#### 
​
Async Process Support
Each process type has an async counterpart that supports non-blocking execution:
Copy
```
class Process:
  async def aworkflow(self):
    """Async workflow process execution"""
    # Async workflow implementation
    
  async def asequential(self):
    """Async sequential process execution"""
    # Async sequential implementation
    
  async def ahierarchical(self):
    """Async hierarchical process execution"""
    # Async hierarchical implementation

```

Example usage:
Copy
```
# Create process instance
process = Process(tasks=tasks, agents=agents)
# Use async workflow
async for task_id in process.aworkflow():
  # Handle task execution
  if tasks[task_id].async_execution:
    await handle_async_task(task_id)
  else:
    handle_sync_task(task_id)

```

#### 
​
Async Process Features
  * Non-blocking task execution
  * Parallel task processing
  * Mixed sync/async task support
  * Efficient resource utilization
  * Async manager coordination (hierarchical)
  * Dynamic task scheduling (workflow)


### 
​
LoopItems
A Pydantic model for handling loop data in workflow process.
#### 
​
Parameters
  * `items: List[Any]` - List of items to be processed in a loop


## 
​
Process Types
### 
​
Sequential Process
  * Tasks are executed one after another in a linear fashion
  * Each task is completed before moving to the next one
  * Simplest form of task execution


### 
​
Hierarchical Process
  * Uses a manager agent to coordinate task execution
  * Manager decides task order and agent assignments
  * Provides more complex task orchestration
  * Requires manager_llm parameter
  * Supports dynamic agent assignment


### 
​
Workflow Process
  * Supports complex task relationships
  * Features: 
    * Task dependencies
    * Conditional execution
    * Loops
    * Context sharing between tasks
  * Maintains task state and relationships
  * Handles data flow between tasks


Was this page helpful?
YesNo
Task Module
On this page
  * Module praisonaiagents.process.process
  * Classes
  * Process
  * Parameters
  * Methods
  * Async Methods
  * Async Process Support
  * Async Process Features
  * LoopItems
  * Parameters
  * Process Types
  * Sequential Process
  * Hierarchical Process
  * Workflow Process


