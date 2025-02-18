PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Models
Models in PraisonAI
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


# 
​
Code
## 
​
Set model by 3 ways
### 
​
1. OpenAI Compatible Endpoints
By Default it uses OPENAI_BASE_URL https://api.openai.com/v1
Example Groq Implementation: 
Copy
```
export OPENAI_API_KEY=groq-api-key
export OPENAI_BASE_URL=https://api.groq.com/openai/v1

```

Copy
```
from praisonaiagents import Agent
agent = Agent(
  instructions="You are a helpful assistant",
  llm="llama-3.1-8b-instant",
)
agent.start("Why sky is Blue?")

```

### 
​
2. Litellm Compatible model names (eg: gemini/gemini-1.5-flash-8b)
Copy
```
pip install "praisonaiagents[llm]"

```

Copy
```
from praisonaiagents import Agent
agent = Agent(
  instructions="You are a helpful assistant",
  llm="gemini/gemini-1.5-flash-8b",
  self_reflect=True,
  verbose=True
)
agent.start("Why sky is Blue?")

```

### 
​
3. Litellm Compatible Configuration
Copy
```
pip install "praisonaiagents[llm]"

```

Copy
```
from praisonaiagents import Agent
llm_config = {
  "model": "gemini/gemini-1.5-flash-latest", # Model name without provider prefix
  
  # Core settings
  "temperature": 0.7,        # Controls randomness (like temperature)
  "timeout": 30,         # Timeout in seconds
  "top_p": 0.9,          # Nucleus sampling parameter
  "max_tokens": 1000,        # Max tokens in response
  
  # Advanced parameters
  "presence_penalty": 0.1,     # Penalize repetition of topics (-2.0 to 2.0)
  "frequency_penalty": 0.1,    # Penalize token repetition (-2.0 to 2.0)
  
  # API settings (optional)
  "api_key": None,         # Your API key (or use environment variable)
  "base_url": None,        # Custom API endpoint if needed
  
  # Response formatting
  "response_format": {       # Force specific response format
    "type": "text"        # Options: "text", "json_object"
  },
  
  # Additional controls
  "seed": 42,           # For reproducible responses
  "stop_phrases": ["##", "END"],  # Custom stop sequences
}
agent = Agent(
  instructions="You are a helpful Assistant."
  llm=llm_config
)
agent.start()

```

## 
​
Advanced Configuration (Litellm Support)
This uses Litellm
1
Install Package
Install required packages:
Copy
```
pip install "praisonaiagents[llm]"

```

2
Setup Environment
Configure environment:
Copy
```
export GOOGLE_API_KEY=your-api-key

```

Get your API key from Google AI Studio
3
Create Agent
Create `app.py`:
Basic
Advanced
Copy
```
# if json_object is supported by the model
from praisonaiagents import Agent
agent = Agent(
  instructions="You are a helpful assistant",
  llm="gemini/gemini-1.5-flash-8b",
  self_reflect=True,
  verbose=True
)
agent.start("Why sky is Blue?")

```

Ollama Integration
Copy
```
export OPENAI_BASE_URL=http://localhost:11434/v1

```

Groq Integration
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxx
export OPENAI_BASE_URL=https://api.groq.com/openai/v1

```

Google Gemini
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxx
export OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/

```

Jan AI Integration
Copy
```
export OPENAI_BASE_URL=http://localhost:1337/v1

```

LM Studio Integration
Copy
```
export OPENAI_BASE_URL=http://localhost:1234/v1

```

OpenRouter Integration
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxx
export OPENAI_BASE_URL=https://openrouter.ai/api/v1

```

## 
​
Supported Models for No Code
PraisonAI Chat| PraisonAI Code| PraisonAI (Multi-Agents)  
---|---|---  
Litellm| Litellm| Below Models  
  * OpenAI
  * Groq
  * Google Gemini
  * Anthropic Claude
  * Cohere
  * Mistral
  * Ollama
  * Other Models


## 
​
Example agents.yaml
This uses Multi-Agents with Multi-LLMs.
Copy
```
framework: crewai
topic: research about the causes of lung disease
roles:
 research_analyst:
  backstory: Experienced in analyzing scientific data related to respiratory health.
  goal: Analyze data on lung diseases
  role: Research Analyst
  llm: 
   model: "groq/llama3-70b-8192"
  function_calling_llm: 
   model: "google/gemini-1.5-flash-001"
  tasks:
   data_analysis:
    description: Gather and analyze data on the causes and risk factors of lung
     diseases.
    expected_output: Report detailing key findings on lung disease causes.
  tools:
  - 'InternetSearchTool'
 medical_writer:
  backstory: Skilled in translating complex medical information into accessible
   content.
  goal: Compile comprehensive content on lung disease causes
  role: Medical Writer
  llm: 
   model: "anthropic/claude-3-haiku-20240307"
  function_calling_llm: 
   model: "openai/gpt-4o"
  tasks:
   content_creation:
    description: Create detailed content summarizing the research findings on
     lung disease causes.
    expected_output: Document outlining various causes and risk factors of lung
     diseases.
  tools:
  - ''
 editor:
  backstory: Proficient in editing medical content for accuracy and clarity.
  goal: Review and refine content on lung disease causes
  role: Editor
  llm: 
   model: "cohere/command-r"
  tasks:
   content_review:
    description: Edit and refine the compiled content on lung disease causes for
     accuracy and coherence.
    expected_output: Finalized document on lung disease causes ready for dissemination.
  tools:
  - ''
dependencies: []

```

Was this page helpful?
YesNo
Chat with PDFOpenAI ChatGPT
On this page
  * Code
  * Set model by 3 ways
  * 1. OpenAI Compatible Endpoints
  * 2. Litellm Compatible model names (eg: gemini/gemini-1.5-flash-8b)
  * 3. Litellm Compatible Configuration
  * Advanced Configuration (Litellm Support)
  * Supported Models for No Code
  * Example agents.yaml


