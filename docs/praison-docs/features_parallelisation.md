PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Workflows
Agentic Parallelization
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
LLM Call 2
LLM Call 1
LLM Call 3
Aggregator
Out
A workflow that distributes tasks across multiple LLM calls simultaneously, aggregating results to handle complex or large-scale operations efficiently.
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
from praisonaiagents import Agent, Task, PraisonAIAgents
from datetime import datetime
import asyncio
def process_time():
  """Simulate processing"""
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(f"Processing at: {current_time}")
  return f"Processed at {current_time}"
# Create parallel processing agents
agent1 = Agent(
  name="Processor 1",
  role="Time collector",
  goal="Get the time and return it",
  tools=[process_time]
)
agent2 = Agent(
  name="Processor 2",
  role="Time collector",
  goal="Get the time and return it",
  tools=[process_time]
)
agent3 = Agent(
  name="Processor 3",
  role="Time collector",
  goal="Get the time and return it",
  tools=[process_time]
)
aggregator = Agent(
  name="Aggregator",
  role="Result aggregator",
  goal="Collect all the processed time from all tasks"
)
# Create parallel tasks with memory disabled
task1 = Task(
  name="process_1",
  description="Use process_time tool to get the time",
  expected_output="processed time",
  agent=agent1,
  is_start=True,
  async_execution=True
)
task2 = Task(
  name="process_2",
  description="Use process_time tool to get the time",
  expected_output="processed time",
  agent=agent2,
  is_start=True,
  async_execution=True
)
task3 = Task(
  name="process_3",
  description="Use process_time tool to get the time",
  expected_output="processed time",
  agent=agent3,
  is_start=True,
  async_execution=True
)
aggregate_task = Task(
  name="aggregate",
  description="Collect all the processed time from all tasks",
  expected_output="Output all the processed time from all tasks and just the time",
  agent=aggregator,
  context=[task1, task2, task3]
)
async def main():
  # Create workflow manager
  workflow = PraisonAIAgents(
    agents=[agent1, agent2, agent3, aggregator],
    tasks=[task1, task2, task3, aggregate_task],
    process="workflow"
  )
  # Run parallel workflow
  results = await workflow.astart()
  # Print results
  print("\nParallel Processing Results:")
  for task_id, result in results["task_results"].items():
    if result:
      print(f"Task {task_id}: {result.raw}")
# Run the async main function
if __name__ == "__main__":
  asyncio.run(main())

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
  * Basic understanding of Python and async programming


## 
​
Understanding Parallelisation
## What is Parallelisation?
Parallelisation enables:
  * Concurrent execution of multiple tasks
  * Improved performance through parallel processing
  * Efficient handling of independent operations
  * Aggregation of parallel task results


## 
​
Features
## Parallel Execution
Run multiple tasks simultaneously for improved performance.
## Async Support
Built-in support for asynchronous execution.
## Result Aggregation
Combine results from parallel tasks efficiently.
## Process Control
Monitor and manage parallel task execution.
## 
​
Configuration Options
Copy
```
# Create a parallel task
task = Task(
  name="parallel_task",
  description="Task to run in parallel",
  expected_output="Task result",
  agent=agent,
  is_start=True,
  async_execution=True # Enable parallel execution
)
# Create an aggregator task
aggregator_task = Task(
  name="aggregate",
  description="Aggregate results from parallel tasks",
  expected_output="Combined results",
  agent=aggregator,
  context=[task1, task2, task3] # Reference parallel tasks
)
# Async workflow execution
async def run_workflow():
  workflow = PraisonAIAgents(
    agents=[agent1, agent2, aggregator],
    tasks=[task1, task2, aggregator_task],
    process="workflow",
    verbose=True
  )
  results = await workflow.astart()

```

## 
​
Troubleshooting
## Execution Issues
If parallel execution fails:
  * Check async configuration
  * Verify task independence
  * Monitor resource usage


## Result Aggregation
If aggregation is incorrect:
  * Review task outputs
  * Check context connections
  * Verify aggregator logic


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your parallel tasks are truly independent and your system has sufficient resources to handle concurrent execution.
Was this page helpful?
YesNo
Autonomous WorkflowPrompt Chaining
On this page
  * Quick Start
  * Understanding Parallelisation
  * Features
  * Configuration Options
  * Troubleshooting
  * Next Steps


