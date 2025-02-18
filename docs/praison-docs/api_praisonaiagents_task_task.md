PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
API Reference
Task Module
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
Module praisonaiagents.task.task
## 
​
Classes
### 
​
Task
Represents a task to be executed by an agent.
#### 
​
Parameters
  * `description: str` - Task description
  * `expected_output: str` - Expected output description
  * `agent: Agent | None = None` - Agent assigned to the task
  * `name: str | None = None` - Task name
  * `tools: List[Any] | None = None` - Tools available for the task
  * `context: List[Task] | None = None` - Context from other tasks
  * `async_execution: bool | None = False` - Enable async execution
  * `config: Dict[str, Any] | None = None` - Task configuration
  * `output_file: str | None = None` - Output file path
  * `output_json: Type[BaseModel] | None = None` - JSON output schema
  * `output_pydantic: Type[BaseModel] | None = None` - Pydantic output schema
  * `callback: Any | None = None` - Task callback
  * `status: str = 'not started'` - Task status
  * `result: TaskOutput | None = None` - Task result
  * `create_directory: bool | None = False` - Create output directory
  * `id: int | None = None` - Task ID
  * `images: List[str] | None = None` - Task images
  * `next_tasks: List[str] | None = None` - Next tasks
  * `task_type: str = 'task'` - Task type
  * `condition: Dict[str, List[str]] | None = None` - Task conditions
  * `is_start: bool = False` - Is start task
  * `loop_state: Dict[str, str | int] | None = None` - Loop state


#### 
​
Async Support
The Task class supports asynchronous execution through the following features:
  * `async_execution`: Boolean flag to enable async execution
  * `callback`: Supports both sync and async callback functions
  * `execute_callback`: Internal async method for handling callbacks


Example usage:
Copy
```
from typing import Coroutine
from praisonaiagents import Task, TaskOutput
# Define an async callback
async def async_callback(output: TaskOutput):
  await some_async_operation()
  print(f"Processed: {output.raw}")
# Create task with async execution
task = Task(
  description="Async task example",
  expected_output="Async result",
  async_execution=True, # Enable async execution
  callback=async_callback # Async callback
)

```

#### 
​
Callback Types
The Task class supports both synchronous and asynchronous callbacks:
Copy
```
# Type definition
callback: Optional[Union[
  Callable[[TaskOutput], Any], # Sync callback
  Callable[[TaskOutput], Coroutine[Any, Any, Any]] # Async callback
]]

```

#### 
​
Async Task States
  * `not started`: Initial state
  * `in progress`: Task is being executed
  * `completed`: Task finished successfully
  * `failed`: Task execution failed


Was this page helpful?
YesNo
AutoAgents ModuleProcess Module
On this page
  * Module praisonaiagents.task.task
  * Classes
  * Task
  * Parameters
  * Async Support
  * Callback Types
  * Async Task States


