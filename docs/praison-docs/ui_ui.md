PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
User Interface
User Interface
DocumentationExamplesAgentsUIToolsJS
PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
##### User Interface
  * Overview
  * Gradio
  * Streamlit
  * UI
  * PraisonAI Chat
  * PraisonAI Code


## 
​
Installation
Copy
```
pip install -U "praisonai[ui]"

```

## 
​
Interface Types
## Multi-Agent Systems
Orchestrate multiple agents with UI framework.
## 
​
Features
Agent orchestration, workflow management, inter-agent communication
## 
​
Getting Started
1
Install Dependencies
Each interface has its own installation requirements. Follow the specific guide.
2
Create Application
Use the provided examples and templates to build your application.
3
Customize
Add features and styling to match your needs using the interface’s components.
## 
​
Chainlit
Copy
```
export OPENAI_API_KEY="Enter your API key"
chainlit create-secret
export CHAINLIT_AUTH_SECRET=xxxxxxxx
praisonai ui

```

or
Copy
```
python -m praisonai ui

```

Default Username: admin Default Password: admin
### 
​
To Change Username and Password
create .env file in the root folder of the project Add below Variables and required Username/Password
Copy
```
CHAINLIT_USERNAME=admin
CHAINLIT_USERNAME=admin

```

## 
​
Using Chainlit (with Pictures)
## 
​
Run Automatically
### 
​
Install Required Package
![Install Required Package](https://docs.praison.ai/images/ui-step-1.png)
### 
​
User Interface
![User Interface](https://docs.praison.ai/images/ui-step-2.png)
### 
​
Select Auto Mode
![Select Auto Mode](https://docs.praison.ai/images/ui-step-4.png)
### 
​
Configure Agent Settings
![Configure Agent Settings](https://docs.praison.ai/images/ui-step-3.png)
### 
​
Define a Task to Auto Generate Agents and Run
![Define a Task](https://docs.praison.ai/images/ui-step-5.png)
### 
​
Output
![Output](https://docs.praison.ai/images/ui-step-6.png)
## 
​
Run Manually
### 
​
Select Manual Mode
![Select Manual Mode](https://docs.praison.ai/images/ui-step-7.png)
### 
​
Modify Agents and Tools
![Modify Agents and Tools](https://docs.praison.ai/images/ui-step-10.png)
## 
​
Review Generated Agents
![Review Generated Agents](https://docs.praison.ai/images/ui-step-9.png)
### 
​
Run Agents
![Run Agents](https://docs.praison.ai/images/ui-step-8.png)
### 
​
Manual Model Output
![Manual Model Output](https://docs.praison.ai/images/ui-step-11.png)
Was this page helpful?
YesNo
Gemini Streamlit UIPraisonAI Chat
On this page
  * Installation
  * Interface Types
  * Features
  * Getting Started
  * Chainlit
  * To Change Username and Password
  * Using Chainlit (with Pictures)
  * Run Automatically
  * Install Required Package
  * User Interface
  * Select Auto Mode
  * Configure Agent Settings
  * Define a Task to Auto Generate Agents and Run
  * Output
  * Run Manually
  * Select Manual Mode
  * Modify Agents and Tools
  * Review Generated Agents
  * Run Agents
  * Manual Model Output


