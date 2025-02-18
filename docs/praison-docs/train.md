PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
Other Features
PraisonAI Train
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
To upload to Huggingface
Copy
```
export HF_TOKEN=xxxxxxxxxxxxxx

```

## 
​
Initilise praisonai train
Copy
```
praisonai train init

```

## 
​
Required
  1. Huggingface token
  2. Base model to train on (e.g. unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit)
  3. Dataset to train on (e.g. yahma/alpaca-cleaned)
  4. Huggingface model name to upload to (e.g. mervinpraison/llama3.1-instruct) (Optional)
  5. Ollama model name to upload to (e.g. mervinpraison/llama3.1-instruct) (Optional)


## 
​
To upload to ollama.com (Linux)
Copy
```
sudo cat /usr/share/ollama/.ollama/id_ed25519.pub

```

Save the output from above to ollama.com —> Ollama keys
## 
​
RUN PraisonAI Train
Copy
```
praisonai train \
  --model unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit \
  --dataset yahma/alpaca-cleaned \
  --hf mervinpraison/llama3.1-instruct \
  --ollama mervinpraison/llama3.1-instruct

```

Note: PraisonAI Train currently tested on Linux with 1 GPU. With pytorch-cuda=12.1
## 
​
Config.yaml example
Copy
```
ollama_save: "true"
huggingface_save: "true"
train: "true"
model_name: "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
hf_model_name: "mervinpraison/llama-3.1-instruct"
ollama_model: "mervinpraison/llama3.1-instruct"
model_parameters: "8b"
dataset:
 - name: "yahma/alpaca-cleaned"
  split_type: "train"
  processing_func: "format_prompts"
  rename:
   input: "input"
   output: "output"
   instruction: "instruction"
  filter_data: false
  filter_column_value: "id"
  filter_value: "alpaca"
  num_samples: 20000
dataset_text_field: "text"
dataset_num_proc: 2
packing: false
max_seq_length: 2048
load_in_4bit: true
lora_r: 16
lora_target_modules: 
 - "q_proj"
 - "k_proj"
 - "v_proj"
 - "o_proj"
 - "gate_proj"
 - "up_proj"
 - "down_proj"
lora_alpha: 16
lora_dropout: 0
lora_bias: "none"
use_gradient_checkpointing: "unsloth"
random_state: 3407
use_rslora: false
loftq_config: null
per_device_train_batch_size: 2
gradient_accumulation_steps: 2
warmup_steps: 5
num_train_epochs: 1
max_steps: 10
learning_rate: 2.0e-4
logging_steps: 1
optim: "adamw_8bit"
weight_decay: 0.01
lr_scheduler_type: "linear"
seed: 3407
output_dir: "outputs"
quantization_method: 
 - "q4_k_m"

```

Copy
```
praisonai train

```

## 
​
wandb
Copy
```
wandb login

```

Get the key from here
Copy
```
export PRAISON_WANDB=True
export WANDB_LOG_MODEL=checkpoint
export WANDB_PROJECT=praisonai-test
export PRAISON_WANDB_RUN_NAME=praisonai-train 

```

Was this page helpful?
YesNo
Firecrawl PraisonAI IntegrationCrewAI with PraisonAI
On this page
  * To upload to Huggingface
  * Initilise praisonai train
  * Required
  * To upload to ollama.com (Linux)
  * RUN PraisonAI Train
  * Config.yaml example
  * wandb


