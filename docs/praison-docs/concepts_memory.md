PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Core Concepts
AI Agents with Memory
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
Agent 1
Agent 2
Agent 3
Store
Vector DB
Memory
Short Term
Long Term
Input
Output
Feature| Knowledge| Memory  
---|---|---  
When Used| Pre-loaded before agent execution| Created and updated during runtime  
Purpose| Provide static reference information| Store dynamic context and interactions  
Storage| Read-only knowledge base| Read-write memory store  
Persistence| Permanent until explicitly changed| Can be temporary (STM) or persistent (LTM)  
Updates| Manual updates through knowledge files| Automatic updates during agent execution  
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
pip install "praisonaiagents[memory]" duckduckgo_search 

```

duckduckgo_search is a tool that allows agents to search the web. It is required for the multiple agents example shown below.
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
Single Agent
Multiple Agents
Copy
```
from praisonaiagents.agents.agents import Agent, Task, PraisonAIAgents
# Create blog writer agent
blog_agent = Agent(
  role="Blog Writer",
  goal="Write a blog post about AI",
  backstory="Expert at writing blog posts",
  llm="gpt-4o-mini"
)
# Create blog writing task
blog_task = Task(
  description="Write a blog post about AI trends",
  expected_output="Well-written blog post about AI trends",
  agent=blog_agent
)
# Create and start the agents with memory enabled
agents = PraisonAIAgents(
  agents=[blog_agent],
  tasks=[blog_task],
  memory=True
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
Understanding Memory
## What is Agent Memory?
Memory in AI agents enables them to:
  * Maintain context across multiple tasks
  * Remember previous interactions and findings
  * Build upon past knowledge
  * Share information between agents
  * Create more coherent and contextual responses


## 
​
Features
## Context Retention
Maintain information across multiple interactions.
## Information Sharing
Share knowledge between multiple agents.
## Long-term Storage
Store and retrieve information over extended periods.
## Memory Types
Support for different memory types (short-term, long-term).
## 
​
Multi-Agent Memory
  * Code
  * No Code


Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
from praisonaiagents.tools import duckduckgo
# Create first agent for research
researcher = Agent(
  role="Research Analyst",
  goal="Research and analyze market trends",
  backstory="Expert in market research and data analysis",
  tools=[duckduckgo],
  verbose=True
)
# Create second agent for report writing
writer = Agent(
  role="Report Writer",
  goal="Create comprehensive market reports",
  backstory="Expert in technical writing and report creation",
  verbose=True
)
# Create research task
research_task = Task(
  description="Research current market trends",
  expected_output="Detailed market analysis",
  agent=researcher
)
# Create writing task
report_task = Task(
  description="Create a market report based on research",
  expected_output="Comprehensive market report",
  agent=writer
)
# Create and start the agents with memory
agents = PraisonAIAgents(
  agents=[researcher, writer],
  tasks=[research_task, report_task],
  memory=True,
  process="sequential"
)
# Start execution
result = agents.start()

```

### 
​
Configuration Options
Copy
```
# Create an agent with memory configuration
agent = Agent(
  role="Research Analyst",
  goal="Research and retain information",
  backstory="Expert in research and analysis",
  tools=[duckduckgo],
  verbose=True, # Enable detailed logging
  llm="gpt-4o" # Language model to use
)
# Create agents with memory options
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  memory=True, # Enable memory
  memory_config={
    "provider": "rag", # Use RAG for semantic search
    "use_embedding": True, # Enable embeddings for better search
    "short_db": ".praison/short_term.db", # Path for short-term memory
    "long_db": ".praison/long_term.db",  # Path for long-term memory
    "rag_db_path": ".praison/chroma_db"  # Path for vector database
  }
)

```

## 
​
Troubleshooting
## Memory Issues
If memory isn’t working as expected:
  * Check memory configuration
  * Enable verbose mode for debugging
  * Verify memory provider settings


## Context Flow
If context isn’t being maintained:
  * Review task dependencies
  * Check memory configuration
  * Verify agent communication


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, configure memory settings based on your specific use case requirements and expected interaction patterns.
### 
​
Memory Configuration Options
The memory system in PraisonAI supports various configuration options to customize how agents store and retrieve information:
Copy
```
memory_config = {
  # Memory Provider
  "provider": "rag",    # Options: "rag", "mem0", "none"
  "use_embedding": True,  # Enable semantic search with embeddings
  
  # Storage Paths
  "short_db": ".praison/short_term.db", # Short-term memory SQLite DB
  "long_db": ".praison/long_term.db",  # Long-term memory SQLite DB
  "rag_db_path": ".praison/chroma_db",  # Vector database path
  
  # Memory Settings
  "ttl": 3600,       # Time to live for memory items (in seconds)
  
  # Optional Mem0 Config (if using mem0 provider)
  "config": {
    "api_key": "...",  # Mem0 API key
    "org_id": "...",   # Organization ID
    "project_id": "..." # Project ID
  }
}
# Create agents with memory configuration
agents = PraisonAIAgents(
  agents=[agent],
  tasks=[task],
  memory=True,
  memory_config=memory_config
)

```

### 
​
Memory Types
PraisonAI’s memory system includes several types of memory:
## Short-term Memory
  * Temporary storage for current context
  * Automatically cleared between sessions
  * Fast access for immediate task context


## Long-term Memory
  * Persistent storage for important information
  * Semantic search capabilities with RAG
  * Quality-based storage decisions


### 
​
Memory Quality Control
PraisonAI includes built-in quality control for memory storage:
Copy
```
# Example of storing with quality metrics
agents.memory.store_long_term(
  text="Important information to remember",
  metadata={
    "task_id": "task_123",
    "agent": "research_agent"
  },
  completeness=0.9,  # How complete is the information
  relevance=0.85,   # How relevant to the task
  clarity=0.95,    # How clear and well-structured
  accuracy=0.9,    # How accurate is the information
  weights={      # Custom weights for quality score
    "completeness": 0.3,
    "relevance": 0.3,
    "clarity": 0.2,
    "accuracy": 0.2
  }
)
# Search with quality filter
results = agents.memory.search_long_term(
  query="search query",
  min_quality=0.8,   # Only return high-quality matches
  limit=5       # Maximum number of results
)

```

Was this page helpful?
YesNo
ToolsKnowledge
On this page
  * Quick Start
  * Understanding Memory
  * Features
  * Multi-Agent Memory
  * Configuration Options
  * Troubleshooting
  * Next Steps
  * Memory Configuration Options
  * Memory Types
  * Memory Quality Control


