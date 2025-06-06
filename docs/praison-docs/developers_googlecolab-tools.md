PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
Google Colab Tools
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


Copy
```
jupyter:
 accelerator: GPU
 colab:
  gpuType: T4
 kernelspec:
  display_name: Python 3
  name: python3
 language_info:
  name: python
 nbformat: 4
 nbformat_minor: 0

```

Copy
```
!pip install -Uq praisonai duckduckgo_search

```

Copy
```
from duckduckgo_search import DDGS
from praisonai_tools import BaseTool
class InternetSearchTool(BaseTool):
  name: str = "InternetSearchTool"
  description: str = "Search Internet for relevant information based on a query or latest news"
  def _run(self, query: str):
    ddgs = DDGS()
    results = ddgs.text(keywords=query, region='wt-wt', safesearch='moderate', max_results=5)
    return results

```

Copy
```
import os
import yaml
from praisonai import PraisonAI
from google.colab import userdata
# Example agent_yaml content
agent_yaml = """
framework: "crewai"
topic: "Space Exploration"
roles:
 astronomer:
  role: "Space Researcher"
  goal: "Discover new insights about {topic}"
  backstory: "You are a curious and dedicated astronomer with a passion for unraveling the mysteries of the cosmos."
  tasks:
   investigate_exoplanets:
    description: "Research and compile information about exoplanets discovered in the last decade."
    expected_output: "A summarized report on exoplanet discoveries, including their size, potential habitability, and distance from Earth."
  tools:
   - "InternetSearchTool"
"""
# Create a PraisonAI instance with the agent_yaml content
praisonai = PraisonAI(agent_yaml=agent_yaml)
# Add OPENAI_API_KEY Secrets to Google Colab on the Left Hand Side 🔑 or Enter Manually Below
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY') or "ENTER OPENAI_API_KEY HERE"
# Run PraisonAI
result = praisonai.run()
# Print the result
print(result)

```

[2024-07-03 04:53:48][DEBUG]: == Working Agent: Space Researcher [2024-07-03 04:53:48][INFO]: == Starting Task: Research and compile information about exoplanets discovered in the last decade.
> Entering new CrewAgentExecutor chain… I now can give a great answer.
Final Answer:
Over the last decade, the field of exoplanet research has experienced significant advancements, leading to the discovery of thousands of exoplanets. These discoveries have been made possible through missions like NASA’s Kepler and TESS (Transiting Exoplanet Survey Satellite), as well as ground-based observatories. Here is a summarized report on some of the notable exoplanet discoveries, including their size, potential habitability, and distance from Earth:
  1. **Kepler-452b**
     * **Size** : Approximately 1.6 times the radius of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, where liquid water could exist. It is often referred to as Earth’s “cousin.”
     * **Distance from Earth** : About 1,400 light-years
  2. **Proxima Centauri b**
     * **Size** : About 1.17 times the mass of Earth
     * **Potential Habitability** : Located in the habitable zone of Proxima Centauri, the closest star to the Sun. It has the potential to have liquid water.
     * **Distance from Earth** : 4.24 light-years
  3. **TRAPPIST-1 System**
     * **Size** : The system includes seven Earth-sized planets
     * **Potential Habitability** : Three of the planets (TRAPPIST-1e, TRAPPIST-1f, and TRAPPIST-1g) are located in the habitable zone and could potentially support liquid water.
     * **Distance from Earth** : Approximately 39 light-years
  4. **LHS 1140b**
     * **Size** : About 1.4 times the size of Earth and 6.6 times its mass
     * **Potential Habitability** : Located in the habitable zone of its star. It has a thick atmosphere and conditions that could support life.
     * **Distance from Earth** : About 40 light-years
  5. **Kepler-186f**
     * **Size** : Similar to Earth in size
     * **Potential Habitability** : The first Earth-sized planet discovered in the habitable zone of another star. It has potential for liquid water on its surface.
     * **Distance from Earth** : About 500 light-years
  6. **K2-18b**
     * **Size** : Approximately 2.6 times the radius of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, with evidence of water vapor in its atmosphere.
     * **Distance from Earth** : About 124 light-years
  7. **GJ 357 d**
     * **Size** : About 6.1 times the mass of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, with the potential to have liquid water on its surface.
     * **Distance from Earth** : About 31 light-years


These discoveries highlight the diversity of exoplanets in terms of size, composition, and potential habitability. The search for exoplanets is crucial for understanding the potential for life beyond Earth and the formation and evolution of planetary systems. Ongoing and future missions, such as the James Webb Space Telescope, are expected to provide even more detailed information about these distant worlds.
The continuous exploration and study of exoplanets will undoubtedly lead to new insights and perhaps even the discovery of life beyond our solar system.
> Finished chain. [2024-07-03 04:53:58][DEBUG]: == [Space Researcher] Task output: Over the last decade, the field of exoplanet research has experienced significant advancements, leading to the discovery of thousands of exoplanets. These discoveries have been made possible through missions like NASA’s Kepler and TESS (Transiting Exoplanet Survey Satellite), as well as ground-based observatories. Here is a summarized report on some of the notable exoplanet discoveries, including their size, potential habitability, and distance from Earth:
  1. **Kepler-452b**
     * **Size** : Approximately 1.6 times the radius of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, where liquid water could exist. It is often referred to as Earth’s “cousin.”
     * **Distance from Earth** : About 1,400 light-years
  2. **Proxima Centauri b**
     * **Size** : About 1.17 times the mass of Earth
     * **Potential Habitability** : Located in the habitable zone of Proxima Centauri, the closest star to the Sun. It has the potential to have liquid water.
     * **Distance from Earth** : 4.24 light-years
  3. **TRAPPIST-1 System**
     * **Size** : The system includes seven Earth-sized planets
     * **Potential Habitability** : Three of the planets (TRAPPIST-1e, TRAPPIST-1f, and TRAPPIST-1g) are located in the habitable zone and could potentially support liquid water.
     * **Distance from Earth** : Approximately 39 light-years
  4. **LHS 1140b**
     * **Size** : About 1.4 times the size of Earth and 6.6 times its mass
     * **Potential Habitability** : Located in the habitable zone of its star. It has a thick atmosphere and conditions that could support life.
     * **Distance from Earth** : About 40 light-years
  5. **Kepler-186f**
     * **Size** : Similar to Earth in size
     * **Potential Habitability** : The first Earth-sized planet discovered in the habitable zone of another star. It has potential for liquid water on its surface.
     * **Distance from Earth** : About 500 light-years
  6. **K2-18b**
     * **Size** : Approximately 2.6 times the radius of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, with evidence of water vapor in its atmosphere.
     * **Distance from Earth** : About 124 light-years
  7. **GJ 357 d**
     * **Size** : About 6.1 times the mass of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, with the potential to have liquid water on its surface.
     * **Distance from Earth** : About 31 light-years


These discoveries highlight the diversity of exoplanets in terms of size, composition, and potential habitability. The search for exoplanets is crucial for understanding the potential for life beyond Earth and the formation and evolution of planetary systems. Ongoing and future missions, such as the James Webb Space Telescope, are expected to provide even more detailed information about these distant worlds.
The continuous exploration and study of exoplanets will undoubtedly lead to new insights and perhaps even the discovery of life beyond our solar system.
### 
​
Task Output
Over the last decade, the field of exoplanet research has experienced significant advancements, leading to the discovery of thousands of exoplanets. These discoveries have been made possible through missions like NASA’s Kepler and TESS (Transiting Exoplanet Survey Satellite), as well as ground-based observatories. Here is a summarized report on some of the notable exoplanet discoveries, including their size, potential habitability, and distance from Earth:
  1. **Kepler-452b**
     * **Size** : Approximately 1.6 times the radius of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, where liquid water could exist. It is often referred to as Earth’s “cousin.”
     * **Distance from Earth** : About 1,400 light-years
  2. **Proxima Centauri b**
     * **Size** : About 1.17 times the mass of Earth
     * **Potential Habitability** : Located in the habitable zone of Proxima Centauri, the closest star to the Sun. It has the potential to have liquid water.
     * **Distance from Earth** : 4.24 light-years
  3. **TRAPPIST-1 System**
     * **Size** : The system includes seven Earth-sized planets
     * **Potential Habitability** : Three of the planets (TRAPPIST-1e, TRAPPIST-1f, and TRAPPIST-1g) are located in the habitable zone and could potentially support liquid water.
     * **Distance from Earth** : Approximately 39 light-years
  4. **LHS 1140b**
     * **Size** : About 1.4 times the size of Earth and 6.6 times its mass
     * **Potential Habitability** : Located in the habitable zone of its star. It has a thick atmosphere and conditions that could support life.
     * **Distance from Earth** : About 40 light-years
  5. **Kepler-186f**
     * **Size** : Similar to Earth in size
     * **Potential Habitability** : The first Earth-sized planet discovered in the habitable zone of another star. It has potential for liquid water on its surface.
     * **Distance from Earth** : About 500 light-years
  6. **K2-18b**
     * **Size** : Approximately 2.6 times the radius of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, with evidence of water vapor in its atmosphere.
     * **Distance from Earth** : About 124 light-years
  7. **GJ 357 d**
     * **Size** : About 6.1 times the mass of Earth
     * **Potential Habitability** : Located in the habitable zone of its star, with the potential to have liquid water on its surface.
     * **Distance from Earth** : About 31 light-years


These discoveries highlight the diversity of exoplanets in terms of size, composition, and potential habitability. The search for exoplanets is crucial for understanding the potential for life beyond Earth and the formation and evolution of planetary systems. Ongoing and future missions, such as the James Webb Space Telescope, are expected to provide even more detailed information about these distant worlds.
The continuous exploration and study of exoplanets will undoubtedly lead to new insights and perhaps even the discovery of life beyond our solar system. ::: :::
Was this page helpful?
YesNo
Google Colab IntegrationLocal Development
On this page
  * Task Output


