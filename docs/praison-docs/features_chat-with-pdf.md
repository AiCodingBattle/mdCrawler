PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Chat with PDF Agents
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
PDF Document
PDF Chat Agent
Vector DB
Chat Interface
Response
A PDF-centric workflow where Chat agents interact with vector databases to store and retrieve information from PDF documents, enabling natural conversations and intelligent question-answering capabilities.
## 
​
Quick Start
1
Install Package
Install PraisonAI Agents with PDF chat support:
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
Create a new file `chat_with_pdf.py`:
Copy
```
from praisonaiagents import Agent
agent = Agent(
  name="PDF Chat Agent",
  instructions="You answer questions based on the provided PDF document.",
  knowledge=["document.pdf"], # PDF Indexing
)
agent.start("What is the main topic of this PDF?") # Chat Query

```

## 
​
PDF Processing and Chat Agents
PDF processing involves indexing the document content for efficient retrieval during chat.
Chat Agents
Chat Agent 1
Chat Agent 2
Chat Agent 3
Vector Store
Vector DB
Input
PDF Documents
The simplest way to create a PDF chat agent is without any configuration:
Copy
```
from praisonaiagents import Agent
agent = Agent(
  name="PDF Chat Agent",
  instructions="You answer questions based on the provided PDF document.",
  knowledge=["document.pdf"] # PDF Indexing
)
agent.start("What are the key points in this document?") # Chat Query

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
  name="PDF Chat Agent",
  instructions="You answer questions based on the provided PDF document.",
  knowledge=["document.pdf"], # PDF Indexing
  knowledge_config=config # Configuration
)
agent.start("What is the main topic of this PDF?") # Chat Query

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
Understanding PDF Chat Agents
## What are PDF Chat Agents?
PDF Chat agents enable:
  * Natural conversation with PDF documents
  * Intelligent information extraction
  * Context-aware document understanding
  * Quick answers to document-specific questions


## 
​
Features
## PDF Processing
Process and index PDF documents efficiently.
## Natural Chat
Have natural conversations about PDF content.
## Smart Retrieval
Intelligently retrieve relevant information from PDFs.
## Context Awareness
Maintain context throughout the conversation.
## 
​
Troubleshooting
## PDF Issues
If PDF processing isn’t working:
  * Check PDF file format and encoding
  * Verify document accessibility
  * Enable verbose mode for debugging


## Chat Issues
If chat responses aren’t accurate:
  * Check PDF indexing quality
  * Verify question clarity
  * Monitor context retention


## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal chat experience, ensure your PDFs are properly formatted and text-searchable.
Was this page helpful?
YesNo
Callbacks AgentModels in PraisonAI
On this page
  * Quick Start
  * PDF Processing and Chat Agents
  * Advanced Configuration
  * Multi-Agent Knowledge System
  * Understanding PDF Chat Agents
  * Features
  * Troubleshooting
  * Next Steps


