PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Code Execution AI Agent
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


## 
​
Quick Start
  * Code
  * No Code


1
Install Package
First, install the required packages:
Copy
```
pip install praisonaiagents e2b_code_interpreter

```

2
Set API Key
Set your OpenAI API key and E2B API key as an environment variable in your terminal:
Copy
```
export OPENAI_API_KEY=your_api_key_here
export E2B_API_KEY=your_e2b_api_key_here

```

3
Create a file
Create a new file `app.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
from e2b_code_interpreter import Sandbox
def code_interpreter(code: str):
  print(f"\n{'='*50}\n> Running following AI-generated code:\n{code}\n{'='*50}")
  exec_result = Sandbox().run_code(code)
  if exec_result.error:
    print("[Code Interpreter error]", exec_result.error)
    return {"error": str(exec_result.error)}
  else:
    results = []
    for result in exec_result.results:
      if hasattr(result, '__iter__'):
        results.extend(list(result))
      else:
        results.append(str(result))
    logs = {"stdout": list(exec_result.logs.stdout), "stderr": list(exec_result.logs.stderr)}
    return json.dumps({"results": results, "logs": logs})
# Create code agent
code_agent = Agent(
  role="Code Developer",
  goal="Write and execute Python code",
  backstory="Expert Python developer with strong coding skills",
  tools=[code_interpreter],
  verbose=True
)
# Create a task
task = Task(
  description="Write and execute a Python script to analyze data",
  expected_output="Working Python script with execution results",
  agent=code_agent
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[code_agent],
  tasks=[task],
  process="sequential",
  verbose=2
)
# Start execution
agents.start()

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
  * e2b_code_interpreter package installed


## 
​
Understanding Code Agents
## What are Code Agents?
Code agents are specialized AI agents that can:
  * Write Python code based on requirements
  * Execute code safely in a sandboxed environment
  * Handle code execution results and errors
  * Work together in a pipeline (writer → executor)


## 
​
Features
## Code Writer
Writes Python code based on requirements.
## Safe Execution
Executes code in a sandboxed environment.
## Error Handling
Manages code execution errors and debugging.
## Results Processing
Processes and formats execution results.
## 
​
Multi-Agent Code Development
  * Code
  * No Code


1
Install Package
First, install the required packages:
Copy
```
pip install praisonaiagents e2b_code_interpreter

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
from e2b_code_interpreter import Sandbox
def code_interpreter(code: str):
  print(f"\n{'='*50}\n> Running following AI-generated code:\n{code}\n{'='*50}")
  exec_result = Sandbox().run_code(code)
  if exec_result.error:
    print("[Code Interpreter error]", exec_result.error)
    return {"error": str(exec_result.error)}
  else:
    results = []
    for result in exec_result.results:
      if hasattr(result, '__iter__'):
        results.extend(list(result))
      else:
        results.append(str(result))
    logs = {"stdout": list(exec_result.logs.stdout), "stderr": list(exec_result.logs.stderr)}
    return json.dumps({"results": results, "logs": logs})
# Create first agent for writing code
code_writer = Agent(
  role="Code Writer",
  goal="Write efficient Python code",
  backstory="Expert Python developer specializing in code writing",
  verbose=True
)
# Create second agent for code execution
code_executor = Agent(
  role="Code Executor",
  goal="Execute and validate Python code",
  backstory="Expert in code execution and testing",
  tools=[code_interpreter],
  verbose=True
)
# Create first task
writing_task = Task(
  description="Write a Python script for data analysis",
  expected_output="Complete Python script",
  agent=code_writer
)
# Create second task
execution_task = Task(
  description="Execute and validate the Python script",
  expected_output="Execution results and validation",
  agent=code_executor
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[code_writer, code_executor],
  tasks=[writing_task, execution_task],
  process="sequential"
)
# Start execution
agents.start()

```

4
Start Agents
Type this in your terminal to run your agents:
Copy
```
python app.py

```

### 
​
Configuration Options
Copy
```
# Create an agent with advanced code execution configuration
agent = Agent(
  role="Code Developer",
  goal="Write and execute Python code",
  backstory="Expert in Python development",
  tools=[code_interpreter],
  verbose=True, # Enable detailed logging
  llm="gpt-4o" # Language model to use
)

```

## 
​
Troubleshooting
## Code Errors
If code execution fails:
  * Check syntax errors
  * Verify package imports
  * Enable verbose mode for debugging


## Sandbox Issues
If sandbox execution fails:
  * Check environment setup
  * Verify permissions
  * Review resource limits


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure code is properly formatted and tested in the sandbox environment before production use.
Was this page helpful?
YesNo
Generate Reasoning DataMath Agent
On this page
  * Quick Start
  * Understanding Code Agents
  * Features
  * Multi-Agent Code Development
  * Configuration Options
  * Troubleshooting
  * Next Steps


