PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Core Concepts
AI Agents with Knowledge
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
Vector Store
Vector DB
Input
PDF
TXT
MD
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
  knowledge=["small.pdf"]
)
agent.start("What is KAG in one line?")

```

## 
​
Basic Usage
The simplest way to create a knowledge-based agent is without any configuration:
Copy
```
from praisonaiagents import Agent
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["small.pdf"]
)
agent.start("What is KAG in one line?")

```

## 
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
      "collection_name": "custom_knowledge",
      "path": ".praison",
    }
  }
}
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["small.pdf"],
  knowledge_config=config
)
agent.start("What is KAG in one line?")

```

## 
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
      "collection_name": "knowledge_test",
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
  knowledge=["sample.pdf"],
  knowledge_config=config,
  verbose=True
)
# Define a task for the agent
knowledge_task = Task(
  name="knowledge_task",
  description="Who is Mervin Praison?",
  expected_output="Answer to the question",
  agent=knowledge_agent
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[knowledge_agent],
  tasks=[knowledge_task],
  process="sequential",
  user_id="user1"
)
# Start execution
result = agents.start()

```

## 
​
Understanding Knowledge Configuration
Vector Store Options
  * **Provider** : Choose between different vector store backends (e.g., “chroma”)
  * **Collection Name** : Name for your knowledge collection
  * **Path** : Location to store the vector database


Supported File Types
  * PDF documents (*.pdf)
  * Text files (*.txt)
  * Markdown files (*.md, *.mdx)
  * And more…


Multi-Agent Setup
  * **Role** : Define specialized roles for knowledge agents
  * **Goal** : Set specific knowledge management objectives
  * **Process** : Choose between sequential or parallel execution


## 
​
Features
## Custom Knowledge
Import your own documents and data as knowledge sources
## Vector Storage
Efficient storage and retrieval of knowledge embeddings
## Multiple Sources
Combine multiple documents and file types
## Persistent Storage
Save and reuse knowledge bases across sessions
## 
​
Best Practices
  1. **Document Preparation**
     * Clean and well-formatted documents work best
     * Break large documents into smaller chunks
     * Use consistent formatting
  2. **Knowledge Organization**
     * Group related documents together
     * Use meaningful file names
     * Keep knowledge bases focused and relevant
  3. **Performance Optimization**
     * Monitor vector store size
     * Clean up unused collections
     * Use appropriate chunk sizes
  4. **Multi-Agent Coordination**
     * Define clear roles and responsibilities
     * Set appropriate logging levels for debugging
     * Use unique collection names for different agent groups


## 
​
Next Steps
  * Learn about Memory Management for long-term recall
  * Explore Tool Integration for enhanced capabilities
  * Check out Examples for implementation ideas


Was this page helpful?
YesNo
MemoryAgentic Routing
On this page
  * Quick Start
  * Basic Usage
  * Advanced Configuration
  * Multi-Agent Knowledge System
  * Understanding Knowledge Configuration
  * Features
  * Best Practices
  * Next Steps


