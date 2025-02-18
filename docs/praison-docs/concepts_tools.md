PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Core Concepts
AI Agents with Tools
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


Agents
Tools
Agent 1
Agent 2
Agent 3
Internet Search
Code Execution
Formatting
Input
Output
Feature| Knowledge| Tools  
---|---|---  
Purpose| Static reference information| Dynamic interaction capabilities  
Access| Read-only reference| Execute actions and commands  
Updates| Manual through files| Real-time through tool calls  
Storage| Knowledge base| Assigned to specific agents  
Persistence| Permanent until changed| Available during agent execution  
## 
​
Quick Start
Tools are functions that agents can use to interact with external systems and perform actions. They are essential for creating agents that can do more than just process text.
## 
​
Creating Custom Tool
1
Create any function that you want to use as a tool, that performs a specific task.
Copy
```
from duckduckgo_search import DDGS
from typing import List, Dict
# Tool Implementation
def internet_search_tool(query: str) -> List[Dict]:
  """
  Perform Internet Search using DuckDuckGo
  
  Args:
    query (str): The search query string
    
  Returns:
    List[Dict]: List of search results containing title, URL, and snippet
  """
  results = []
  ddgs = DDGS()
  for result in ddgs.text(keywords=query, max_results=5):
    results.append({
      "title": result.get("title", ""),
      "url": result.get("href", ""),
      "snippet": result.get("body", "")
    })
  return results

```

2
Assign the tool to an agent
Copy
```
  data_agent = Agent(
    name="DataCollector",
    role="Search Specialist",
    goal="Perform internet searches to collect relevant information.",
    backstory="Expert in finding and organising internet data.",
    tools=[internet_search_tool], ## Add the tool to the agent i.e the function name
  )

```

## That's it!
You have created a custom tool and assigned it to an agent.
## 
​
Implementing Tools Full Code Example
  * Code
  * No Code


1
Install PraisonAI
Install the core package:
Terminal
Copy
```
pip install praisonaiagents duckduckgo-search

```

2
Configure Environment
Terminal
Copy
```
export OPENAI_API_KEY=your_openai_key

```

Generate your OpenAI API key from OpenAI Use other LLM providers like Ollama, Anthropic, Groq, Google, etc. Please refer to the Models for more information.
3
Create Agent with Tool
Create `app.py`
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
from duckduckgo_search import DDGS
from typing import List, Dict
# 1. Tool Implementation
def internet_search_tool(query: str) -> List[Dict]:
  """
  Perform Internet Search using DuckDuckGo
  
  Args:
    query (str): The search query string
    
  Returns:
    List[Dict]: List of search results containing title, URL, and snippet
  """
  results = []
  ddgs = DDGS()
  for result in ddgs.text(keywords=query, max_results=5):
    results.append({
      "title": result.get("title", ""),
      "url": result.get("href", ""),
      "snippet": result.get("body", "")
    })
  return results
# 2. Assign the tool to an agent
data_agent = Agent(
  name="DataCollector",
  role="Search Specialist",
  goal="Perform internet searches to collect relevant information.",
  backstory="Expert in finding and organising internet data.",
  tools=[internet_search_tool],
  self_reflect=False
)
# 3. Task Definition
collect_task = Task(
  description="Perform an internet search using the query: 'AI job trends in 2024'. Return results as a list of title, URL, and snippet.",
  expected_output="List of search results with titles, URLs, and snippets.",
  agent=data_agent,
  name="collect_data",
)
# 4. Start Agents
agents = PraisonAIAgents(
  agents=[data_agent],
  tasks=[collect_task],
  process="sequential"
)
agents.start()

```

4
Start Agents
Execute your script:
Terminal
Copy
```
python app.py

```

## 
​
In-build Tools in PraisonAI
## Search Tools
Tools for searching and retrieving information from various sources
## Python Tools
Essential Python utilities for data manipulation and scripting
## Spider Tools
Web crawling and scraping capabilities for data extraction
## Arxiv Tools
Access and search academic papers from arXiv repository
## Newspaper Tools
Extract and parse content from news articles and websites
## DuckDB Tools
Fast analytical SQL database operations and queries
## DuckDuckGo Tools
Web search functionality using DuckDuckGo’s API
## Calculator Tools
Perform mathematical calculations and conversions
## YAML Tools
Parse and manipulate YAML format data
## JSON Tools
Handle JSON data structures and operations
## Pandas Tools
Data analysis and manipulation using Pandas
## YFinance Tools
Fetch financial market data from Yahoo Finance
## Shell Tools
Execute shell commands and system operations
## Wikipedia Tools
Access and search Wikipedia articles and data
## XML Tools
Process and manipulate XML format data
## File Tools
File system operations and management utilities
## Excel Tools
Work with Excel spreadsheets and workbooks
## CSV Tools
Handle CSV file operations and transformations
## 
​
Tools Overview
## Search Tools
Tools for searching and retrieving information from various sources
## File Tools
Tools for reading, writing, and manipulating files
## API Tools
Tools for interacting with external APIs and services
## 
​
Advanced Tool Features
### 
​
Tool Configuration
Copy
```
def configured_tool(
  query: str,
  max_results: int = 5,
  timeout: int = 10
) -> List[Dict]:
  """
  Example of a configurable tool
  
  Args:
    query (str): Search query
    max_results (int): Maximum number of results
    timeout (int): Request timeout in seconds
    
  Returns:
    List[Dict]: Search results
  """
  # Tool implementation
  pass

```

### 
​
Tool Chaining
Copy
```
def chain_tools(input_data: str) -> Dict:
  """
  Example of chaining multiple tools
  
  Args:
    input_data (str): Input data
    
  Returns:
    Dict: Processed results
  """
  # 1. Search for data
  search_results = internet_search_tool(input_data)
  
  # 2. Process results
  processed_data = process_tool(search_results)
  
  # 3. Format output
  return format_tool(processed_data)

```

### 
​
Tool Categories
## Data Collection Tools
  * Web scraping
  * API integration
  * Database queries


## Processing Tools
  * Data transformation
  * Text analysis
  * Image processing


## Output Tools
  * File generation
  * Report creation
  * Data visualization


## 
​
Tool Integration
### 
​
Adding Tools to Agents
Copy
```
# Multiple tools
agent = Agent(
  name="MultiTool Agent",
  tools=[
    internet_search_tool,
    file_processing_tool,
    api_integration_tool
  ]
)

```

### 
​
Tool Dependencies
Copy
```
# Tool with dependencies
def advanced_tool(data: Dict) -> Dict:
  """
  Tool that depends on external libraries
  
  Args:
    data (Dict): Input data
    
  Returns:
    Dict: Processed data
  """
  try:
    import required_library
    # Tool implementation
    return processed_result
  except ImportError:
    raise Exception("Required library not installed")

```

## 
​
Tool Guidelines
## Best Practices
  1. **Type Hints**
     * Use Python type hints
     * Define clear input/output types
     * Document complex types
  2. **Documentation**
     * Write clear docstrings
     * Explain parameters
     * Provide usage examples
  3. **Error Handling**
     * Handle exceptions gracefully
     * Return meaningful errors
     * Validate inputs


## Tool Types
  1. **Search Tools**
     * Web search
     * Database queries
     * Document search
  2. **File Tools**
     * Read/write operations
     * File conversion
     * Data extraction
  3. **API Tools**
     * REST API calls
     * GraphQL queries
     * Service integration


## 
​
Best Practices Summary
Following these best practices will help you create robust, efficient, and secure tools in PraisonAI.
## Design Principles
Single Responsibility
Each tool should have one clear purpose and do it well. Avoid creating tools that try to do too many things.
Copy
```
# Good Example
def process_image(image: np.array) -> np.array:
  return processed_image
# Avoid
def process_and_save_and_upload(image):
  # Too many responsibilities
  pass

```

Clear Interfaces
Define explicit input/output types and maintain consistent parameter naming.
Copy
```
def search_tool(
  query: str,
  max_results: int = 10
) -> List[Dict[str, Any]]:
  """
  Search for information with clear parameters
  """
  pass

```

Documentation
Always include detailed docstrings and type hints.
Copy
```
def analyze_text(
  text: str,
  language: str = "en"
) -> Dict[str, float]:
  """
  Analyze text sentiment and emotions.
  
  Args:
    text: Input text to analyze
    language: ISO language code
    
  Returns:
    Dict with sentiment scores
  """
  pass

```

## Performance Optimization
Efficient Processing
Optimize resource usage and processing time.
Copy
```
# Use generators for large datasets
def process_large_data():
  for chunk in data_generator():
    yield process_chunk(chunk)

```

Resource Management
Properly handle resource allocation and cleanup.
Copy
```
async with aiohttp.ClientSession() as session:
  # Resource automatically managed
  await process_data(session)

```

Caching
Implement caching for frequently accessed data.
Copy
```
@cache.memoize(timeout=300)
def expensive_operation(data: str) -> Dict:
  return process_expensive(data)

```

Async Operations
Use async/await for I/O-bound operations.
Copy
```
async def fetch_data(urls: List[str]):
  async with aiohttp.ClientSession() as session:
    tasks = [fetch_url(session, url) for url in urls]
    return await asyncio.gather(*tasks)

```

## Security Best Practices
Input Validation
Always validate and sanitize inputs to prevent security vulnerabilities.
Copy
```
def process_user_input(data: str) -> str:
  if not isinstance(data, str):
    raise ValueError("Input must be string")
  return sanitize_input(data.strip())

```

Rate Limiting
Implement rate limiting for API calls to prevent abuse.
Copy
```
@rate_limit(calls=100, period=60)
async def api_call():
  return await make_request()

```

API Key Management
Securely handle API keys and credentials using environment variables.
Copy
```
# Use environment variables
api_key = os.getenv('API_KEY')
if not api_key:
  raise ConfigError("API key not found")

```

Error Masking
Hide sensitive information in error messages to prevent information leakage.
Copy
```
try:
  result = process_sensitive_data()
except Exception as e:
  # Log detailed error internally
  logger.error(f"Detailed error: {str(e)}")
  # Return sanitized error to user
  raise PublicError("Processing failed")

```

**Pro Tip** : Start with these practices from the beginning of your project. It’s easier to maintain good practices than to retrofit them later.
Was this page helpful?
YesNo
ProcessMemory
On this page
  * Quick Start
  * Creating Custom Tool
  * Implementing Tools Full Code Example
  * In-build Tools in PraisonAI
  * Tools Overview
  * Advanced Tool Features
  * Tool Configuration
  * Tool Chaining
  * Tool Categories
  * Tool Integration
  * Adding Tools to Agents
  * Tool Dependencies
  * Tool Guidelines
  * Best Practices Summary


