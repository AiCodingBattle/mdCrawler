PraisonAI Documentation home page![light logo](https://docs.praison.ai/images/praisonai-logo-large-dark.png)![dark logo](https://docs.praison.ai/images/praisonai-logo-large-light.png)
Search...
Ctrl K
Search...
Navigation
User Interface
PraisonAI Chat
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
Different User Interfaces:
Interface| Description| URL  
---|---|---  
**UI**|  Multi Agents such as CrewAI or AutoGen| https://docs.praison.ai/ui/ui  
**Chat**|  Chat with 100+ LLMs, single AI Agent| https://docs.praison.ai/ui/chat  
**Code**|  Chat with entire Codebase, single AI Agent| https://docs.praison.ai/ui/code  
## 
​
Quick Start
  1. Install PraisonAI Chat:


Copy
```
pip install "praisonai[chat]"

```

  1. Set up your OpenAI API key:


Copy
```
export OPENAI_API_KEY=xxxxxxxx

```

  1. Set up your Database URL:


Copy
```
export DATABASE_URL=postgresql+asyncpg://<username>:<password>@<your-db-instance-url>/<database-name>

```

  1. Launch PraisonAI Chat:


Copy
```
praisonai chat

```

  1. URL : http://localhost:8084/
  2. Username: admin
  3. Password: admin
  4. Set Model name to be gpt-4o-mini in the settings


## 
​
Key Features
### 
​
Internet Search
PraisonAI Chat now includes internet search capabilities using Crawl4AI and Tavily. This feature allows you to retrieve up-to-date information during your conversations, enhancing the AI’s ability to provide current and relevant information.
### 
​
Vision Language Model (VLM) Support
You can now upload images and ask questions based on them using Vision Language Models. This multimodal support enables visual understanding and analysis within your chat sessions, allowing for a more comprehensive interaction with the AI.
To use this feature:
  1. Upload an image to the chat interface
  2. Ask questions or request analysis based on the uploaded image
  3. The VLM will process the image and provide insights or answers based on its visual content


These new features significantly expand the capabilities of PraisonAI Chat, allowing for more diverse and informative interactions.
## 
​
Custom Database
PraisonAI Chat supports custom database configurations, allowing you to use PostgreSQL or other databases instead of the default SQLite database. This is particularly useful for production environments or when you need more advanced database features.
### 
​
PostgreSQL Configuration
To use PostgreSQL as your database backend:
  1. **Install Required Dependencies**
For local development:
Copy
```
pip install asyncpg

```

For Replit:
     * Open the “Packages” tab in the Tools section
     * Search for and install: 
       * `python3-dev`
       * `libpq-dev`
     * Then install Python packages:
Copy
```
pip install asyncpg

```

  2. **Set Environment Variables** Add these variables to your `.env` file or Replit Secrets:
Copy
```
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<your-db-instance-url>/<database-name>
DATABASE_SSL=true # Required for most cloud PostgreSQL services

```

For Replit:
     * Click on “Tools” in the left sidebar
     * Select “Secrets”
     * Add your database configuration as `DATABASE_URL`
  3. **Database Tables** The application will automatically:
     * Detect PostgreSQL connections
     * Create all necessary tables if they don’t exist
     * Set up proper indexes and constraints
     * Handle table creation errors
  4. **Cloud Database Services** For Replit, we recommend using cloud database services that provide free tiers:
     * Neon (Recommended)
     * Supabase
     * ElephantSQL
These services provide:
     * Free PostgreSQL hosting
     * Automatic SSL configuration
     * Connection string ready to use


### 
​
Default Configuration
If no `DATABASE_URL` is provided, PraisonAI Chat will automatically use SQLite with the following default configuration:
Copy
```
DATABASE_URL=sqlite+aiosqlite:///{HOME}/.praison/database.sqlite

```

### 
​
Supported Database Types
PraisonAI Chat supports various database backends through SQLAlchemy:
  * PostgreSQL (recommended for production)
  * MySQL/MariaDB
  * SQLite (default)
  * Oracle
  * Microsoft SQL Server


For other database types, refer to the SQLAlchemy documentation for the correct connection string format.
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
UIPraisonAI Code
On this page
  * Different User Interfaces:
  * Quick Start
  * Key Features
  * Internet Search
  * Vision Language Model (VLM) Support
  * Custom Database
  * PostgreSQL Configuration
  * Default Configuration
  * Supported Database Types
  * Local Docker Development with Live Reload


