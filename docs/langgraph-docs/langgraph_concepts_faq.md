Skip to content 
# FAQ¶
Common questions and their answers!
## Do I need to use LangChain to use LangGraph? What’s the difference?¶
No. LangGraph is an orchestration framework for complex agentic systems and is more low-level and controllable than LangChain agents. LangChain provides a standard interface to interact with models and other components, useful for straight-forward chains and retrieval flows.
## How is LangGraph different from other agent frameworks?¶
Other agentic frameworks can work for simple, generic tasks but fall short for complex tasks bespoke to a company’s needs. LangGraph provides a more expressive framework to handle companies’ unique tasks without restricting users to a single black-box cognitive architecture.
## Does LangGraph impact the performance of my app?¶
LangGraph will not add any overhead to your code and is specifically designed with streaming workflows in mind.
## Is LangGraph open source? Is it free?¶
Yes. LangGraph is an MIT-licensed open-source library and is free to use.
## How are LangGraph and LangGraph Platform different?¶
LangGraph is a stateful, orchestration framework that brings added control to agent workflows. LangGraph Platform is a service for deploying and scaling LangGraph applications, with an opinionated API for building agent UXs, plus an integrated developer studio.
Features | LangGraph (open source) | LangGraph Platform  
---|---|---  
Description | Stateful orchestration framework for agentic applications | Scalable infrastructure for deploying LangGraph applications  
SDKs | Python and JavaScript | Python and JavaScript  
HTTP APIs | None | Yes - useful for retrieving & updating state or long-term memory, or creating a configurable assistant  
Streaming | Basic | Dedicated mode for token-by-token messages  
Checkpointer | Community contributed | Supported out-of-the-box  
Persistence Layer | Self-managed | Managed Postgres with efficient storage  
Deployment | Self-managed | • Cloud SaaS • Free self-hosted • Enterprise (BYOC or paid self-hosted)  
Scalability | Self-managed | Auto-scaling of task queues and servers  
Fault-tolerance | Self-managed | Automated retries  
Concurrency Control | Simple threading | Supports double-texting  
Scheduling | None | Cron scheduling  
Monitoring | None | Integrated with LangSmith for observability  
IDE integration | LangGraph Studio for Desktop | LangGraph Studio for Desktop & Cloud  
## What are my deployment options for LangGraph Platform?¶
We currently have the following deployment options for LangGraph applications:
  * ‍Self-Hosted Lite: A free (up to 1M nodes executed), limited version of LangGraph Platform that you can run locally or in a self-hosted manner. This version requires a LangSmith API key and logs all usage to LangSmith. Fewer features are available than in paid plans.
  * Cloud SaaS: Fully managed and hosted as part of LangSmith, with automatic updates and zero maintenance.
  * ‍Bring Your Own Cloud (BYOC): Deploy LangGraph Platform within your VPC, provisioned and run as a service. Keep data in your environment while outsourcing the management of the service.
  * Self-Hosted Enterprise: Deploy LangGraph entirely on your own infrastructure.


## Is LangGraph Platform open source?¶
No. LangGraph Platform is proprietary software.
There is a free, self-hosted version of LangGraph Platform with access to basic features. The Cloud SaaS deployment option is free while in beta, but will eventually be a paid service. We will always give ample notice before charging for a service and reward our early adopters with preferential pricing. The Bring Your Own Cloud (BYOC) and Self-Hosted Enterprise options are also paid services. Contact our sales team to learn more.
For more information, see our LangGraph Platform pricing page.
## Does LangGraph work with LLMs that don't support tool calling?¶
Yes! You can use LangGraph with any LLMs. The main reason we use LLMs that support tool calling is that this is often the most convenient way to have the LLM make its decision about what to do. If your LLM does not support tool calling, you can still use it - you just need to write a bit of logic to convert the raw LLM string response to a decision about what to do.
## Does LangGraph work with OSS LLMs?¶
Yes! LangGraph is totally ambivalent to what LLMs are used under the hood. The main reason we use closed LLMs in most of the tutorials is that they seamlessly support tool calling, while OSS LLMs often don't. But tool calling is not necessary (see this section) so you can totally use LangGraph with OSS LLMs.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! Please help us improve this page by adding to the discussion below. 
## Comments
Back to top 
