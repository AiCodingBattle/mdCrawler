PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Models
DeepSeek Agents
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


Input
Ollama
Deepseek
Basic Agent
RAG Agent
UI Agent
Output
Output
Output
Learn how to use Deepseek models with PraisonAI Agents through Ollama integration for basic queries, RAG applications, and interactive UI implementations.
## 
​
Prerequisites
1
Install Ollama
First, install Ollama on your system:
Copy
```
curl -fsSL https://ollama.com/install.sh | sh

```

2
Pull Deepseek Model
Pull the Deepseek model from Ollama:
Copy
```
ollama pull deepseek-r1

```

3
Install Package
Install PraisonAI Agents:
Copy
```
pip install "praisonaiagents[knowledge]" ollama streamlit

```

Streamlit for UI is optional. Ollama is required for Local RAG Agents. praisonaiagents[knowledge] is for RAG Agents. praisonaiagents is for Basic Agents.
4
Set Environment
Set Ollama as your base URL:
Copy
```
export OPENAI_BASE_URL=http://localhost:11434/v1
export OPENAI_API_KEY=fake-key

```

## 
​
Basic Usage
The simplest way to use Deepseek with PraisonAI Agents:
Copy
```
from praisonaiagents import Agent
agent = Agent(instructions="You are helpful Assisant", llm="deepseek-r1")
agent.start("Why sky is Blue?")

```

## 
​
RAG Implementation
Use Deepseek with RAG capabilities for knowledge-based interactions:
Copy
```
from praisonaiagents import Agent
config = {
  "vector_store": {
    "provider": "chroma",
    "config": {
      "collection_name": "praison",
      "path": ".praison"
    }
  },
  "llm": {
    "provider": "ollama",
    "config": {
      "model": "deepseek-r1:latest",
      "temperature": 0,
      "max_tokens": 8000,
      "ollama_base_url": "http://localhost:11434",
    },
  },
  "embedder": {
    "provider": "ollama",
    "config": {
      "model": "nomic-embed-text:latest",
      "ollama_base_url": "http://localhost:11434",
      "embedding_dims": 1536
    },
  },
}
agent = Agent(
  name="Knowledge Agent",
  instructions="You answer questions based on the provided knowledge.",
  knowledge=["kag-research-paper.pdf"], # Indexing
  knowledge_config=config,
  user_id="user1",
  llm="deepseek-r1"
)
agent.start("What is KAG in one line?") # Retrieval

```

## 
​
Interactive UI with Streamlit
Create an interactive chat interface using Streamlit:
Copy
```
import streamlit as st
from praisonaiagents import Agent
def init_agent():
  config = {
    "vector_store": {
      "provider": "chroma",
      "config": {
        "collection_name": "praison",
        "path": ".praison"
      }
    },
    "llm": {
      "provider": "ollama",
      "config": {
        "model": "deepseek-r1:latest",
        "temperature": 0,
        "max_tokens": 8000,
        "ollama_base_url": "http://localhost:11434",
      },
    },
    "embedder": {
      "provider": "ollama",
      "config": {
        "model": "nomic-embed-text:latest",
        "ollama_base_url": "http://localhost:11434",
        "embedding_dims": 1536
      },
    },
  }
  
  return Agent(
    name="Knowledge Agent",
    instructions="You answer questions based on the provided knowledge.",
    knowledge=["kag-research-paper.pdf"],
    knowledge_config=config,
    user_id="user1",
    llm="deepseek-r1"
  )
st.title("Knowledge Agent Chat")
if "agent" not in st.session_state:
  st.session_state.agent = init_agent()
  st.session_state.messages = []
if "messages" in st.session_state:
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])
prompt = st.chat_input("Ask a question...")
if prompt:
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  with st.chat_message("assistant"):
    response = st.session_state.agent.start(prompt)
    st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response}) 

```

## 
​
Running the UI
1
Install Streamlit
Install Streamlit if you haven’t already:
Copy
```
pip install streamlit

```

2
Save and Run
Save the UI code in a file (e.g., `app.py`) and run:
Copy
```
streamlit run app.py

```

## 
​
Features
## Local Deployment
Run Deepseek models locally through Ollama.
## RAG Capabilities
Integrate with vector databases for knowledge retrieval.
## Interactive UI
Create chat interfaces with Streamlit integration.
## Custom Configuration
Configure model parameters and embedding settings.
## 
​
Troubleshooting
## Ollama Issues
If Ollama isn’t working:
  * Check if Ollama is running
  * Verify model is downloaded
  * Check port availability


## Performance Issues
If responses are slow:
  * Check system resources
  * Adjust max_tokens
  * Monitor memory usage


For optimal performance, ensure your system meets the minimum requirements for running Deepseek models locally through Ollama.
Was this page helpful?
YesNo
MistralOther Models
On this page
  * Prerequisites
  * Basic Usage
  * RAG Implementation
  * Interactive UI with Streamlit
  * Running the UI
  * Features
  * Troubleshooting


