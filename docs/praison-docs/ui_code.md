PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
User Interface
PraisonAI Code
DocumentationExamplesAgentsUIToolsJS
PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
##### User Interface
  * Overview
  * Gradio
  * Streamlit
  * UI
  * PraisonAI Chat
  * PraisonAI Code


PraisonAI Code helps you to interact with your whole codebase using the power of AI.
## 
​
Different User Interfaces:
Interface| Description| URL  
---|---|---  
**UI**|  Multi Agents such as CrewAI or AutoGen| https://docs.praison.ai/ui/ui  
**Chat**|  Chat with 100+ LLMs, single AI Agent| https://docs.praison.ai/ui/chat  
**Code**|  Chat with entire Codebase, single AI Agent| https://docs.praison.ai/ui/code  
## 
​
Table of Contents
  * Install PraisonAI Code
  * Other Models
  * To Use Gemini 1.5
  * Ignore Files
    * Using .praisonignore
    * Using settings.yaml
    * Using .env File
    * Using Environment Variables in the Terminal
  * Include Files
  * Set Max Tokens


## 
​
Install PraisonAI Code
Copy
```
pip install "praisonai[code]"

```

Copy
```
export OPENAI_API_KEY=xxxxxxxx

```

Copy
```
praisonai code

```

  1. Username and Password will be asked for the first time. `admin` is the default username and password.
  2. Set Model name to be gpt-4o-mini in the settings


## 
​
Other Models
  * Use 100+ LLMs - Litellm
  * Includes Gemini 1.5 for 2 Million Context Length


## 
​
To Use Gemini 1.5
  * `export GEMINI_API_KEY=xxxxxxxxx`
  * `praisonai code`
  * Set Model name to be `gemini/gemini-1.5-flash` in the settings


## 
​
Ignore Files
### 
​
Using .praisonignore
  * Create a `.praisonignore` file in the root folder of the project
  * Add files to ignore


Copy
```
.*
*.pyc
pycache
.git
.gitignore
.vscode
.idea
.DS_Store
.lock
.pyc
.env

```

### 
​
Using settings.yaml
(.praisonignore is preferred)
  * Create a `settings.yaml` file in the root folder of the project
  * Add below Variables and required Ignore Files


Copy
```
code:
 ignore_files:
 - ".*"
 - "*.pyc"
 - "pycache"
 - ".git"
 - ".gitignore"
 - ".vscode"
 - ".idea"
 - ".DS_Store"
 - ".lock"
 - ".pyc"
 - ".env"

```

### 
​
Using .env File
  * Create a `.env` file in the root folder of the project
  * Add below Variables and required Ignore Files


Copy
```
PRAISONAI_IGNORE_FILES=".*,*.pyc,__pycache__,.git,.gitignore,.vscode"

```

### 
​
Using Environment Variables in the Terminal
Copy
```
export PRAISONAI_IGNORE_FILES=".*,*.pyc,__pycache__,.git,.gitignore,.vscode"

```

## 
​
Include Files .praisoninclude
  * Add files you wish to Include files in the context
  * This will include the files/folders mentioned in `.praisoninclude` to the original context (files in the folder - .gitignore - .praisonignore)


  * Create a `.praisoninclude` file in the root folder of the project
  * Add files to Include


Copy
```
projectfiles
docs

```

## 
​
Include ONLY these Files .praisoncontext (Context)
  * Add files you wish to Include files in the context
  * This will include ONLY the files/folders mentioned in `.praisoncontext` to the context


  * Create a `.praisoncontext` file in the root folder of the project
  * Add files to Include


Copy
```
projectfiles
docs

```

## 
​
Set Max Tokens
Note: By Default Max Tokens set is 900,000
Copy
```
export PRAISONAI_MAX_TOKENS=1000000

```

or
  * Create a .env file in the root folder of the project
  * Add below Variables and required Max Tokens
  * Copy
```
PRAISONAI_MAX_TOKENS=1000000

```



## 
​
Default DB Location
`~/.praison/database.sqlite`
## 
​
Key Features
### 
​
Internet Search
PraisonAI Code now includes internet search capabilities using Crawl4AI and Tavily. This feature allows you to retrieve up-to-date information and code snippets during your coding sessions, enhancing your ability to find relevant programming information and examples.
To use this feature:
  1. Ask a question or request information about a specific coding topic
  2. The AI will use internet search to find the most relevant and current information
  3. You’ll receive code snippets, documentation references, or explanations based on the latest available resources


### 
​
Vision Language Model (VLM) Support
While primarily designed for code interactions, PraisonAI Code also supports Vision Language Model capabilities. This feature can be particularly useful when dealing with visual aspects of programming, such as UI design, data visualization, or understanding code structure through diagrams.
To use this feature:
  1. Upload an image related to your coding query (e.g., a screenshot of a UI, a flowchart, or a code snippet image)
  2. Ask questions or request analysis based on the uploaded image
  3. The VLM will process the image and provide insights or answers based on its visual content, helping you understand or implement the visual concepts in your code


These new features significantly expand the capabilities of PraisonAI Code, allowing for more comprehensive and up-to-date coding assistance.
## 
​
Local Docker Development with Live Reload
To facilitate local development with live reload, you can use Docker. Follow the steps below:
  1. **Create a`Dockerfile.dev`** :
Copy
```
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask praisonai==2.0.18 watchdog
EXPOSE 5555
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]

```

  2. **Create a`docker-compose.yml`** :
Copy
```
version: '3.8'
services:
 app:
  build:
   context: .
   dockerfile: Dockerfile.dev
  volumes:
   - .:/app
  ports:
   - "5555:5555"
  environment:
   FLASK_ENV: development
  command: flask run --host=0.0.0.0
 watch:
  image: alpine:latest
  volumes:
   - .:/app
  command: sh -c "apk add --no-cache inotify-tools && while inotifywait -r -e modify,create,delete /app; do kill -HUP 1; done"

```

  3. **Run Docker Compose** :
Copy
```
docker-compose up

```



This setup will allow you to develop locally with live reload, making it easier to test and iterate on your code.
Was this page helpful?
YesNo
PraisonAI Chat
On this page
  * Different User Interfaces:
  * Table of Contents
  * Install PraisonAI Code
  * Other Models
  * To Use Gemini 1.5
  * Ignore Files
  * Using .praisonignore
  * Using settings.yaml
  * Using .env File
  * Using Environment Variables in the Terminal
  * Include Files .praisoninclude
  * Include ONLY these Files .praisoncontext (Context)
  * Set Max Tokens
  * Default DB Location
  * Key Features
  * Internet Search
  * Vision Language Model (VLM) Support
  * Local Docker Development with Live Reload


