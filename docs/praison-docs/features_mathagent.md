PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Math AI Agent
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
First, install the PraisonAI Agents package:
Copy
```
pip install praisonaiagents sympy pint

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
from praisonaiagents.tools import (
  evaluate, solve_equation, convert_units,
  calculate_statistics, calculate_financial
)
# Create math agent
math_agent = Agent(
  role="Math Expert",
  goal="Perform complex mathematical calculations",
  backstory="Expert in mathematical computations and analysis",
  tools=[
    evaluate, solve_equation, convert_units,
    calculate_statistics, calculate_financial
  ],
  verbose=True
)
# Create a task
task = Task(
  description="Calculate compound interest and statistical analysis",
  expected_output="Detailed mathematical analysis",
  agent=math_agent
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[math_agent],
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
  * sympy and pint packages (automatically installed when needed)


## 
​
Understanding Math Agents
## What are Math Agents?
Math agents are specialized AI agents that can:
  * Evaluate mathematical expressions
  * Solve equations and systems of equations
  * Perform unit conversions
  * Calculate statistical metrics
  * Handle financial calculations


## 
​
Features
## Expression Evaluator
Evaluates mathematical expressions and formulas.
## Equation Solver
Solves mathematical equations and systems.
## Unit Converter
Converts between different units of measurement.
## Statistical Calculator
Calculates statistical metrics and analysis.
## 
​
Multi-Agent AI Math Analysis
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
from praisonaiagents import Agent, Task, PraisonAIAgents
from praisonaiagents.tools import (
  evaluate, solve_equation, convert_units,
  calculate_statistics, calculate_financial
)
# Create first agent for calculations
calculator = Agent(
  role="Mathematical Calculator",
  goal="Perform complex calculations and analysis",
  backstory="Expert in mathematical computations",
  tools=[evaluate, solve_equation, convert_units],
  verbose=True
)
# Create second agent for statistics
statistician = Agent(
  role="Statistical Analyst",
  goal="Perform statistical analysis and interpretation",
  backstory="Expert in statistical analysis",
  tools=[calculate_statistics, calculate_financial],
  verbose=True
)
# Create first task
calc_task = Task(
  description="Calculate compound interest for $10000 at 5% for 3 years",
  expected_output="Detailed interest calculation",
  agent=calculator
)
# Create second task
stats_task = Task(
  description="Analyze the monthly interest distribution",
  expected_output="Statistical analysis of interest data",
  agent=statistician
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[calculator, statistician],
  tasks=[calc_task, stats_task],
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
# Create an agent with advanced math configuration
agent = Agent(
  role="Math Expert",
  goal="Perform complex mathematical analysis",
  backstory="Expert in mathematical computations",
  tools=[
    evaluate,
    solve_equation,
    convert_units,
    calculate_statistics,
    calculate_financial
  ],
  verbose=True, # Enable detailed logging
  llm="gpt-4o" # Language model to use
)

```

## 
​
Troubleshooting
## Expression Errors
If expressions are not evaluating:
  * Check syntax and formatting
  * Verify variable definitions
  * Enable verbose mode for debugging


## Calculation Issues
If calculations are incorrect:
  * Review input formats
  * Check unit compatibility
  * Verify formula structure


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure mathematical expressions and units are properly formatted for your specific use case.
Was this page helpful?
YesNo
Code AgentStructured AI Agents
On this page
  * Quick Start
  * Understanding Math Agents
  * Features
  * Multi-Agent AI Math Analysis
  * Configuration Options
  * Troubleshooting
  * Next Steps


