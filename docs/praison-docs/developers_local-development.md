PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
Local Development
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
Logging
Copy
```
export LOGLEVEL=info

```

Advanced logging:
Copy
```
export LOGLEVEL=debug

```

## 
​
Local Docker Development with Live Reload
To facilitate local development with live reload, you can use Docker. Follow the steps below:
### 
​
1. Create Dockerfile.dev
Dockerfile.dev
Copy
```
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask praisonai==2.0.18 watchdog
EXPOSE 5555
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]

```

### 
​
2. Create docker-compose.yml
docker-compose.yml
Copy
```
version: '3.8'
services:
 app:
  build:
   context: .
   dockerfile: Dockerfile.dev
  volumes:
   - .:/app
  ports:
   - "5555:5555"
  environment:
   FLASK_ENV: development
  command: flask run --host=0.0.0.0
 watch:
  image: alpine:latest
  volumes:
   - .:/app
  command: sh -c "apk add --no-cache inotify-tools && while inotifywait -r -e modify,create,delete /app; do kill -HUP 1; done"

```

### 
​
3. Run Docker Compose
Terminal
Copy
```
docker-compose up

```

This setup will allow you to develop locally with live reload, making it easier to test and iterate on your code.
Was this page helpful?
YesNo
Google Colab ToolsDeploy
On this page
  * Logging
  * Local Docker Development with Live Reload
  * 1. Create Dockerfile.dev
  * 2. Create docker-compose.yml
  * 3. Run Docker Compose


