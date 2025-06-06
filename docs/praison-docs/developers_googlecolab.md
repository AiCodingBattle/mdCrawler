PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Developers
Google Colab Integration
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


## Basic PraisonAI
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)
## PraisonAI with Tools
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)
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
!pip install -Uq praisonai

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

[2024-07-03 04:39:09][DEBUG]: == Working Agent: Space Researcher [2024-07-03 04:39:09][INFO]: == Starting Task: Research and compile information about exoplanets discovered in the last decade.
> Entering new CrewAgentExecutor chain… I now can give a great answer.
Final Answer:
In the last decade, the field of exoplanet research has experienced a remarkable surge in discoveries, thanks to advancements in technology and dedicated space missions such as Kepler, TESS (Transiting Exoplanet Survey Satellite), and various ground-based observatories. Here is a summarized report on some of the notable exoplanet discoveries, highlighting their size, potential habitability, and distance from Earth:
  1. **Kepler-452b**
     * **Size:** Approximately 60% larger in diameter than Earth.
     * **Potential Habitability:** Often referred to as “Earth’s Cousin,” Kepler-452b orbits within the habitable zone of its star, where liquid water could exist. The planet receives a similar amount of energy from its star as Earth does from the Sun.
     * **Distance from Earth:** About 1,402 light-years.
  2. **Proxima Centauri b**
     * **Size:** Slightly larger than Earth, with a minimum mass of 1.17 Earth masses.
     * **Potential Habitability:** Located in the habitable zone of Proxima Centauri, the closest known star to the Sun. Potential for liquid water exists, but its habitability is uncertain due to stellar flare activity.
     * **Distance from Earth:** 4.24 light-years.
  3. **TRAPPIST-1 System**
     * **Size:** The system contains seven Earth-sized planets. TRAPPIST-1e, f, and g are within the star’s habitable zone.
     * **Potential Habitability:** TRAPPIST-1e is considered the most promising candidate for habitability, as it has a rocky composition and is located in the middle of the habitable zone.
     * **Distance from Earth:** About 39 light-years.
  4. **LHS 1140 b**
     * **Size:** About 1.4 times the size of Earth with a mass of around 6.6 Earth masses.
     * **Potential Habitability:** Resides in the habitable zone of its red dwarf star. The planet is likely rocky and has an atmosphere that could support life.
     * **Distance from Earth:** Approximately 40 light-years.
  5. **K2-18b**
     * **Size:** About 2.6 times the size of Earth with a mass of 8.6 Earth masses.
     * **Potential Habitability:** This exoplanet lies within the habitable zone and has been detected to have water vapor in its atmosphere. It is considered one of the most promising candidates for habitability outside our solar system.
     * **Distance from Earth:** Roughly 124 light-years.
  6. **Gliese 667 Cc**
     * **Size:** At least 4.5 times the mass of Earth.
     * **Potential Habitability:** Orbits within the habitable zone of its host star, Gliese 667 C. Its orbit allows for the possibility of liquid water on its surface.
     * **Distance from Earth:** About 23.62 light-years.
  7. **HD 40307 g**
     * **Size:** A super-Earth with at least 7 Earth masses.
     * **Potential Habitability:** Located in the habitable zone of its star, this planet could potentially support liquid water and therefore life.
     * **Distance from Earth:** Approximately 42 light-years.
  8. **Ross 128 b**
     * **Size:** Similar to Earth, with a minimum mass of 1.35 Earth masses.
     * **Potential Habitability:** Orbits within the habitable zone of the relatively quiet red dwarf star Ross 128. The planet has mild temperatures that could allow for liquid water.
     * **Distance from Earth:** About 11 light-years.
  9. **Teegarden’s Star b**
     * **Size:** Comparable to Earth.
     * **Potential Habitability:** Orbits within the habitable zone of Teegarden’s Star, a cool red dwarf. Conditions could be suitable for liquid water.
     * **Distance from Earth:** Approximately 12 light-years.
  10. **Barnard’s Star b**
     * **Size:** A super-Earth with a mass of about 3.2 Earth masses.
     * **Potential Habitability:** Located just outside the traditional habitable zone, but still within a range where liquid water could exist under certain conditions.
     * **Distance from Earth:** About 6 light-years.


These discoveries highlight the diverse and intriguing nature of exoplanets found in the last decade. Each of these planets adds valuable information to our understanding of planetary formation, potential habitability, and the search for extraterrestrial life. Continued advancements in detection methods and technologies promise to further expand our knowledge in the years to come.
> Finished chain. [2024-07-03 04:39:25][DEBUG]: == [Space Researcher] Task output: In the last decade, the field of exoplanet research has experienced a remarkable surge in discoveries, thanks to advancements in technology and dedicated space missions such as Kepler, TESS (Transiting Exoplanet Survey Satellite), and various ground-based observatories. Here is a summarized report on some of the notable exoplanet discoveries, highlighting their size, potential habitability, and distance from Earth:
  1. **Kepler-452b**
     * **Size:** Approximately 60% larger in diameter than Earth.
     * **Potential Habitability:** Often referred to as “Earth’s Cousin,” Kepler-452b orbits within the habitable zone of its star, where liquid water could exist. The planet receives a similar amount of energy from its star as Earth does from the Sun.
     * **Distance from Earth:** About 1,402 light-years.
  2. **Proxima Centauri b**
     * **Size:** Slightly larger than Earth, with a minimum mass of 1.17 Earth masses.
     * **Potential Habitability:** Located in the habitable zone of Proxima Centauri, the closest known star to the Sun. Potential for liquid water exists, but its habitability is uncertain due to stellar flare activity.
     * **Distance from Earth:** 4.24 light-years.
  3. **TRAPPIST-1 System**
     * **Size:** The system contains seven Earth-sized planets. TRAPPIST-1e, f, and g are within the star’s habitable zone.
     * **Potential Habitability:** TRAPPIST-1e is considered the most promising candidate for habitability, as it has a rocky composition and is located in the middle of the habitable zone.
     * **Distance from Earth:** About 39 light-years.
  4. **LHS 1140 b**
     * **Size:** About 1.4 times the size of Earth with a mass of around 6.6 Earth masses.
     * **Potential Habitability:** Resides in the habitable zone of its red dwarf star. The planet is likely rocky and has an atmosphere that could support life.
     * **Distance from Earth:** Approximately 40 light-years.
  5. **K2-18b**
     * **Size:** About 2.6 times the size of Earth with a mass of 8.6 Earth masses.
     * **Potential Habitability:** This exoplanet lies within the habitable zone and has been detected to have water vapor in its atmosphere. It is considered one of the most promising candidates for habitability outside our solar system.
     * **Distance from Earth:** Roughly 124 light-years.
  6. **Gliese 667 Cc**
     * **Size:** At least 4.5 times the mass of Earth.
     * **Potential Habitability:** Orbits within the habitable zone of its host star, Gliese 667 C. Its orbit allows for the possibility of liquid water on its surface.
     * **Distance from Earth:** About 23.62 light-years.
  7. **HD 40307 g**
     * **Size:** A super-Earth with at least 7 Earth masses.
     * **Potential Habitability:** Located in the habitable zone of its star, this planet could potentially support liquid water and therefore life.
     * **Distance from Earth:** Approximately 42 light-years.
  8. **Ross 128 b**
     * **Size:** Similar to Earth, with a minimum mass of 1.35 Earth masses.
     * **Potential Habitability:** Orbits within the habitable zone of the relatively quiet red dwarf star Ross 128. The planet has mild temperatures that could allow for liquid water.
     * **Distance from Earth:** About 11 light-years.
  9. **Teegarden’s Star b**
     * **Size:** Comparable to Earth.
     * **Potential Habitability:** Orbits within the habitable zone of Teegarden’s Star, a cool red dwarf. Conditions could be suitable for liquid water.
     * **Distance from Earth:** Approximately 12 light-years.
  10. **Barnard’s Star b**
     * **Size:** A super-Earth with a mass of about 3.2 Earth masses.
     * **Potential Habitability:** Located just outside the traditional habitable zone, but still within a range where liquid water could exist under certain conditions.
     * **Distance from Earth:** About 6 light-years.


These discoveries highlight the diverse and intriguing nature of exoplanets found in the last decade. Each of these planets adds valuable information to our understanding of planetary formation, potential habitability, and the search for extraterrestrial life. Continued advancements in detection methods and technologies promise to further expand our knowledge in the years to come.
### 
​
Task Output
In the last decade, the field of exoplanet research has experienced a remarkable surge in discoveries, thanks to advancements in technology and dedicated space missions such as Kepler, TESS (Transiting Exoplanet Survey Satellite), and various ground-based observatories. Here is a summarized report on some of the notable exoplanet discoveries, highlighting their size, potential habitability, and distance from Earth:
  1. **Kepler-452b**
     * **Size:** Approximately 60% larger in diameter than Earth.
     * **Potential Habitability:** Often referred to as “Earth’s Cousin,” Kepler-452b orbits within the habitable zone of its star, where liquid water could exist. The planet receives a similar amount of energy from its star as Earth does from the Sun.
     * **Distance from Earth:** About 1,402 light-years.
  2. **Proxima Centauri b**
     * **Size:** Slightly larger than Earth, with a minimum mass of 1.17 Earth masses.
     * **Potential Habitability:** Located in the habitable zone of Proxima Centauri, the closest known star to the Sun. Potential for liquid water exists, but its habitability is uncertain due to stellar flare activity.
     * **Distance from Earth:** 4.24 light-years.
  3. **TRAPPIST-1 System**
     * **Size:** The system contains seven Earth-sized planets. TRAPPIST-1e, f, and g are within the star’s habitable zone.
     * **Potential Habitability:** TRAPPIST-1e is considered the most promising candidate for habitability, as it has a rocky composition and is located in the middle of the habitable zone.
     * **Distance from Earth:** About 39 light-years.
  4. **LHS 1140 b**
     * **Size:** About 1.4 times the size of Earth with a mass of around 6.6 Earth masses.
     * **Potential Habitability:** Resides in the habitable zone of its red dwarf star. The planet is likely rocky and has an atmosphere that could support life.
     * **Distance from Earth:** Approximately 40 light-years.
  5. **K2-18b**
     * **Size:** About 2.6 times the size of Earth with a mass of 8.6 Earth masses.
     * **Potential Habitability:** This exoplanet lies within the habitable zone and has been detected to have water vapor in its atmosphere. It is considered one of the most promising candidates for habitability outside our solar system.
     * **Distance from Earth:** Roughly 124 light-years.
  6. **Gliese 667 Cc**
     * **Size:** At least 4.5 times the mass of Earth.
     * **Potential Habitability:** Orbits within the habitable zone of its host star, Gliese 667 C. Its orbit allows for the possibility of liquid water on its surface.
     * **Distance from Earth:** About 23.62 light-years.
  7. **HD 40307 g**
     * **Size:** A super-Earth with at least 7 Earth masses.
     * **Potential Habitability:** Located in the habitable zone of its star, this planet could potentially support liquid water and therefore life.
     * **Distance from Earth:** Approximately 42 light-years.
  8. **Ross 128 b**
     * **Size:** Similar to Earth, with a minimum mass of 1.35 Earth masses.
     * **Potential Habitability:** Orbits within the habitable zone of the relatively quiet red dwarf star Ross 128. The planet has mild temperatures that could allow for liquid water.
     * **Distance from Earth:** About 11 light-years.
  9. **Teegarden’s Star b**
     * **Size:** Comparable to Earth.
     * **Potential Habitability:** Orbits within the habitable zone of Teegarden’s Star, a cool red dwarf. Conditions could be suitable for liquid water.
     * **Distance from Earth:** Approximately 12 light-years.
  10. **Barnard’s Star b**
     * **Size:** A super-Earth with a mass of about 3.2 Earth masses.
     * **Potential Habitability:** Located just outside the traditional habitable zone, but still within a range where liquid water could exist under certain conditions.
     * **Distance from Earth:** About 6 light-years.


These discoveries highlight the diverse and intriguing nature of exoplanets found in the last decade. Each of these planets adds valuable information to our understanding of planetary formation, potential habitability, and the search for extraterrestrial life. Continued advancements in detection methods and technologies promise to further expand our knowledge in the years to come.
Was this page helpful?
YesNo
Integrate with ToolsGoogle Colab Tools
On this page
  * Task Output


