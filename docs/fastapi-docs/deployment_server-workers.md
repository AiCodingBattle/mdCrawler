Skip to content 
# Server Workers - Uvicorn with Workers¶
Let's check back those deployment concepts from before:
  * Security - HTTPS
  * Running on startup
  * Restarts
  * **Replication (the number of processes running)**
  * Memory
  * Previous steps before starting


Up to this point, with all the tutorials in the docs, you have probably been running a **server program** , for example, using the `fastapi` command, that runs Uvicorn, running a **single process**.
When deploying applications you will probably want to have some **replication of processes** to take advantage of **multiple cores** and to be able to handle more requests.
As you saw in the previous chapter about Deployment Concepts, there are multiple strategies you can use.
Here I'll show you how to use **Uvicorn** with **worker processes** using the `fastapi` command or the `uvicorn` command directly.
Info
If you are using containers, for example with Docker or Kubernetes, I'll tell you more about that in the next chapter: FastAPI in Containers - Docker.
In particular, when running on **Kubernetes** you will probably **not** want to use workers and instead run **a single Uvicorn process per container** , but I'll tell you about it later in that chapter.
## Multiple Workers¶
You can start multiple workers with the `--workers` command line option:
`fastapi``uvicorn`
If you use the `fastapi` command:
```

fast →fastapi run --workers 4 _main.py_  FastAPI  Starting production server 🚀       Searching for package file structure from directories with       __init__.py files       Importing from /home/user/code/awesomeapp   module  🐍 main.py    code  Importing the FastAPI app object from the module with the       following code:       _from __**main**__ import __**app**_    app  Using import string: main:app   server  Server started at _http://0.0.0.0:8000_   server  Documentation at _http://0.0.0.0:8000/docs_       Logs:    INFO  Uvicorn running on _http://0.0.0.0:8000_ **(**Press CTRL+C to       quit**)**    INFO  Started parent process **[****27365****]**    INFO  Started server process **[****27368****]**    INFO  Started server process **[****27369****]**    INFO  Started server process **[****27370****]**    INFO  Started server process **[****27367****]**    INFO  Waiting for application startup.    INFO  Waiting for application startup.    INFO  Waiting for application startup.    INFO  Waiting for application startup.    INFO  Application startup complete.    INFO  Application startup complete.    INFO  Application startup complete.    INFO  Application startup complete.restart ↻

```

If you prefer to use the `uvicorn` command directly:
```

fast →

```

The only new option here is `--workers` telling Uvicorn to start 4 worker processes.
You can also see that it shows the **PID** of each process, `27365` for the parent process (this is the **process manager**) and one for each worker process: `27368`, `27369`, `27370`, and `27367`.
## Deployment Concepts¶
Here you saw how to use multiple **workers** to **parallelize** the execution of the application, take advantage of **multiple cores** in the CPU, and be able to serve **more requests**.
From the list of deployment concepts from above, using workers would mainly help with the **replication** part, and a little bit with the **restarts** , but you still need to take care of the others:
  * **Security - HTTPS**
  * **Running on startup**
  * **_Restarts_**
  * Replication (the number of processes running)
  * **Memory**
  * **Previous steps before starting**


## Containers and Docker¶
In the next chapter about FastAPI in Containers - Docker I'll explain some strategies you could use to handle the other **deployment concepts**.
I'll show you how to **build your own image from scratch** to run a single Uvicorn process. It is a simple process and is probably what you would want to do when using a distributed container management system like **Kubernetes**.
## Recap¶
You can use multiple worker processes with the `--workers` CLI option with the `fastapi` or `uvicorn` commands to take advantage of **multi-core CPUs** , to run **multiple processes in parallel**.
You could use these tools and ideas if you are setting up **your own deployment system** while taking care of the other deployment concepts yourself.
Check out the next chapter to learn about **FastAPI** with containers (e.g. Docker and Kubernetes). You will see that those tools have simple ways to solve the other **deployment concepts** as well. ✨
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
