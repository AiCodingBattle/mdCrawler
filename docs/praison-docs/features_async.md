PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Async Agents
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
AI Agent
AI Agent
AI Agent
Out
Async AI Agents allow you to run AI tasks asynchronously, improving performance and efficiency in your applications.
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
Set your OpenAI API key as an environment variable:
Copy
```
export OPENAI_API_KEY=your_api_key_here

```

3
Create Project
Create a new file `app.py` with the basic setup:
Copy
```
import asyncio
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create an agent
agent = Agent(
  name="AsyncAgent",
  role="Assistant",
  goal="Help with tasks",
  backstory="Expert in async operations"
)
# Create a task
task = Task(
  name="hello_task",
  description="Say hello and introduce yourself",
  agent=agent,
  async_execution=True,
  expected_output="Answer to the question"
)
# Create agents manager
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  process="sequential"
)
# Main async function
async def main():
  result = await agents.astart()
  print(result)
# Run the program
if __name__ == "__main__":
  asyncio.run(main())

```

4
Run the Program
Run your async AI agent:
Copy
```
python app.py

```

**Requirements**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.
  * Basic understanding of async/await in Python


## 
​
Understanding Async Execution
## What is Asynchronous Execution?
Async execution lets your program continue running while waiting for operations to complete. This is ideal for:
  * Making multiple AI API calls
  * Processing large datasets
  * Handling multiple tasks simultaneously
  * Maintaining responsive applications


Sync
Async
Copy
```
# Synchronous execution (blocks until complete)
result = agent.chat("Hello")

```

## 
​
Features
## Async Tasks
Create tasks that run asynchronously with built-in error handling and retries.
## Parallel Processing
Run multiple tasks in parallel using asyncio.gather().
## Mixed Mode
Mix sync and async tasks in the same workflow seamlessly.
## Resource Management
Built-in resource management and performance optimization.
## 
​
Advanced Usage
  * Code
  * No Code


### Async Tasks with Callbacks and Tools Example Code
Copy
```
import asyncio
import time
from typing import List, Dict
from praisonaiagents import Agent, Task, PraisonAIAgents, TaskOutput
from duckduckgo_search import DDGS
from pydantic import BaseModel
# 1. Define async tool
class SearchResult(BaseModel):
  query: str
  results: List[Dict[str, str]]
  total_results: int
async def async_search_tool(query: str) -> Dict:
  """
  Asynchronous search using DuckDuckGo.
  Args:
    query (str): The search query.
  Returns:
    dict: Search results in SearchResult model format
  """
  await asyncio.sleep(1) # Simulate network delay
  try:
    results = []
    ddgs = DDGS()
    for result in ddgs.text(keywords=query, max_results=5):
      results.append({
        "title": result.get("title", ""),
        "url": result.get("href", ""),
        "snippet": result.get("body", "")
      })
    
    # Format response to match SearchResult model
    return {
      "query": query,
      "results": results,
      "total_results": len(results)
    }
  except Exception as e:
    print(f"Error during async search: {e}")
    return {
      "query": query,
      "results": [],
      "total_results": 0
    }
# 2. Define async callback
async def async_callback(output: TaskOutput):
  await asyncio.sleep(1) # Simulate processing
  if output.output_format == "JSON":
    print(f"Processed JSON result: {output.json_dict}")
  elif output.output_format == "Pydantic":
    print(f"Processed Pydantic result: {output.pydantic}")
# 3. Create specialized agents
async_agent = Agent(
  name="AsyncSearchAgent",
  role="Asynchronous Search Specialist",
  goal="Perform fast and efficient asynchronous searches with structured results",
  backstory="Expert in parallel search operations and data retrieval",
  tools=[async_search_tool],
  self_reflect=False,
  verbose=True,
  markdown=True
)
summary_agent = Agent(
  name="SummaryAgent",
  role="Research Synthesizer",
  goal="Create comprehensive summaries and identify patterns across multiple search results",
  backstory="""Expert in analyzing and synthesizing information from multiple sources.
Skilled at identifying patterns, trends, and connections between different topics.
Specializes in creating clear, structured summaries that highlight key insights.""",
  self_reflect=True, # Enable self-reflection for better summary quality
  verbose=True,
  markdown=True
)
# 4. Create async tasks
async_task = Task(
  name="async_search",
  description="""Search for 'Async programming' and return results in the following JSON format:
{
  "query": "the search query",
  "results": [
    {
      "title": "result title",
      "url": "result url",
      "snippet": "result snippet"
    }
  ],
  "total_results": number of results
}""",
  expected_output="SearchResult model with query details and results",
  agent=async_agent,
  async_execution=True,
  callback=async_callback,
  output_pydantic=SearchResult
)
# 5. Example usage functions
async def run_single_task():
  """Run single async task"""
  print("\nRunning Single Async Task...")
  agents = PraisonAIAgents(
    agents=[async_agent],
    tasks=[async_task],
    verbose=1,
    process="sequential"
  )
  result = await agents.astart()
  print(f"Single Task Result: {result}")
async def run_parallel_tasks():
  """Run multiple async tasks in parallel"""
  print("\nRunning Parallel Async Tasks...")
  
  # Define different search topics
  search_topics = [
    "Latest AI Developments 2024",
    "Machine Learning Best Practices",
    "Neural Networks Architecture"
  ]
  
  # Create tasks for different topics
  parallel_tasks = [
    Task(
      name=f"search_task_{i}",
      description=f"""Search for '{topic}' and return results in the following JSON format:
{{
  "query": "{topic}",
  "results": [
    {{
      "title": "result title",
      "url": "result url",
      "snippet": "result snippet"
    }}
  ],
  "total_results": number of results
}}""",
      expected_output="SearchResult model with detailed information",
      agent=async_agent,
      async_execution=True,
      callback=async_callback,
      output_pydantic=SearchResult
    ) for i, topic in enumerate(search_topics)
  ]
  
  # Create summarization task with the specialized summary agent
  summary_task = Task(
    name="summary_task",
    description="""As a Research Synthesizer, analyze the search results and create a comprehensive summary. Your task:
1. Analyze Results:
  - Review all search results thoroughly
  - Extract key findings from each topic
  - Identify main themes and concepts
2. Find Connections:
  - Identify relationships between topics
  - Spot common patterns or contradictions
  - Note emerging trends across sources
3. Create Structured Summary:
  - Main findings per topic
  - Cross-cutting themes
  - Emerging trends
  - Practical implications
  - Future directions
4. Quality Checks:
  - Ensure all topics are covered
  - Verify accuracy of connections
  - Confirm clarity of insights
  - Validate practical relevance
Present the summary in a clear, structured format with sections for findings, patterns, trends, and implications.""",
    expected_output="""A comprehensive research synthesis containing:
- Detailed findings from each search topic
- Cross-topic patterns and relationships
- Emerging trends and their implications
- Practical applications and future directions""",
    agent=summary_agent, # Use the specialized summary agent
    async_execution=False, # Run synchronously after search tasks
    callback=async_callback
  )
  
  # Create a single PraisonAIAgents instance with both agents
  agents = PraisonAIAgents(
    agents=[async_agent, summary_agent], # Include both agents
    tasks=parallel_tasks + [summary_task], # Include all tasks
    verbose=1,
    process="sequential" # Tasks will run in sequence, with parallel tasks running first
  )
  
  # Run all tasks
  results = await agents.astart()
  print(f"Tasks Results: {results}")
  
  # Return results in a serializable format
  return {
    "search_results": {
      "task_status": {k: v for k, v in results["task_status"].items() if k != summary_task.id},
      "task_results": [str(results["task_results"][i]) if results["task_results"][i] else None 
              for i in range(len(parallel_tasks))]
    },
    "summary": str(results["task_results"][summary_task.id]) if results["task_results"].get(summary_task.id) else None,
    "topics": search_topics
  }
# 6. Main execution
async def main():
  """Main execution function"""
  print("Starting Async AI Agents Examples...")
  
  try:
    # Run different async patterns
    await run_single_task()
    await run_parallel_tasks()
  except Exception as e:
    print(f"Error in main execution: {e}")
if __name__ == "__main__":
  # Run the main function
  asyncio.run(main())

```

### 1. Async Tasks with Callbacks
Task
Callback
Copy
```
# Create an async task with callback
async_task = Task(
  name="weather_task",
  description="Check weather conditions",
  agent=agent,
  async_execution=True,
  callback=async_callback
)

```

### 2. Parallel Task Processing
Be mindful of rate limits and resource usage when processing tasks in parallel.
Copy
```
async def process_multiple_tasks():
  tasks = [
    Task(
      name=f"task_{i}",
      description=f"Process item {i}",
      async_execution=True
    ) for i in range(5)
  ]
  
  results = await asyncio.gather(
    *[agent.achat(task.description) for task in tasks]
  )
  return results

```

## 
​
Best Practices
Error Handling
Copy
```
async def safe_async_operation():
  try:
    result = await agent.achat("Process this")
    return result
  except Exception as e:
    logging.error(f"Error: {e}")
    return None

```

Resource Management
Copy
```
async def efficient_processing():
  semaphore = asyncio.Semaphore(5)
  async with semaphore:
    result = await agent.achat("Process within limits")
  return result

```

Performance Tips
  * Use `asyncio.gather()` for parallel operations
  * Implement proper error handling
  * Monitor memory usage
  * Use timeouts for long-running operations


## 
​
Troubleshooting
## ChatCompletion Error
If you see “ChatCompletion can’t be used in await expression”:
  * Use AsyncOpenAI() client
  * Ensure proper async context


## Event Loop Error
If you get “Event loop is closed”:
  * Use asyncio.run() for main entry
  * Check async context


## 
​
API Reference
### 
​
Async Methods
achat()
async
Async version of chat method
aexecute_tool()
async
Async tool execution method
astart()
async
Async task execution starter
### 
​
Task Properties
async_execution
boolean
Enable/disable async mode for tasks
callback
function
Set sync or async callback function
## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
Remember to handle errors properly, manage resources efficiently, and test thoroughly in async contexts.
Was this page helpful?
YesNo
LangChain AgentsMini AI Agents
On this page
  * Quick Start
  * Understanding Async Execution
  * Features
  * Advanced Usage
  * Best Practices
  * Troubleshooting
  * API Reference
  * Async Methods
  * Task Properties
  * Next Steps


