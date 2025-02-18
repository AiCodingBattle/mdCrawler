PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Workflows
Agentic Evaluator Optimizer
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


SOLUTION
ACCEPTED
REJECTED + FEEDBACK
In
LLM Call Generator
LLM Call Evaluator
Out
A feedback loop workflow where LLM-generated outputs are evaluated, refined, and optimized iteratively to improve accuracy and relevance.
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
# Create generator and evaluator agents
generator = Agent(
  name="Generator",
  role="Solution generator",
  goal="Generate initial solutions and incorporate feedback",
  instructions=(
    "1. Look at the context from previous tasks.\n"
    "2. If you see that you have already produced 2 points, then add another 2 new points "
    "  so that the total becomes 10.\n"
    "3. Otherwise, just produce the first 2 points.\n"
    "4. Return only the final list of points, with no extra explanation."
  )
)
evaluator = Agent(
  name="Evaluator",
  role="Solution evaluator",
  goal="Evaluate solutions and provide improvement feedback",
  instructions=(
    "1. Count how many lines in the response start with a number and a period (like '1. ' or '2. ').\n"
    "2. If there are 10 or more, respond with 'done'.\n"
    "3. Otherwise, respond with 'more'.\n"
    "4. Return only the single word: 'done' or 'more'."
  )
)
# Create tasks for the feedback loop
generate_task = Task(
  name="generate",
  description="Write 2 points about AI incuding if anything exiting from previous points",
  expected_output="2 points",
  agent=generator,
  is_start=True,
  task_type="decision",
  next_tasks=["evaluate"]
)
evaluate_task = Task(
  name="evaluate",
  description="Check if there are 10 points about AI",
  expected_output="more or done",
  agent=evaluator,
  next_tasks=["generate"],
  context=[generate_task],
  task_type="decision",
  condition={
    "more": ["generate"], # Continue to generate
    "done": [""] # Exit when optimization complete
  }
)
# Create workflow manager
workflow = PraisonAIAgents(
  agents=[generator, evaluator],
  tasks=[generate_task, evaluate_task],
  process="workflow",
  verbose=True
)
# Run optimization workflow
results = workflow.start()
# Print results
print("\nEvaluator-Optimizer Results:")
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
Understanding Evaluator-Optimizer
## What is Evaluator-Optimizer?
Evaluator-Optimizer pattern enables:
  * Iterative solution generation and refinement
  * Automated quality evaluation
  * Feedback-driven optimization
  * Continuous improvement loops


## 
​
Features
## Solution Generation
Generate solutions based on requirements and feedback.
## Quality Evaluation
Automatically assess solution quality and completeness.
## Feedback Loop
Implement iterative improvement through feedback cycles.
## Process Control
Monitor and control the optimization process.
## 
​
Configuration Options
Copy
```
# Create a generator agent
generator = Agent(
  name="Generator",
  role="Solution generator",
  goal="Generate and improve solutions",
  instructions="Step-by-step instructions for generation",
  verbose=True # Enable detailed logging
)
# Create an evaluator agent
evaluator = Agent(
  name="Evaluator",
  role="Solution evaluator",
  goal="Evaluate and provide feedback",
  instructions="Evaluation criteria and feedback format"
)
# Create tasks with feedback loop
generate_task = Task(
  name="generate",
  description="Generate solution",
  agent=generator,
  is_start=True,
  task_type="decision",
  next_tasks=["evaluate"]
)
evaluate_task = Task(
  name="evaluate",
  description="Evaluate solution",
  agent=evaluator,
  context=[generate_task],
  task_type="decision",
  condition={
    "more": ["generate"], # Continue optimization
    "done": [""] # Exit when complete
  }
)

```

## 
​
Troubleshooting
## Generation Issues
If generation is not improving:
  * Review generator instructions
  * Check feedback integration
  * Enable verbose mode for debugging


## Evaluation Flow
If evaluation cycle is incorrect:
  * Verify evaluation criteria
  * Check condition mappings
  * Review feedback loop connections


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your generator instructions and evaluation criteria are clear and well-defined to achieve the desired optimization outcomes.
Was this page helpful?
YesNo
Prompt ChainingRepetitive Agents
On this page
  * Quick Start
  * Understanding Evaluator-Optimizer
  * Features
  * Configuration Options
  * Troubleshooting
  * Next Steps


