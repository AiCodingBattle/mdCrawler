PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Workflows
Agentic Prompt Chaining
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
A workflow where the output of one LLM call becomes the input for the next. This sequential design allows for structured reasoning and step-by-step task completion.
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
import time
def get_time_check():
  current_time = int(time.time())
  result = "even" if current_time % 2 == 0 else "odd"
  print(f"Time check: {current_time} is {result}")
  return result
# Create agents for each step in the chain
agent1 = Agent(
  name="Time Checker",
  role="Time checker",
  goal="Check if the time is even or odd",
  instructions="Check if the time is even or odd",
  tools=[get_time_check]
)
agent2 = Agent(
  name="Advanced Analyzer",
  role="Advanced data analyzer",
  goal="Perform in-depth analysis of processed data",
  instructions="Analyze the processed data in detail"
)
agent3 = Agent(
  name="Final Processor",
  role="Final data processor",
  goal="Generate final output based on analysis",
  instructions="Create final output based on analyzed data"
)
# Create tasks for each step
initial_task = Task(
  name="time_check",
  description="Getting time check and checking if it is even or odd",
  expected_output="Getting time check and checking if it is even or odd",
  agent=agent1,
  is_start=True, # Mark as the starting task
  task_type="decision", # This task will make a decision
  next_tasks=["advanced_analysis"], # Next task if condition passes
  condition={
    "even": ["advanced_analysis"], # If passes, go to advanced analysis
    "odd": "" # If fails, exit the chain
  }
)
analysis_task = Task(
  name="advanced_analysis",
  description="Perform advanced analysis on the processed data",
  expected_output="Analyzed data ready for final processing",
  agent=agent2,
  next_tasks=["final_processing"]
)
final_task = Task(
  name="final_processing",
  description="Generate final output",
  expected_output="Final processed result",
  agent=agent3
)
# Create the workflow manager
workflow = PraisonAIAgents(
  agents=[agent1, agent2, agent3],
  tasks=[initial_task, analysis_task, final_task],
  process="workflow", # Use workflow process type
  verbose=True
)
# Run the workflow
results = workflow.start()
# Print results
print("\nWorkflow Results:")
for task_id, result in results["task_results"].items():
  if result:
    print(f"Task {task_id}: {result.raw}")

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
Understanding Prompt Chaining
## What is Prompt Chaining?
Prompt chaining enables:
  * Sequential execution of prompts
  * Data flow between agents
  * Conditional branching in workflows
  * Step-by-step processing of complex tasks


## 
​
Features
## Sequential Processing
Execute tasks in a defined sequence with data passing between steps.
## Decision Points
Implement conditional logic to control workflow progression.
## Data Flow
Pass data seamlessly between agents in the chain.
## Process Control
Monitor and control the execution of each step in the chain.
## 
​
Configuration Options to exit the chain
Copy
```
# Task with chaining configuration
task = Task(
  name="time_check",
  description="Check time and make decision",
  expected_output="Time check result",
  agent=agent,
  is_start=True,
  task_type="decision",
  next_tasks=["next_step"],
  condition={
    "even": ["next_step"],
    "odd": ""
  }
)

```

Copy
```
task = Task(
  name="time_check",
  description="Check time and make decision",
  expected_output="Time check result",
  agent=agent,
  is_start=True,
  task_type="decision",
  next_tasks=["next_step"],
  condition={
    "even": ["next_step"],
    "odd": "exit"
  }
)

```

Copy
```
task = Task(
  name="time_check",
  description="Check time and make decision",
  expected_output="Time check result",
  agent=agent,
  is_start=True,
  task_type="decision",
  next_tasks=["next_step"],
  condition={
    "even": ["next_step"],
    "odd": ["exit"]
  }
)

```

Copy
```
task = Task(
  name="time_check",
  description="Check time and make decision",
  expected_output="Time check result",
  agent=agent,
  is_start=True,
  task_type="decision",
  next_tasks=["next_step"],
  condition={
    "even": ["next_step"],
    "odd": [""]
  }
)

```

## 
​
Troubleshooting
## Chain Issues
If chain execution fails:
  * Verify task connections
  * Check condition logic
  * Enable verbose mode for debugging


## Data Flow
If data flow is incorrect:
  * Review task outputs
  * Check agent configurations
  * Verify task dependencies


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your chain is properly configured with clear task dependencies and conditions for branching logic.
Was this page helpful?
YesNo
ParallelizationEvaluator Optimizer
On this page
  * Quick Start
  * Understanding Prompt Chaining
  * Features
  * Configuration Options to exit the chain
  * Troubleshooting
  * Next Steps


