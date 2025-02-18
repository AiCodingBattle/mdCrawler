PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Multimodal Agents
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
Quick Start
  * Code
  * No Code


1
Install Package
First, install the PraisonAI Agents package:
Copy
```
pip install praisonaiagents opencv-python moviepy

```

2
Set API Key
Set your OpenAI API key as an environment variable in your terminal:
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxx

```

3
Create a file
Create a new file `app.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create Vision Analysis Agent
vision_agent = Agent(
  name="VisionAnalyst",
  role="Computer Vision Specialist",
  goal="Analyze images and videos to extract meaningful information",
  backstory="""You are an expert in computer vision and image analysis.
  You excel at describing images, detecting objects, and understanding visual content.""",
  llm="gpt-4o-mini",
  self_reflect=False
)
# Create tasks with different media types
task = Task(
  name="analyze_landmark",
  description="Describe this famous landmark and its architectural features.",
  expected_output="Detailed description of the landmark's architecture and significance",
  agent=vision_agent,
  images=["https://upload.wikimedia.org/wikipedia/commons/b/bf/Krakow_-_Kosciol_Mariacki.jpg"]
)
# Run the agents
agents = PraisonAIAgents(
  agents=[vision_agent],
  tasks=[task],
  process="sequential",
  verbose=True
)
agents.start()

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
  * OpenAI API key with vision model access
  * Basic understanding of Python and media handling


## 
​
Understanding Multimodal Agents
## What are Multimodal Agents?
Multimodal agents are designed to:
  * Process multiple types of data (text, images, videos)
  * Understand context across different modalities
  * Generate insights from diverse media sources
  * Handle complex multimedia tasks


## 
​
Features
## Vision Processing
Analyze images, detect objects, and understand visual content.
## Video Analysis
Process video content for events and actions.
## Text Extraction
Extract and analyze text from images and documents.
## Cross-Modal Understanding
Integrate insights across different media types.
## 
​
Multi-Agent Media Processing
  * Code
  * No Code


Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
# Create first agent for image analysis
vision_agent = Agent(
  role="Image Analyst",
  goal="Analyze visual content and extract key information",
  backstory="Expert in visual analysis and image understanding",
  llm="gpt-4o-mini",
  self_reflect=False
)
# Create second agent for content writing
writer_agent = Agent(
  role="Content Writer",
  goal="Create engaging content based on image analysis",
  backstory="Expert in creating compelling content from visual insights",
  llm="gpt-4o-mini"
)
# Create tasks for different media types
document_task = Task(
  description="Extract and summarize text from this document image",
  expected_output="Structured text content with key information highlighted",
  agent=vision_agent,
  images=["document.jpg"]
)
writing_task = Task(
  description="Create engaging content based on image analysis",
  expected_output="Compelling article incorporating visual insights",
  agent=writer_agent
)
# Create and start the agents
agents = PraisonAIAgents(
  agents=[vision_agent, writer_agent],
  tasks=[document_task, writing_task],
  process="sequential"
)
result = agents.start()

```

### 
​
Configuration Options
Copy
```
# Create an agent with multimodal configuration
agent = Agent(
  role="Media Analyst",
  goal="Process multiple types of media",
  backstory="Expert in multimedia analysis",
  llm="gpt-4o-mini", # Must support vision capabilities
  verbose=True, # Enable detailed logging
  self_reflect=False # Optional: disable self-reflection
)
# Task with media requirements
task = Task(
  description="Analyze media content",
  expected_output="Comprehensive analysis",
  agent=agent,
  images=[ # Support multiple media sources
    "https://example.com/image1.jpg",
    "path/to/local/image.jpg",
    "path/to/video.mp4"
  ]
)

```

## 
​
Best Practices
## Media Handling
  * Use supported formats (JPEG, PNG)
  * Keep reasonable file sizes
  * Provide high-quality media
  * Validate files before processing


## Task Design
  * Write clear descriptions
  * Break down complex analyses
  * Specify expected outputs
  * Handle errors gracefully


## 
​
Example Use Cases
## Document Analysis
Extract and analyze text from document images.
## Security Monitoring
Monitor security feeds for suspicious activity.
## Medical Imaging
Analyze medical scans for abnormalities.
## Architectural Analysis
Study architectural features and designs.
## 
​
Next Steps
## AutoAgents
Learn about automatically created and managed AI agents
## Mini Agents
Explore lightweight, focused AI agents
For optimal results, ensure your media files are in supported formats and sizes for processing.
Was this page helpful?
YesNo
Reasoning AgentsLangChain Agents
On this page
  * Quick Start
  * Understanding Multimodal Agents
  * Features
  * Multi-Agent Media Processing
  * Configuration Options
  * Best Practices
  * Example Use Cases
  * Next Steps


