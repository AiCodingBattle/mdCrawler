PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
RAG Agents
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


Query
Input
RAG Agent
Vector DB
Knowledge Task
Output
A knowledge-centric workflow where RAG (Retrieval Augmented Generation) agents interact with vector databases to store and retrieve information efficiently, enabling sophisticated question-answering and information retrieval capabilities.
## 
​
Quick Start
1
Install Package
Install PraisonAI Agents with knowledge support:
Copy
```
pip install "praisonaiagents[knowledge]"

```

2
Set API Key
Set your OpenAI API key:
Copy
```
export OPENAI_API_KEY=xxxxx

```

3
Create Script
Create a new file `app.py`:
Copy
```
from praisonaiagents import Agent
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["small.pdf"], # Indexing
)
agent.start("What is KAG in one line?") # Retrieval

```

## 
​
Data Indexing and Retrieval Agents
Indexing and Ingestion are relatively the same.
Agents
Agent 1
Agent 2
Agent 3
Vector Store
Vector DB
Input
PDF
TXT
MD
The simplest way to create a knowledge-based agent is without any configuration:
Copy
```
from praisonaiagents import Agent
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["small.pdf"] # Indexing
)
agent.start("What is KAG in one line?") # Retrieval

```

### 
​
Advanced Configuration
For more control over the knowledge base, you can specify a configuration:
Copy
```
from praisonaiagents import Agent
config = {
  "vector_store": {
    "provider": "chroma",
    "config": {
      "collection_name": "praison",
      "path": ".praison",
    }
  }
}
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["small.pdf"], # Indexing
  knowledge_config=config # Configuration
)
agent.start("What is KAG in one line?") # Retrieval

```

### 
​
Multi-Agent Knowledge System
For more complex scenarios, you can create a knowledge-based system with multiple agents:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
import logging
import os
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Define the configuration for the Knowledge instance
config = {
  "vector_store": {
    "provider": "chroma",
    "config": {
      "collection_name": "praison",
      "path": ".praison",
    }
  }
}
# Create an agent with knowledge capabilities
knowledge_agent = Agent(
  name="KnowledgeAgent",
  role="Information Specialist",
  goal="Store and retrieve knowledge efficiently",
  backstory="Expert in managing and utilizing stored knowledge",
  knowledge=["sample.pdf"], # Indexing
  knowledge_config=config, # Configuration
  verbose=True
)
# Define a task for the agent
knowledge_task = Task(
  name="knowledge_task",
  description="Who is Mervin Praison?",
  expected_output="Answer to the question",
  agent=knowledge_agent # Agent
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[knowledge_agent],
  tasks=[knowledge_task],
  process="sequential",
  user_id="user1" # User ID
)
# Start execution
result = agents.start() # Retrieval

```

## 
​
Retrieval Agents
Retrieval is the process of querying the vector database for information. Considering there is data already in the Vector Database.
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
Create a new file `rag_agent.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
# Define the configuration for the Knowledge instance
config = {
  "vector_store": {
    "provider": "chroma",
    "config": {
      "collection_name": "praison",
      "path": ".praison"
    }
  }
}
# Create an agent
rag_agent = Agent(
  name="RAG Agent",
  role="Information Specialist",
  goal="Retrieve knowledge efficiently",
  llm="gpt-4o-mini"
)
# Define a task for the agent
rag_task = Task(
  name="RAG Task",
  description="What is KAG?",
  expected_output="Answer to the question",
  agent=rag_agent,
  context=[config] # Retrieval : Vector Database provided as context
)
# Build Agents
agents = PraisonAIAgents(
  agents=[rag_agent],
  tasks=[rag_task],
  user_id="user1"
)
# Start Agents
agents.start()

```

4
Start Agents
Type this in your terminal to run your agents:
Copy
```
python rag_agent.py

```

**Requirements**
  * Python 3.10 or higher
  * OpenAI API key. Generate OpenAI API key here. Use Other models using this guide.
  * ChromaDB or other supported vector database


### 
​
Adding Knowledge to RAG Agents
Copy
```
from praisonaiagents import Agent
config = {
  "vector_store": {
    "provider": "chroma",
    "config": {
      "collection_name": "praison",
      "path": ".praison",
    }
  }
}
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["small.pdf"], # Indexing
  knowledge_config=config # Configuration
)
agent.start("What is KAG in one line?") # Retrieval

```

## 
​
Understanding RAG Agents
## What are RAG Agents?
RAG (Retrieval Augmented Generation) agents enable:
  * Efficient knowledge retrieval
  * Semantic search capabilities
  * Persistent knowledge storage
  * Context-aware responses


## 
​
Features
## RAG Architecture
Store and manage vector embeddings efficiently.
## Semantic Search
Find relevant information using semantic similarity.
## Knowledge Integration
Seamlessly integrate with existing knowledge bases.
## Context Management
Handle complex contextual queries and responses.
## 
​
Troubleshooting
## RAG Issues
If RAG system isn’t working:
  * Check database configuration
  * Verify connection settings
  * Enable verbose mode for debugging


## Query Issues
If queries aren’t returning expected results:
  * Check embedding quality
  * Verify search parameters
  * Monitor similarity thresholds


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your vector database is properly configured and indexed for your specific use case.
Was this page helpful?
YesNo
Self Reflection AgentsReasoning Extract Agents
On this page
  * Quick Start
  * Data Indexing and Retrieval Agents
  * Advanced Configuration
  * Multi-Agent Knowledge System
  * Retrieval Agents
  * Adding Knowledge to RAG Agents
  * Understanding RAG Agents
  * Features
  * Troubleshooting
  * Next Steps


