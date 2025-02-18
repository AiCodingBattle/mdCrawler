PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Workflows
Agentic Autonomous Workflow
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


ACTION
FEEDBACK
Human
LLM Call
Environment
Stop
An agent-based workflow where LLMs act autonomously within a loop, interacting with their environment and receiving feedback to refine their actions and decisions.
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
def get_environment_state():
  """Simulates getting current environment state"""
  current_time = int(time.time())
  states = ["normal", "critical", "optimal"]
  state = states[current_time % 3]
  print(f"Environment state: {state}")
  return state
def perform_action(state: str):
  """Simulates performing an action based on state"""
  actions = {
    "normal": "maintain",
    "critical": "fix",
    "optimal": "enhance"
  }
  action = actions.get(state, "observe")
  print(f"Performing action: {action} for state: {state}")
  return action
def get_feedback():
  """Simulates environment feedback"""
  current_time = int(time.time())
  feedback = "positive" if current_time % 2 == 0 else "negative"
  print(f"Feedback received: {feedback}")
  return feedback
# Create specialized agents
llm_caller = Agent(
  name="Environment Monitor",
  role="State analyzer",
  goal="Monitor environment and analyze state",
  instructions="Check environment state and provide analysis",
  tools=[get_environment_state]
)
action_agent = Agent(
  name="Action Executor",
  role="Action performer",
  goal="Execute appropriate actions based on state",
  instructions="Determine and perform actions based on environment state",
  tools=[perform_action]
)
feedback_agent = Agent(
  name="Feedback Processor",
  role="Feedback analyzer",
  goal="Process environment feedback and adapt strategy",
  instructions="Analyze feedback and provide adaptation recommendations",
  tools=[get_feedback]
)
# Create tasks for autonomous workflow
monitor_task = Task(
  name="monitor_environment",
  description="Monitor and analyze environment state",
  expected_output="Current environment state analysis",
  agent=llm_caller,
  is_start=True,
  task_type="decision",
  next_tasks=["execute_action"],
  condition={
    "normal": ["execute_action"],
    "critical": ["execute_action"],
    "optimal": "exit"
  }
)
action_task = Task(
  name="execute_action",
  description="Execute appropriate action based on state",
  expected_output="Action execution result",
  agent=action_agent,
  next_tasks=["process_feedback"]
)
feedback_task = Task(
  name="process_feedback",
  description="Process feedback and adapt strategy",
  expected_output="Strategy adaptation based on feedback",
  agent=feedback_agent,
  next_tasks=["monitor_environment"], # Create feedback loop
  context=[monitor_task, action_task] # Access to previous states and actions
)
# Create workflow manager
workflow = PraisonAIAgents(
  agents=[llm_caller, action_agent, feedback_agent],
  tasks=[monitor_task, action_task, feedback_task],
  process="workflow",
  verbose=True
)
def main():
  print("\nStarting Autonomous Agent Workflow...")
  print("=" * 50)
  
  # Run autonomous workflow
  results = workflow.start()
  
  # Print results
  print("\nAutonomous Agent Results:")
  print("=" * 50)
  for task_id, result in results["task_results"].items():
    if result:
      task_name = result.description
      print(f"\nTask: {task_name}")
      print(f"Result: {result.raw}")
      print("-" * 50)
if __name__ == "__main__":
  main()

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
Understanding Autonomous Workflow
## What is Autonomous Workflow?
Autonomous Workflow enables:
  * Continuous environment monitoring
  * Automated decision-making and action execution
  * Real-time feedback processing
  * Self-adapting behavior based on outcomes


## 
​
Features
## Environment Monitoring
Continuously monitor and analyze environment state.
## Adaptive Actions
Execute context-aware actions based on state analysis.
## Feedback Processing
Process and learn from action outcomes.
## Self-Optimization
Improve performance through continuous learning.
## 
​
Configuration Options
Copy
```
# Create a monitor agent
monitor = Agent(
  name="Environment Monitor",
  role="State analyzer",
  goal="Monitor and analyze state",
  tools=[get_environment_state], # Environment monitoring tools
  verbose=True # Enable detailed logging
)
# Create an action agent
action = Agent(
  name="Action Executor",
  role="Action performer",
  goal="Execute appropriate actions",
  tools=[perform_action] # Action execution tools
)
# Create monitoring task
monitor_task = Task(
  name="monitor_environment",
  description="Monitor environment state",
  agent=monitor,
  is_start=True,
  task_type="decision",
  condition={
    "normal": ["execute_action"],
    "critical": ["execute_action"],
    "optimal": "exit"
  }
)
# Create feedback loop task
feedback_task = Task(
  name="process_feedback",
  description="Process and adapt",
  agent=feedback_agent,
  next_tasks=["monitor_environment"], # Create feedback loop
  context=[monitor_task, action_task] # Access history
)

```

## 
​
Troubleshooting
## Monitoring Issues
If monitoring fails:
  * Check environment access
  * Verify state detection
  * Enable verbose mode for debugging


## Adaptation Flow
If adaptation is incorrect:
  * Review feedback processing
  * Check action outcomes
  * Verify learning loop


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your environment monitoring is reliable and your feedback processing logic is properly configured for effective adaptation.
Was this page helpful?
YesNo
Orchestrator WorkerParallelization
On this page
  * Quick Start
  * Understanding Autonomous Workflow
  * Features
  * Configuration Options
  * Troubleshooting
  * Next Steps


