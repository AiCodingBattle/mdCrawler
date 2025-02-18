PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
API Reference
AutoAgents Module
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
Module praisonaiagents.agents.autoagents
The AutoAgents module provides automatic creation and management of AI agents and tasks based on high-level instructions.
## 
​
Classes
### 
​
AutoAgents
The main class for automatically creating and managing AI agents and tasks.
#### 
​
Parameters
  * `instructions: str` - High-level task description for the agents
  * `tools: Optional[List[Any]] = None` - List of tools available to the agents
  * `verbose: bool = False` - Enable detailed logging
  * `process: str = "sequential"` - Process type (sequential or hierarchical)
  * `manager_llm: Optional[str] = None` - Language model for manager agent
  * `max_retries: int = 5` - Maximum retry attempts
  * `completion_checker: Optional[Any] = None` - Custom completion checker
  * `allow_code_execution: bool = False` - Allow code execution
  * `memory: bool = True` - Enable agent memory
  * `markdown: bool = True` - Enable markdown formatting
  * `self_reflect: bool = False` - Enable agent self-reflection
  * `max_reflect: int = 3` - Maximum reflection iterations
  * `min_reflect: int = 1` - Minimum reflection iterations
  * `llm: Optional[str] = None` - Language model for agents
  * `function_calling_llm: Optional[str] = None` - Language model for tool calling
  * `respect_context_window: bool = True` - Respect model context window
  * `code_execution_mode: str = "safe"` - Code execution mode (safe/unsafe)
  * `embedder_config: Optional[Dict[str, Any]] = None` - Embedder configuration
  * `knowledge_sources: Optional[List[Any]] = None` - Knowledge sources
  * `use_system_prompt: bool = True` - Use system prompts
  * `cache: bool = True` - Enable caching
  * `allow_delegation: bool = False` - Allow task delegation
  * `step_callback: Optional[Any] = None` - Callback for each step
  * `system_template: Optional[str] = None` - Custom system template
  * `prompt_template: Optional[str] = None` - Custom prompt template
  * `response_template: Optional[str] = None` - Custom response template
  * `max_rpm: Optional[int] = None` - Maximum requests per minute
  * `max_execution_time: Optional[int] = None` - Maximum execution time
  * `max_iter: int = 20` - Maximum iterations
  * `reflect_llm: Optional[str] = None` - Language model for reflection
  * `max_agents: int = 3` - Maximum number of agents to create


#### 
​
Methods
##### start()
Start the agents synchronously.
Copy
```
def start(self):
  """
  Creates tasks based on the instructions, then starts execution.
  Returns the task status and results dictionary.
  """
  return super().start()

```

##### astart()
Start the agents asynchronously.
Copy
```
async def astart(self):
  """
  Async version of start() method.
  Creates tasks based on the instructions, then starts execution.
  Returns the task status and results dictionary.
  """
  return await super().astart()

```

#### 
​
Internal Methods
##### _generate_config()
Generate the configuration for agents and tasks.
Copy
```
def _generate_config(self) -> AutoAgentsConfig:
  """
  Generate the configuration for agents and tasks based on instructions.
  Returns AutoAgentsConfig object containing agent and task configurations.
  """

```

##### _create_agents_and_tasks()
Create agents and tasks from configuration.
Copy
```
def _create_agents_and_tasks(self, config: AutoAgentsConfig) -> tuple[List[Agent], List[Task]]:
  """
  Create agents and tasks based on the generated configuration.
  Returns tuple of (agents, tasks).
  """

```

##### _assign_tools_to_agent()
Assign appropriate tools to an agent.
Copy
```
def _assign_tools_to_agent(self, agent_config: AgentConfig) -> List[Any]:
  """
  Assign tools to an agent based on its role and tasks.
  Returns list of assigned tools.
  """

```

## 
​
Pydantic Models
### 
​
TaskConfig
Configuration for a task.
#### 
​
Attributes
  * `name: str` - Task name
  * `description: str` - Task description
  * `expected_output: str` - Expected output description
  * `tools: List[str]` - Required tools for the task


### 
​
AgentConfig
Configuration for an agent.
#### 
​
Attributes
  * `name: str` - Agent name
  * `role: str` - Agent role
  * `goal: str` - Agent goal
  * `backstory: str` - Agent backstory
  * `tools: List[str]` - Required tools
  * `tasks: List[TaskConfig]` - Tasks assigned to the agent


### 
​
AutoAgentsConfig
Overall configuration for AutoAgents.
#### 
​
Attributes
  * `main_instruction: str` - Main instruction for the agents
  * `process_type: str` - Process type (sequential/hierarchical)
  * `agents: List[AgentConfig]` - List of agent configurations


## 
​
Example Usage
### 
​
Basic Usage
Copy
```
from praisonaiagents import AutoAgents
from praisonaiagents.tools import SerperDevTool
agents = AutoAgents(
  instructions="Research recent AI developments",
  tools=[SerperDevTool()],
  verbose=True
)
result = agents.start()

```

### 
​
Async Usage
Copy
```
async def main():
  agents = AutoAgents(
    instructions="Research recent AI developments",
    tools=[SerperDevTool()],
    process="hierarchical"
  )
  result = await agents.astart()
import asyncio
asyncio.run(main())

```

### 
​
Advanced Configuration
Copy
```
agents = AutoAgents(
  instructions="Complex research task",
  tools=[SerperDevTool()],
  max_agents=5,
  process="hierarchical",
  manager_llm="gpt-4o",
  memory=True,
  allow_delegation=True,
  max_execution_time=600,
  self_reflect=True
)

```

For optimal results, provide clear instructions and appropriate tools for your use case.
Was this page helpful?
YesNo
Agents ModuleTask Module
On this page
  * Module praisonaiagents.agents.autoagents
  * Classes
  * AutoAgents
  * Parameters
  * Methods
  * Internal Methods
  * Pydantic Models
  * TaskConfig
  * Attributes
  * AgentConfig
  * Attributes
  * AutoAgentsConfig
  * Attributes
  * Example Usage
  * Basic Usage
  * Async Usage
  * Advanced Configuration


