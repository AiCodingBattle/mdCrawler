PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
AI Agents with Callbacks
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
Out
Callback
Learn how to implement callbacks to monitor and log AI agent interactions, errors, and task completions.
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
from praisonaiagents import (
  register_display_callback,
  Agent, 
  Task, 
  PraisonAIAgents
)
def simple_callback(message=None, response=None, **kwargs):
  print(f"Received message: {message}")
  print(f"Got response: {response}")
# Register as synchronous callback
register_display_callback('interaction', simple_callback, is_async=False)
# For async callbacks
async def async_simple_callback(message=None, response=None, **kwargs):
  await asyncio.sleep(0) # Non-blocking pause
  print(f"Received message: {message}")
  print(f"Got response: {response}")
# Register as async callback
register_display_callback('interaction', async_simple_callback, is_async=True)
# Create an agent
agent = Agent(
  name="MyAgent",
  role="Assistant",
  goal="Help with tasks",
  backstory="I am a helpful assistant",
  verbose=True # Enable verbose mode to see callbacks in action
)
# Create a task
task = Task(
  name="simple_task",
  description="Say hello",
  agent=agent,
  expected_output="A greeting"
)
# Run the agent
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task]
)
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
  * Basic understanding of Python functions


## 
​
Understanding Callbacks
## What are Callbacks?
Callbacks are functions that get called automatically when specific events occur in your AI agents:
  * Interactions between user and agent
  * Error messages
  * Tool calls
  * Self-reflection moments
  * Task completion
  * Generation progress


## 
​
Features
## Interaction Callback
Triggered when the agent interacts with users
## Error Callback
Called when errors occur
## Tool Call Callback
Activated when tools are used
## Self Reflection Callback
Triggered during agent self-reflection
## Instruction Callback
Called when instructions are processed
## Generating Callback
Activated during content generation
## 
​
Basic Implementation
### 
​
1. Simple Logging Callback
  * Code
  * No Code


Basic
Advanced
Copy
```
import logging
# Setup logging
logging.basicConfig(level=logging.INFO)
def log_callback(message=None, **kwargs):
  logging.info(f"Agent message: {message}")
# Register synchronous callback
register_display_callback('interaction', log_callback, is_async=False)
# Register asynchronous callback
async def async_log_callback(message=None, **kwargs):
  await asyncio.sleep(0)
  logging.info(f"Agent message: {message}")
# Register as async callback
register_display_callback('interaction', async_log_callback, is_async=True)

```

### 
​
2. Multiple Callback Types
  * Code
  * No Code


Copy
```
# Error callback
def error_callback(message=None):
  logging.error(f"Error occurred: {message}")
# Tool call callback
def tool_callback(message=None):
  logging.info(f"Tool called: {message}")
# Register multiple callbacks
register_display_callback('error', error_callback)
register_display_callback('tool_call', tool_callback)

```

## 
​
Complete Example
Here’s a full implementation showing all callback types and proper logging:
  * Code
  * No Code


Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents, register_display_callback
import logging
from datetime import datetime
# Setup logging
logging.basicConfig(
  filename='ai_interactions.log',
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# Interaction callback
def interaction_callback(message=None, response=None, markdown=None, generation_time=None):
  logging.info(f"""
  === INTERACTION ===
  Time: {datetime.now()}
  Generation Time: {generation_time}s
  Message: {message}
  Response: {response}
  Markdown: {markdown}
  """)
# Error callback
def error_callback(message=None):
  logging.error(f"""
  === ERROR ===
  Time: {datetime.now()}
  Message: {message}
  """)
# Tool call callback
def tool_call_callback(message=None):
  logging.info(f"""
  === TOOL CALL ===
  Time: {datetime.now()}
  Message: {message}
  """)
# Register callbacks
register_display_callback('interaction', interaction_callback)
register_display_callback('error', error_callback)
register_display_callback('tool_call', tool_call_callback)
agent = Agent(
  name="CallbackAgent",
  role="Assistant",
  goal="Demonstrate callbacks",
  backstory="I am a helpful assistant",
  verbose=True
)
task = Task(
  name="callback_task",
  description="Show how callbacks work",
  agent=agent,
  expected_output="Demonstration complete"
)
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  verbose=True
)
agents.start()

```

## 
​
Advanced Examples
  * All callback types
  * Comprehensive logging
  * Task callbacks
  * Tool integration
  * Multiple agents


  * Code
  * No Code


Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents, error_logs, register_display_callback
from duckduckgo_search import DDGS
from rich.console import Console
import json
from datetime import datetime
import logging
# Setup logging
logging.basicConfig(
  filename='ai_interactions.log',
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# Callback functions for different display types
def interaction_callback(message=None, response=None, markdown=None, generation_time=None):
  """Callback for display_interaction"""
  logging.info(f"""
  === INTERACTION ===
  Time: {datetime.now()}
  Generation Time: {generation_time}s
  Message: {message}
  Response: {response}
  Markdown: {markdown}
  """)
def error_callback(message=None):
  """Callback for display_error"""
  logging.error(f"""
  === ERROR ===
  Time: {datetime.now()}
  Message: {message}
  """)
def tool_call_callback(message=None):
  """Callback for display_tool_call"""
  logging.info(f"""
  === TOOL CALL ===
  Time: {datetime.now()}
  Message: {message}
  """)
def instruction_callback(message=None):
  """Callback for display_instruction"""
  logging.info(f"""
  === INSTRUCTION ===
  Time: {datetime.now()}
  Message: {message}
  """)
def self_reflection_callback(message=None):
  """Callback for display_self_reflection"""
  logging.info(f"""
  === SELF REFLECTION ===
  Time: {datetime.now()}
  Message: {message}
  """)
def generating_callback(content=None, elapsed_time=None):
  """Callback for display_generating"""
  logging.info(f"""
  === GENERATING ===
  Time: {datetime.now()}
  Content: {content}
  Elapsed Time: {elapsed_time}
  """)
# Register all callbacks
register_display_callback('interaction', interaction_callback)
register_display_callback('error', error_callback)
register_display_callback('tool_call', tool_call_callback)
register_display_callback('instruction', instruction_callback)
register_display_callback('self_reflection', self_reflection_callback)
# register_display_callback('generating', generating_callback)
def task_callback(output):
  """Callback for task completion"""
  logging.info(f"""
  === TASK COMPLETED ===
  Time: {datetime.now()}
  Description: {output.description}
  Agent: {output.agent}
  Output: {output.raw[:200]}...
  """)
def internet_search_tool(query) -> list:
  """
  Perform a search using DuckDuckGo.
  Args:
    query (str): The search query.
  Returns:
    list: A list of search result titles and URLs.
  """
  try:
    results = []
    ddgs = DDGS()
    for result in ddgs.text(keywords=query, max_results=10):
      results.append({
        "title": result.get("title", ""),
        "url": result.get("href", ""),
        "snippet": result.get("body", "")
      })
    return results
  except Exception as e:
    print(f"Error during DuckDuckGo search: {e}")
    return []
def main():
  # Create agents
  researcher = Agent(
    name="Researcher",
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI and data science",
    backstory="""You are an expert at a technology research group, 
    skilled in identifying trends and analyzing complex data.""",
    verbose=True,
    allow_delegation=False,
    tools=[internet_search_tool],
    llm="gpt-4o",
    markdown=True,
    reflect_llm="gpt-4o",
    min_reflect=2,
    max_reflect=4
  )
  
  writer = Agent(
    name="Writer",
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a content strategist known for 
    making complex tech topics interesting and easy to understand.""",
    verbose=True,
    allow_delegation=True,
    llm="gpt-4o",
    tools=[],
    markdown=True
  )
  # Create tasks with callbacks
  task1 = Task(
    name="research_task",
    description="""Analyze 2024's AI advancements. 
    Find major trends, new technologies, and their effects.""",
    expected_output="""A detailed report on 2024 AI advancements""",
    agent=researcher,
    tools=[internet_search_tool],
    callback=task_callback
  )
  task2 = Task(
    name="writing_task",
    description="""Create a blog post about major AI advancements using the insights you have.
    Make it interesting, clear, and suited for tech enthusiasts. 
    It should be at least 4 paragraphs long.""",
    expected_output="A blog post of at least 4 paragraphs",
    agent=writer,
    context=[task1],
    callback=task_callback,
    tools=[]
  )
  task3 = Task(
    name="json_task",
    description="""Create a json object with a title of "My Task" and content of "My content".""",
    expected_output="""JSON output with title and content""",
    agent=researcher,
    callback=task_callback
  )
  task4 = Task(
    name="save_output_task",
    description="""Save the AI blog post to a file""",
    expected_output="""File saved successfully""",
    agent=writer,
    context=[task2],
    output_file='test.txt',
    create_directory=True,
    callback=task_callback
  )
  # Create and run agents manager
  agents = PraisonAIAgents(
    agents=[researcher, writer],
    tasks=[task1, task2, task3, task4],
    verbose=True,
    process="sequential",
    manager_llm="gpt-4o"
  )
  agents.start()
if __name__ == "__main__":
  main()

```

## 
​
Async Callbacks
Async callbacks allow you to handle events asynchronously, which is particularly useful for long-running operations or when dealing with multiple agents simultaneously.
### 
​
Basic Async Callback Implementation
  * Code
  * No Code


Copy
```
import asyncio
from praisonaiagents import register_display_callback
async def async_interaction_callback(message=None, response=None, **kwargs):
  """Async callback for handling interactions"""
  await asyncio.sleep(0) # Non-blocking pause
  print(f"Async processing - Message: {message}")
  print(f"Response: {response}")
# Register the async callback
register_display_callback('interaction', async_interaction_callback)

```

### 
​
Complete Async Example
  * Code
  * No Code


Copy
```
import asyncio
from praisonaiagents import Agent, Task, PraisonAIAgents, register_display_callback
import logging
from datetime import datetime
# Setup async logging
async def setup_async_logging():
  logging.basicConfig(
    filename='async_ai_interactions.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  )
# Async callbacks
async def async_interaction_callback(message=None, response=None, markdown=None, generation_time=None):
  await asyncio.sleep(0)
  logging.info(f"""
  === ASYNC INTERACTION ===
  Time: {datetime.now()}
  Generation Time: {generation_time}s
  Message: {message}
  Response: {response}
  """)
async def async_error_callback(message=None):
  await asyncio.sleep(0)
  logging.error(f"""
  === ASYNC ERROR ===
  Time: {datetime.now()}
  Message: {message}
  """)
# Register async callbacks
register_display_callback('interaction', async_interaction_callback, is_async=True)
register_display_callback('error', async_error_callback, is_async=True)
# Create async task callback
async def async_task_callback(output):
  await asyncio.sleep(0)
  logging.info(f"""
  === ASYNC TASK COMPLETED ===
  Time: {datetime.now()}
  Description: {output.description}
  Agent: {output.agent}
  Output: {output.raw[:200]}...
  """)
async def main():
  await setup_async_logging()
  
  # Create agent with async capabilities
  agent = Agent(
    name="AsyncAgent",
    role="Assistant",
    goal="Demonstrate async callbacks",
    backstory="I am an async-capable assistant",
    verbose=True
  )
  # Create task with async callback
  task = Task(
    name="async_task",
    description="Demonstrate async callbacks",
    agent=agent,
    expected_output="Async demonstration complete",
    callback=async_task_callback
  )
  # Create and run agents with async support
  agents = PraisonAIAgents(
    agents=[agent],
    tasks=[task],
    verbose=True
  )
  await agents.start_async()
if __name__ == "__main__":
  asyncio.run(main())

```

## 
​
Async Display Functions
PraisonAI Agents provides several async versions of display functions, prefixed with ‘a’. Here’s the complete list:
## adisplay_instruction
Copy
```
async def adisplay_instruction(
  message: str, 
  console=None
)

```

Async version for showing instructions.
## adisplay_tool_call
Copy
```
async def adisplay_tool_call(
  message: str, 
  console=None
)

```

Async version for displaying tool calls.
## adisplay_error
Copy
```
async def adisplay_error(
  message: str, 
  console=None
)

```

Async version for error messages.
## adisplay_generating
Copy
```
async def adisplay_generating(
  content: str = "", 
  start_time: Optional[float] = None
)

```

Async version for showing generation progress.
#### 
​
Example Usage
Copy
```
import asyncio
from praisonaiagents import (
  adisplay_interaction,
  adisplay_error,
  adisplay_tool_call
)
async def main():
  # Display an interaction
  await adisplay_interaction(
    message="What's the weather?",
    response="Let me check that for you.",
    generation_time=0.5
  )
  # Display a tool call
  await adisplay_tool_call(
    "Calling weather API for location data..."
  )
  # Handle an error
  try:
    raise Exception("API connection failed")
  except Exception as e:
    await adisplay_error(str(e))
if __name__ == "__main__":
  asyncio.run(main())

```

## 
​
Best Practices
## Error Handling
  * Implement proper error handling
  * Use try-catch blocks
  * Log errors appropriately
  * Handle edge cases


## Performance
  * Keep callbacks lightweight
  * Avoid blocking operations
  * Use async when appropriate
  * Monitor resource usage


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
Remember to handle callbacks efficiently and implement proper error handling to ensure smooth agent operations.
Was this page helpful?
YesNo
Structured AI AgentsChat with PDF
On this page
  * Quick Start
  * Understanding Callbacks
  * Features
  * Basic Implementation
  * 1. Simple Logging Callback
  * 2. Multiple Callback Types
  * Complete Example
  * Advanced Examples
  * Async Callbacks
  * Basic Async Callback Implementation
  * Complete Async Example
  * Async Display Functions
  * Example Usage
  * Best Practices
  * Next Steps


