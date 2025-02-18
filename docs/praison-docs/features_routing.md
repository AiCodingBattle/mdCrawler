PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Workflows
Agentic Routing
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


In
LLM Call Router
LLM Call 1
LLM Call 2
LLM Call 3
Out
A low-latency workflow where inputs are dynamically routed to the most appropriate LLM instance or configuration, optimizing efficiency and specialization.
## 
​
Quick Start
1
Install Package
First, install the PraisonAI Agents package:
Copy
```
pip install praisonaiagents

```

2
Set API Key
Set your OpenAI API key as an environment variable in your terminal:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

3
Create a file
Create a new file `app.py` with the basic setup:
Copy
```
from praisonaiagents.agent import Agent
from praisonaiagents.task import Task
from praisonaiagents.agents import PraisonAIAgents
import time
def get_time_check():
  current_time = int(time.time())
  result = "even" if current_time % 2 == 0 else "odd"
  print(f"Time check: {current_time} is {result}")
  return result
# Create specialized agents
router = Agent(
  name="Router",
  role="Input Router",
  goal="Evaluate input and determine routing path",
  instructions="Analyze input and decide whether to proceed or exit",
  tools=[get_time_check]
)
processor1 = Agent(
  name="Processor 1",
  role="Secondary Processor",
  goal="Process valid inputs that passed initial check",
  instructions="Process data that passed the routing check"
)
processor2 = Agent(
  name="Processor 2",
  role="Final Processor",
  goal="Perform final processing on validated data",
  instructions="Generate final output for processed data"
)
# Create tasks with routing logic
routing_task = Task(
  name="initial_routing",
  description="check the time and return according to what is returned",
  expected_output="pass or fail based on what is returned",
  agent=router,
  is_start=True,
  task_type="decision",
  condition={
    "pass": ["process_valid"],
    "fail": ["process_invalid"]
  }
)
processing_task = Task(
  name="process_valid",
  description="Process validated input",
  expected_output="Processed data ready for final step",
  agent=processor1,
)
final_task = Task(
  name="process_invalid",
  description="Generate final output",
  expected_output="Final processed result",
  agent=processor2
)
# Create and run workflow
workflow = PraisonAIAgents(
  agents=[router, processor1, processor2],
  tasks=[routing_task, processing_task, final_task],
  process="workflow",
  verbose=True
)
print("\nStarting Routing Workflow...")
print("=" * 50)
results = workflow.start()
print("\nWorkflow Results:")
print("=" * 50)
for task_id, result in results["task_results"].items():
  if result:
    task_name = result.description
    print(f"\nTask: {task_name}")
    print(f"Result: {result.raw}")
    print("-" * 50)

```

4
Start Agents
Type this in your terminal to run your agents:
Copy
```
python app.py

```

**Requirements**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.
  * Basic understanding of Python


## 
​
Understanding Agentic Routing
## What is Agentic Routing?
Agentic routing enables:
  * Dynamic decision-making in workflows
  * Conditional task execution paths
  * Automated process branching
  * Intelligent workflow management


## 
​
Features
## Dynamic Routing
Route tasks based on real-time decisions and conditions.
## Conditional Logic
Implement complex branching logic in workflows.
## Task Management
Handle task dependencies and execution order.
## Process Control
Control workflow execution with detailed monitoring.
## 
​
Configuration Options
Copy
```
# Create a router agent
router = Agent(
  name="Router",
  role="Input Router",
  goal="Evaluate input and determine routing path",
  instructions="Analyze input and decide whether to proceed or exit",
  tools=[get_time_check], # Custom tools for routing decisions
  verbose=True # Enable detailed logging
)
# Task with routing configuration
routing_task = Task(
  name="initial_routing",
  description="Route based on conditions",
  expected_output="Routing decision",
  agent=router,
  is_start=True,
  task_type="decision",
  condition={
    "pass": ["next_task"],
    "fail": ["alternate_task"]
  }
)

```

## 
​
Troubleshooting
## Routing Issues
If routing doesn’t work as expected:
  * Verify condition mappings
  * Check task dependencies
  * Enable verbose mode for debugging


## Workflow Flow
If workflow is unclear:
  * Review task connections
  * Verify agent configurations
  * Check routing conditions


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your routing conditions are well-defined and your task dependencies are properly configured.
Was this page helpful?
YesNo
KnowledgeOrchestrator Worker
On this page
  * Quick Start
  * Understanding Agentic Routing
  * Features
  * Configuration Options
  * Troubleshooting
  * Next Steps


