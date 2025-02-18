PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
Agents Playbook
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
Agents Playbook
## 
​
Simple Playbook Example
Copy
```
framework: crewai
topic: Artificial Intelligence
roles:
 screenwriter:
  backstory: 'Skilled in crafting scripts with engaging dialogue about {topic}.'
  goal: Create scripts from concepts.
  role: Screenwriter
  tasks:
   scriptwriting_task:
    description: 'Develop scripts with compelling characters and dialogue about {topic}.'
    expected_output: 'Complete script ready for production.'

```

## 
​
Detailed Playbook Example
Copy
```
framework: crewai
topic: Artificial Intelligence
roles:
 movie_concept_creator:
  backstory: 'Creative thinker with a deep understanding of cinematic storytelling,
   capable of using AI-generated storylines to create unique and compelling movie
   ideas.'
  goal: Generate engaging movie concepts using AI storylines
  role: Movie Concept Creator
  tasks:
   movie_concept_development:
    description: 'Develop movie concepts from AI-generated storylines, ensuring
     they are engaging and have strong narrative arcs.'
    expected_output: 'Well-structured movie concept document with character
     bios, settings, and plot outlines.'
 screenwriter:
  backstory: 'Expert in writing engaging dialogue and script structure, able to
   turn movie concepts into production-ready scripts.'
  goal: Write compelling scripts based on movie concepts
  role: Screenwriter
  tasks:
   scriptwriting_task:
    description: 'Turn movie concepts into polished scripts with well-developed
     characters, strong dialogue, and effective scene transitions.'
    expected_output: 'Production-ready script with a beginning, middle, and
     end, along with character development and engaging dialogues.'
 editor:
  backstory: 'Adept at identifying inconsistencies, improving language usage,
   and maintaining the overall flow of the script.'
  goal: Refine the scripts and ensure continuity of the movie storyline
  role: Editor
  tasks:
   editing_task:
    description: 'Review, edit, and refine the scripts to ensure they are cohesive
     and follow a well-structured narrative.'
    expected_output: 'A polished final draft of the script with no inconsistencies,
     strong character development, and effective dialogue.'
dependencies: []

```

Was this page helpful?
YesNo
TestPraisonAI Package Integration
On this page
  * Agents Playbook
  * Simple Playbook Example
  * Detailed Playbook Example


