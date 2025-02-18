PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Features
Generate Synthetic Reasoning Data Agents
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


Start
Question Answer Generator Agent
Evaluator Agent
Reasoning Steps / COT Generator Agent
HuggingFace Uploader Agent
End
## 
​
What is Chain-of-Thought Generation?
Chain-of-Thought (CoT) Generation is a process where AI agents create detailed, step-by-step reasoning paths for solving problems. This involves generating questions, evaluating them, producing detailed solution steps, and making the data available for training and analysis.
## 
​
Quick Start
1
Install Package
First, install the PraisonAI Agents package:
Copy
```
pip install "praisonaiagents[llm]" datasets huggingface-hub pandas

```

2
Set API Key
Set your OpenAI API key as an environment variable in your terminal:
Copy
```
export OPENAI_API_KEY=your_api_key_here
export HF_TOKEN=your_huggingface_token_here

```

3
Create a file
Create a new file `app.py` with the basic setup:
Copy
```
from praisonaiagents import Agent, Task, PraisonAIAgents
from praisonaiagents.tools import cot_save, cot_upload_to_huggingface
from pydantic import BaseModel
import os
# Define Pydantic model for structured output
class DecisionModel(BaseModel):
  response: str
  decision: str
def write_csv(file_path, data):
  """Write data to CSV file."""
  if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
      file.write(data + '\n')
  else:
    with open(file_path, 'a') as file:
      file.write(data + '\n')
  return f"Data appended to {file_path}"
def count_questions(file_path):
  """Count lines in file."""
  with open(file_path, 'r') as file:
    return sum(1 for _ in file)
# Create specialized agents
qa_generator = Agent(
  name="Generator",
  role="Question Creator",
  goal="Create challenging math and logic questions",
  backstory="Expert in educational content creation",
  llm="gpt-4o-mini",
  tools=[write_csv, count_questions]
)
total_questions_evaluator = Agent(
  name="TotalQuestionsEvaluator",
  role="Total Questions Evaluator",
  goal="Evaluate the total number of questions in qa_pairs.csv file",
  backstory="Expert in evaluating the total number of questions in a file",
  llm="gpt-4o-mini",
  tools=[count_questions],
  verbose=False
)
cot_generator = Agent(
  name="COTGenerator",
  role="Chain of Thought Specialist",
  goal="Generate and manage chain of thought solutions for Q&A pairs",
  backstory="Expert in breaking down problems and generating detailed solution steps",
  tools=[cot_save],
  llm="gpt-4o-mini",
  verbose=False
)
upload_to_huggingface = Agent(
  name="UploadToHuggingface",
  role="Upload to Huggingface",
  goal="Upload the generated chain of thought solutions to a Huggingface dataset",
  backstory="Expert in saving data to Huggingface",
  tools=[cot_upload_to_huggingface],
  llm="gpt-4o-mini",
  verbose=False
)
# Define tasks with workflow
generate_task = Task(
  description="""Generate question and answer in csv format without headers: question, answer and append to qa_pairs.csv file
generate 10 unique questions and answers and don't repeat on the same question and answer. Reponse with 'done' when done
with append mode as 'a'
Example question and answer:
question, answer
What is the sum of numbers from 1 to 10?, 55
Number of r's in the word strawberry, 3
""",
  expected_output="append to qa_pairs.csv file with questions and answers and move to next task",
  agent=qa_generator,
  name="generate_task",
  is_start=True,
  next_tasks=["evaluate_total_questions"],
  task_type="decision",
  condition={
    "more": "generate_task",
    "done": "evaluate_total_questions"
  }
)
evaluate_total_questions_task = Task(
  description="Evaluate the total number of questions in qa_pairs.csv file is 1",
  expected_output="Total number of questions in qa_pairs.csv file",
  agent=total_questions_evaluator,
  task_type="decision",
  name="evaluate_total_questions",
  condition={
    "more": "generate_task",
    "done": "generate_cot"
  }
)
generate_cot_task = Task(
  name="generate_cot",
  description="""Generate chain of thought solutions for each question in the input file. 
Save to cot_solutions.csv file
Don't generate chain of thought solutions again after receiving the response from Tool Call
After calling the tool, respond with a JSON object:
{
  "response": "done",
  "decision": "done"
}
""",
  expected_output="done",
  agent=cot_generator,
  input_file="qa_pairs.csv",
  task_type="loop",
  next_tasks=["upload_to_huggingface"],
  condition={
    "done": ["upload_to_huggingface"],
    "exit": [],
  },
  output_pydantic=DecisionModel # Use Pydantic model for output validation
)
upload_to_huggingface_task = Task(
  name="upload_to_huggingface",
  description="""Upload to Huggingface:
  1. Save to cot_solutions.csv
  2. Upload to mervinpraison/cot-dataset""",
  expected_output="Dataset published successfully",
  agent=upload_to_huggingface,
  tools=[cot_upload_to_huggingface]
)
# Initialize workflow
agents = PraisonAIAgents(
  agents=[qa_generator, total_questions_evaluator, cot_generator, upload_to_huggingface],
  tasks=[generate_task, evaluate_total_questions_task, generate_cot_task, upload_to_huggingface_task],
  process="workflow",
  max_iter=30,
  verbose=False
)
agents.start()

```

4
Run the application
Execute the Python script to start generating chain-of-thought data:
Copy
```
python app.py

```

## 
​
Features
## Question Generation
Create challenging math and logic questions with answers.
## Question Evaluation
Evaluate and validate generated questions for quality.
## CoT Solutions
Generate detailed chain-of-thought solutions for each question.
## Data Management
Save and manage generated data in structured formats.
## HuggingFace Integration
Upload datasets directly to HuggingFace for sharing.
## 
​
Understanding the Workflow
Key Components
## Question Generator
Creates unique math and logic questions with answers. Uses `write_csv` and `count_questions` tools.
## Questions Evaluator
Validates the total number of generated questions. Uses `count_questions` tool.
## CoT Generator
Produces detailed step-by-step solutions. Uses `cot_save` tool for solution management.
## HuggingFace Uploader
Publishes datasets to HuggingFace. Uses `cot_upload_to_huggingface` tool.
Task Types and Flow Control
  * Decision Tasks
  * Loop Tasks


Used in question generation and evaluation phases.
Decision Task Example
Copy
```
generate_task = Task(
  task_type="decision",
  condition={
    "more": "generate_task",
    "done": "evaluate_total_questions"
  }
)

```

Conditions determine whether to continue generating or move forward. The task can loop back to itself or proceed to the next task.
Each task type serves a specific purpose in the workflow:
  * **Decision Tasks** : Control flow and branching logic
  * **Loop Tasks** : Process data iteratively with validation


## 
​
Next Steps
## Introduction
Learn more about PraisonAI and its core concepts
## Quick Start
Get started with the basics of PraisonAI
Was this page helpful?
YesNo
Mini AI AgentsCode Agent
On this page
  * What is Chain-of-Thought Generation?
  * Quick Start
  * Features
  * Understanding the Workflow
  * Next Steps


