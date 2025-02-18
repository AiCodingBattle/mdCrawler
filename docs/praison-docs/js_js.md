PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
JavaScript
JavaScript AI Agents Framework
DocumentationExamplesAgentsUIToolsJS
PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
##### JavaScript
  * JavaScript Agents
  * TypeScript Agents
  * Node.js Agents
  * TypeScript Async
  * Development


PraisonAI is a production-ready Multi AI Agents framework for JavaScript, designed to create AI Agents to automate and solve problems ranging from simple tasks to complex challenges. It provides a low-code solution to streamline the building and management of multi-agent LLM systems, emphasising simplicity, customisation, and effective human-agent collaboration.
📋 Task
🤖 AI Agent
🔧 Tools
📋 Task
🤖 AI Agent
🔧 Tools
▶ Start
⚙ Process
✓ Output
  * JavaScript


1
Install Package
npm
yarn
Copy
```
npm install praisonai

```

2
Set API Key
Copy
```
export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxx

```

3
Create File
Create `app.js` file
## Code Example
Single Agent
Multi Agents
Copy
```
const { Agent } = require('praisonai');
const agent = new Agent({ instructions: 'You are a helpful AI assistant' });
agent.start('Write a movie script about a robot in Mars');

```

4
Run Script
Copy
```
node app.js

```

## 
​
Usage Examples
Single Agent Example
Create and run a single agent to perform a specific task:
Copy
```
const { Agent } = require('praisonai');
// Create a simple science explainer agent
const agent = new Agent({
 instructions: "You are a science expert who explains complex phenomena in simple terms.",
 name: "ScienceExplainer",
 verbose: true
});
// Ask a question
agent.start("Why is the sky blue?")
 .then(response => {
  console.log('\nExplanation:');
  console.log(response);
 })
 .catch(error => console.error('Error:', error));

```

Multi-Agent Example
Create and run multiple agents working together:
Copy
```
const { PraisonAIAgents, Agent } = require('praisonai');
// Create a story agent and a summary agent
const storyAgent = new Agent({
 instructions: "You are a creative storyteller. Create engaging stories.",
 name: "Storyteller"
});
const summaryAgent = new Agent({
 instructions: "You summarize stories into brief, engaging summaries.",
 name: "Summarizer"
});
// Create multi-agent system
const agents = new PraisonAIAgents({
 agents: [storyAgent, summaryAgent],
 tasks: [
  "Create a short story about a magical forest",
  "Summarize the story in 2 sentences"
 ]
});
// Run the agents
agents.start()
 .then(responses => {
  console.log('\nStory:');
  console.log(responses[0]);
  console.log('\nSummary:');
  console.log(responses[1]);
 })
 .catch(error => console.error('Error:', error));

```

Task-Based Agent Example
Create agents with specific tasks and dependencies:
Copy
```
const { Agent, Task } = require('praisonai');
// Create a task-based agent
const agent = new Agent({
 name: "TaskMaster",
 role: "Assistant",
 goal: "Complete tasks efficiently",
 backstory: "You are an AI assistant that helps complete tasks step by step."
});
// Create a task with dependencies
const mainTask = new Task({
 name: "Write Blog Post",
 description: "Write a blog post about artificial intelligence",
 expected_output: "A complete blog post",
 dependencies: []
});
// Execute the task
agent.execute(mainTask)
 .then(response => {
  console.log('\nBlog Post:');
  console.log(response);
 })
 .catch(error => console.error('Error:', error));

```

## 
​
Running the Examples
1
Set Environment Variables
Copy
```
export OPENAI_API_KEY='your-api-key'

```

2
Create Example File
Create a new JavaScript file (e.g., `app.js`) with any of the above examples.
3
Run the Example
Copy
```
node app.js

```

Was this page helpful?
YesNo
TypeScript Agents
On this page
  * Usage Examples
  * Running the Examples


