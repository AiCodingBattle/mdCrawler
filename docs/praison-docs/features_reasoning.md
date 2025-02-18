PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Reasoning Agents
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
AI Agent
Think
Decide
Act
Out
Learn how to create AI agents with advanced reasoning capabilities for complex problem-solving.
## 
​
Quick Start
  * Code
  * No Code


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
from praisonaiagents import Agent, Task, PraisonAIAgents, Tools
# Create reasoning agent
reasoner = Agent(
  role="Problem Solver",
  goal="Solve complex problems using logical reasoning",
  backstory="Expert in logical analysis and problem-solving",
  tools=[Tools.internet_search],
  verbose=True
)
# Create task
task = Task(
  description="Analyze and solve a complex business problem",
  expected_output="Detailed solution with reasoning steps",
  agent=reasoner
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[reasoner],
  tasks=[task],
  process="sequential",
  verbose=2
)
# Start execution
result = agents.start()
print(result)

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
Understanding Reasoning
## What is Reasoning?
Reasoning agents are designed to:
  * Break down complex problems into manageable steps
  * Apply logical analysis to find solutions
  * Explain their thought process and decisions
  * Handle uncertainty and incomplete information


## 
​
Features
## Problem Decomposition
Break complex problems into smaller, manageable parts.
## Logical Analysis
Apply structured thinking to solve problems.
## Error Recovery
Handle edge cases and recover from errors.
## Explanation
Provide detailed reasoning for decisions.
## 
​
Multi-Agent Reasoning
  * Code
  * No Code


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
from praisonaiagents import Agent, Task, PraisonAIAgents, Tools
# Create first agent for analysis
analyst = Agent(
  role="Business Analyst",
  goal="Analyze business problems and identify key issues",
  backstory="Expert in business analysis and problem identification",
  tools=[Tools.internet_search],
  verbose=True
)
# Create second agent for solution development
solver = Agent(
  role="Solution Architect",
  goal="Develop comprehensive solutions to business problems",
  backstory="Expert in solution design and implementation",
  verbose=True
)
# Create first task
analysis_task = Task(
  description="Analyze the current market challenges",
  expected_output="Detailed analysis of key issues",
  agent=analyst
)
# Create second task
solution_task = Task(
  description="Develop solutions for identified challenges",
  expected_output="Comprehensive solution strategy",
  agent=solver
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[analyst, solver],
  tasks=[analysis_task, solution_task],
  process="sequential"
)
# Start execution
result = agents.start()

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
# Create an agent with reasoning configuration
agent = Agent(
  role="Problem Solver",
  goal="Solve complex problems",
  backstory="Expert in problem-solving",
  tools=[Tools.internet_search],
  verbose=True, # Enable detailed logging
  llm="gpt-4o" # Language model to use
)
# Task with reasoning requirements
task = Task(
  description="Solve complex problem",
  expected_output="Detailed solution",
  agent=agent
)

```

## 
​
Troubleshooting
## Reasoning Errors
If reasoning seems incorrect:
  * Check problem description clarity
  * Enable verbose mode for debugging
  * Review agent configuration


## Process Flow
If process flow is unclear:
  * Verify task dependencies
  * Check agent roles and goals
  * Review task descriptions


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your problem descriptions are clear and provide sufficient context for the reasoning agents.
Was this page helpful?
YesNo
Reasoning Extract AgentsMultimodal Agents
On this page
  * Quick Start
  * Understanding Reasoning
  * Features
  * Multi-Agent Reasoning
  * Configuration Options
  * Troubleshooting
  * Next Steps


