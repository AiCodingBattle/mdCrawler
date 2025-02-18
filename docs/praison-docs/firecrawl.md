PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Tools
Firecrawl PraisonAI Integration
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
Firecrawl PraisonAI Integration
## 
​
Firecrawl running in Localhost:3002
Copy
```
from firecrawl import FirecrawlApp
from praisonai_tools import BaseTool
import re
class WebPageScraperTool(BaseTool):
  name: str = "Web Page Scraper Tool"
  description: str = "Scrape and extract information from a given web page URL."
  def _run(self, url: str) -> str:
    app = FirecrawlApp(api_url='http://localhost:3002')
    response = app.scrape_url(url=url)
    content = response["content"]
    # Remove all content above the line "========================================================"
    if "========================================================" in content:
      content = content.split("========================================================", 1)[1]
    # Remove all menu items and similar patterns
    content = re.sub(r'\*\s+\[.*?\]\(.*?\)', '', content)
    content = re.sub(r'\[Skip to the content\]\(.*?\)', '', content)
    content = re.sub(r'\[.*?\]\(.*?\)', '', content)
    content = re.sub(r'\s*Menu\s*', '', content)
    content = re.sub(r'\s*Search\s*', '', content)
    content = re.sub(r'Categories\s*', '', content)
    # Remove all URLs
    content = re.sub(r'http\S+', '', content)
    
    # Remove empty lines or lines with only whitespace
    content = '\n'.join([line for line in content.split('\n') if line.strip()])
    # Limit to the first 1000 words
    words = content.split()
    if len(words) > 1000:
      content = ' '.join(words[:1000])
    
    return content

```

Was this page helpful?
YesNo
Other ModelsPraisonAI Train
On this page
  * Firecrawl PraisonAI Integration
  * Firecrawl running in Localhost:3002


