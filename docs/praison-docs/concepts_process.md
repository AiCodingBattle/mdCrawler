PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Core Concepts
Process
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
Understanding Process Types
Process types in PraisonAI define how tasks are executed and how agents collaborate. Each process type offers different patterns for task execution and agent coordination.
## 
​
Process Types Overview
## Sequential Process
Linear task execution in a predefined order
## Hierarchical Process
Manager-coordinated task execution with dynamic assignment
## Workflow Process
Complex task flows with conditional execution and state management
## 
​
Sequential Process
Agents
Agent 3
Agent 2
Agent 1
Input
Output
The simplest form of task execution where tasks are performed one after another.
### Characteristics
  * Linear execution flow
  * Predictable order
  * Simple dependency management
  * Direct task progression


### Usage
Copy
```
agents = PraisonAIAgents(
  agents=[agent1, agent2],
  tasks=[task1, task2, task3],
  process="sequential"
)

```

## 
​
Hierarchical Process
Agents
Workers
Manager Agent
Worker 1
Worker 2
Worker 3
Input
Output
Uses a manager agent to coordinate task execution and agent assignments.
### Characteristics
  * Manager-driven coordination
  * Dynamic task assignment
  * Flexible execution order
  * Intelligent resource allocation


### Configuration
Copy
```
agents = PraisonAIAgents(
  agents=[manager_agent, worker_agent1, worker_agent2],
  tasks=[task1, task2],
  process="hierarchical",
  manager_llm="gpt-4o"
)

```

## 
​
Workflow Process
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
Advanced process type supporting complex task relationships and conditional execution.
### Features
  * Task dependencies
  * Conditional branching
  * Loop handling
  * Context sharing
  * State management


### Implementation
Copy
```
task_workflow = {
  "start_task": {
    "next": ["decision_task"],
    "type": "task"
  },
  "decision_task": {
    "type": "decision",
    "conditions": {
      "success": ["process_task"],
      "failure": ["error_task"]
    }
  }
}

```

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
Single Agent Sequential Process
Multiple Agents Hierarchical Process
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
  verbose=False,
  process="sequential"
)
result = agents.start()

```

## 
​
Advanced Features
## State Management
Task State Tracking
Monitor and manage the progress of each task in real-time
Context Preservation
Maintain important information across different stages of execution
Data Flow Control
Manage how data moves between tasks and agents efficiently
## Error Handling
Graceful Recovery
Automatically handle failures and continue execution
Alternative Paths
Switch to backup plans when primary execution fails
Error Reporting
Detailed error logs and diagnostic information
## Monitoring
Progress Tracking
Real-time visibility into task completion status
Performance Metrics
Measure execution time and resource efficiency
Resource Usage
Monitor system resource utilization
## Integration
External Systems
Connect with other services and platforms
API Sync
Maintain data consistency across systems
Event Handling
React to system and external events
## 
​
Async Processing
All process types support asynchronous execution through async generators, enabling efficient parallel processing and non-blocking operations.
### 
​
Core Async Methods
## asequential
Async version of sequential process for non-blocking linear execution
## aworkflow
Async workflow process for complex parallel task execution
## ahierarchical
Async hierarchical process for distributed task management
### 
​
Process-Specific Features
  * Sequential Process
  * Workflow Process
  * Hierarchical Process


  * Tasks execute in order but don’t block
  * Maintains sequence while allowing async operations
  * Perfect for I/O-heavy tasks


Copy
```
async def main():
  agents = PraisonAIAgents(
    process="sequential",
    async_mode=True
  )
  await agents.astart()

```

### 
​
Key Benefits
## Performance
  * Efficient resource utilization
  * Reduced waiting time
  * Better throughput


## Flexibility
  * Mix sync and async tasks
  * Adaptable execution patterns
  * Easy scaling


Was this page helpful?
YesNo
TasksTools
On this page
  * Understanding Process Types
  * Process Types Overview
  * Sequential Process
  * Hierarchical Process
  * Workflow Process
  * Getting Started
  * Advanced Features
  * Async Processing
  * Core Async Methods
  * Process-Specific Features
  * Key Benefits


