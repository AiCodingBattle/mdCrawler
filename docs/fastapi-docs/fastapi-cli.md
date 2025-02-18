Skip to content 
# FastAPI CLI¶
**FastAPI CLI** is a command line program that you can use to serve your FastAPI app, manage your FastAPI project, and more.
When you install FastAPI (e.g. with `pip install "fastapi[standard]"`), it includes a package called `fastapi-cli`, this package provides the `fastapi` command in the terminal.
To run your FastAPI app for development, you can use the `fastapi dev` command:
```

fast →

```

The command line program called `fastapi` is **FastAPI CLI**.
FastAPI CLI takes the path to your Python program (e.g. `main.py`) and automatically detects the `FastAPI` instance (commonly named `app`), determines the correct import process, and then serves it.
For production you would use `fastapi run` instead. 🚀
Internally, **FastAPI CLI** uses Uvicorn, a high-performance, production-ready, ASGI server. 😎
## `fastapi dev`¶
Running `fastapi dev` initiates development mode.
By default, **auto-reload** is enabled, automatically reloading the server when you make changes to your code. This is resource-intensive and could be less stable than when it's disabled. You should only use it for development. It also listens on the IP address `127.0.0.1`, which is the IP for your machine to communicate with itself alone (`localhost`).
## `fastapi run`¶
Executing `fastapi run` starts FastAPI in production mode by default.
By default, **auto-reload** is disabled. It also listens on the IP address `0.0.0.0`, which means all the available IP addresses, this way it will be publicly accessible to anyone that can communicate with the machine. This is how you would normally run it in production, for example, in a container.
In most cases you would (and should) have a "termination proxy" handling HTTPS for you on top, this will depend on how you deploy your application, your provider might do this for you, or you might need to set it up yourself.
Tip
You can learn more about it in the deployment documentation.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
