PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Core Concepts
Tasks
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
Understanding Tasks
Tasks are units of work that agents execute. Each task has a clear goal, input requirements, and expected outputs.
Task
Role
Goal
Backstory
Expected Output
Input
Output
## 
​
Core Components
## Task Definition
Clear description of work to be done and expected outputs
## Agent Assignment
Matching tasks with capable agents
## Tool Access
Resources available for task completion
## Output Handling
Managing and formatting task results
## 
​
Task Configuration
Basic
Advanced
Copy
```
task = Task(
  description="Research AI trends",
  expected_output="Summary report",
  agent=research_agent
)

```

# 
​
Understanding Tasks
⚙️ Execution
Processing & Tools
🤖 Agent Assignment
Matching & Delegation
📋 Task Definition
Description & Requirements
▶ Start
✓ Output
📥 Pending
⚡ In Progress
✅ Completed
❌ Failed
## 
​
Task Types
1
Basic Task
Simple, single-operation tasks with clear inputs and outputs
2
Decision Task
Tasks involving choices and conditional paths
Copy
```
decision_task = Task(
  type="decision",
  conditions={
    "success": ["next_task"],
    "failure": ["error_task"]
  }
)

```

3
Loop Task
Repetitive operations over collections
Copy
```
loop_task = Task(
  type="loop",
  items=data_list,
  operation="process_item"
)

```

## 
​
Task Relationships
Properly managing task dependencies is crucial for complex workflows. Always ensure proper context sharing and error handling.
### 
​
Context Sharing
Copy
```
task_a = Task(name="research")
task_b = Task(
  name="analyze",
  context=[task_a] # Uses task_a's output
)

```

### 
​
Task Dependencies
Relationship| Description| Example  
---|---|---  
**Sequential**|  Tasks run one after another| Research → Analysis → Report  
**Parallel**|  Independent tasks run simultaneously| Data Collection + Processing  
**Conditional**|  Tasks depend on previous results| Success → Next Task, Failure → Retry  
## 
​
Advanced Features
## Output Handling
  * Multiple output formats
  * Structured data validation
  * File system integration


## Task Control
  * Execution flow control
  * Error recovery
  * Progress tracking


## 
​
Getting Started
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
Multiple Agents
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create an agent
researcher = Agent(
  name="Researcher",
  role="Senior Research Analyst",
  goal="Uncover cutting-edge developments in AI",
  backstory="You are an expert at a technology research group",
  verbose=True,
  llm="gpt-4o"
)
# Define a task
task = Task(
  name="research_task",
  description="Analyze 2024's AI advancements",
  expected_output="A detailed report",
  agent=researcher
)
# Run the agents
agents = PraisonAIAgents(
  agents=[researcher],
  tasks=[task],
  verbose=False
)
result = agents.start()

```

## 
​
Best Practices
Design tasks to be atomic and focused. Each task should have a single, clear responsibility.
## Task Design Principles
Clear Task Descriptions
Write precise, unambiguous task descriptions that clearly state the task’s purpose and requirements.
Copy
```
task = Task(
  description=(
    "Analyze Q4 2024 sales data "
    "and generate growth metrics"
  ),
  expected_output="Sales growth report"
)

```

Success Criteria
Define measurable success criteria to ensure task completion can be properly evaluated.
Copy
```
task = Task(
  success_criteria={
    "format": "markdown",
    "metrics": [
      "growth_rate",
      "revenue_change"
    ],
    "min_confidence": 0.95
  }
)

```

Task Dependencies
Specify any dependencies or prerequisites for the task.
Copy
```
task = Task(
  description="Generate final report",
  dependencies=[
    data_collection_task,
    analysis_task
  ],
  wait_for_dependencies=True
)

```

## Resource Management
Tool Selection
Choose appropriate tools that match your task’s requirements.
Copy
```
task = Task(
  tools=[
    DataAnalyzer(),
    ReportGenerator(),
    MetricsCalculator()
  ],
  tool_config={
    "timeout": 30,
    "retry": True
  }
)

```

Error Handling
Implement comprehensive error management strategies.
Copy
```
task = Task(
  error_strategy="retry",
  max_retries=3,
  fallback_handler=handler,
  error_callbacks=[
    log_error,
    notify_admin
  ]
)

```

Resource Limits
Set appropriate resource constraints for optimal performance.
Copy
```
task = Task(
  memory_limit="2GB",
  timeout=300,
  max_concurrent=5,
  cpu_priority="high",
  auto_scale=True
)

```

Performance Monitoring
Configure monitoring and logging for task execution.
Copy
```
task = Task(
  monitoring={
    "metrics": ["duration", "memory", "cpu"],
    "log_level": "INFO",
    "trace_enabled": True,
    "alert_threshold": 0.85
  }
)

```

## 
​
Async Task Execution
## Async Task Features
  * Basic Configuration
  * Async Callbacks
  * Mixed Execution


Copy
```
async_task = Task(
  description="Perform async operation",
  expected_output="Async result",
  agent=async_agent,
  async_execution=True, # Enable async execution
  callback=async_callback # Optional async callback
)

```

  * Enable async execution with `async_execution=True`
  * Perfect for I/O-heavy operations
  * Supports parallel task execution


**Pro Tip** : Use async execution for tasks that involve I/O operations (like API calls or file operations) to improve overall performance. Keep CPU-intensive tasks synchronous.
## 
​
Next Steps
## Create Tasks
Learn how to create and configure tasks
## Task API
Explore the complete Task API documentation
Was this page helpful?
YesNo
AgentsProcess
On this page
  * Understanding Tasks
  * Core Components
  * Task Configuration
  * Understanding Tasks
  * Task Types
  * Task Relationships
  * Context Sharing
  * Task Dependencies
  * Advanced Features
  * Getting Started
  * Best Practices
  * Async Task Execution
  * Next Steps


