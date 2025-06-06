Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# Debugging and Monitoring
Applications that use LLMs have some challenges that are well known and understood: LLMs are **slow** , **unreliable** and **expensive**.
These applications also have some challenges that most developers have encountered much less often: LLMs are **fickle** and **non-deterministic**. Subtle changes in a prompt can completely change a model's performance, and there's no `EXPLAIN` query you can run to understand why.
Warning
From a software engineers point of view, you can think of LLMs as the worst database you've ever heard of, but worse.
If LLMs weren't so bloody useful, we'd never touch them.
To build successful applications with LLMs, we need new tools to understand both model performance, and the behavior of applications that rely on them.
LLM Observability tools that just let you understand how your model is performing are useless: making API calls to an LLM is easy, it's building that into an application that's hard.
## Pydantic Logfire
Pydantic Logfire is an observability platform developed by the team who created and maintain Pydantic and PydanticAI. Logfire aims to let you understand your entire application: Gen AI, classic predictive AI, HTTP traffic, database queries and everything else a modern application needs.
Pydantic Logfire is a commercial product
Logfire is a commercially supported, hosted platform with an extremely generous and perpetual free tier. You can sign up and start using Logfire in a couple of minutes.
PydanticAI has built-in (but optional) support for Logfire via the `logfire-api` no-op package.
That means if the `logfire` package is installed and configured, detailed information about agent runs is sent to Logfire. But if the `logfire` package is not installed, there's virtually no overhead and nothing is sent.
Here's an example showing details of running the Weather Agent in Logfire:
![Weather Agent Logfire](https://ai.pydantic.dev/img/logfire-weather-agent.png)
## Using Logfire
To use logfire, you'll need a logfire account, and logfire installed:
pipuv
```
pipinstall'pydantic-ai[logfire]'

```

```
uvadd'pydantic-ai[logfire]'

```

Then authenticate your local environment with logfire:
pipuv
```
logfireauth

```

```
uvrunlogfireauth

```

And configure a project to send data to:
pipuv
```
logfireprojectsnew

```

```
uvrunlogfireprojectsnew

```

(Or use an existing project with `logfire projects use`)
The last step is to add logfire to your code:
adding_logfire.py```
import logfire
logfire.configure()

```

The logfire documentation has more details on how to use logfire, including how to instrument other libraries like Pydantic, HTTPX and FastAPI.
Since Logfire is build on OpenTelemetry, you can use the Logfire Python SDK to send data to any OpenTelemetry collector.
Once you have logfire set up, there are two primary ways it can help you understand your application:
  * **Debugging** — Using the live view to see what's happening in your application in real-time.
  * **Monitoring** — Using SQL and dashboards to observe the behavior of your application, Logfire is effectively a SQL database that stores information about how your application is running.


### Debugging
To demonstrate how Logfire can let you visualise the flow of a PydanticAI run, here's the view you get from Logfire while running the chat app examples:
### Monitoring Performance
We can also query data with SQL in Logfire to monitor the performance of an application. Here's a real world example of using Logfire to monitor PydanticAI runs inside Logfire itself:
![Logfire monitoring PydanticAI](https://ai.pydantic.dev/img/logfire-monitoring-pydanticai.png)
### Monitoring HTTPX Requests
In order to monitor HTTPX requests made by models, you can use `logfire`'s HTTPX integration.
Instrumentation is as easy as adding the following three lines to your application:
instrument_httpx.py```
import logfire
logfire.configure()
logfire.instrument_httpx(capture_all=True) 

```

In particular, this can help you to trace specific requests, responses, and headers:
instrument_httpx_example.py```
import logfire
from pydantic_ai import Agent
logfire.configure()
logfire.instrument_httpx(capture_all=True) 
agent = Agent('openai:gpt-4o')
result = agent.run_sync('What is the capital of France?')
print(result.data)
#> The capital of France is Paris.

```

With `httpx` instrumentationWithout `httpx` instrumentation
![Logfire with HTTPX instrumentation](https://ai.pydantic.dev/img/logfire-with-httpx.png)
![Logfire without HTTPX instrumentation](https://ai.pydantic.dev/img/logfire-without-httpx.png)
Tip
`httpx` instrumentation might be of particular utility if you're using a custom `httpx` client in your model in order to get insights into your custom requests.
