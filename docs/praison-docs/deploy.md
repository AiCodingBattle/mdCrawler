PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
Deploy
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
Google Cloud
Copy
```
gcloud init
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
gcloud services enable cloudbuild.googleapis.com
export OPENAI_MODEL_NAME="gpt-4o"
export OPENAI_API_KEY="Enter your API key"
export OPENAI_API_BASE="https://api.openai.com/v1"
yes | gcloud auth configure-docker us-central1-docker.pkg.dev 
gcloud artifacts repositories create praisonai-repository --repository-format=docker --location=us-central1
PROJECT_ID=$(gcloud config get-value project)
TAG="latest"
docker build --platform linux/amd64 -t gcr.io/${PROJECT_ID}/praisonai-app:${TAG} .
docker tag gcr.io/${PROJECT_ID}/praisonai-app:${TAG} us-central1-docker.pkg.dev/${PROJECT_ID}/praisonai-repository/praisonai-app:${TAG}
docker push us-central1-docker.pkg.dev/${PROJECT_ID}/praisonai-repository/praisonai-app:${TAG}
gcloud run deploy praisonai-service \
  --image us-central1-docker.pkg.dev/${PROJECT_ID}/praisonai-repository/praisonai-app:${TAG} \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_MODEL_NAME=${OPENAI_MODEL_NAME},OPENAI_API_KEY=${OPENAI_API_KEY},OPENAI_API_BASE=${OPENAI_API_BASE}

```

Was this page helpful?
YesNo
Local DevelopmentIntroduction
On this page
  * Google Cloud


