Skip to content 
# Templating - `Jinja2Templates`¶
You can use the `Jinja2Templates` class to render Jinja templates.
Read more about it in the FastAPI docs for Templates.
You can import it directly from `fastapi.templating`:
```
fromfastapi.templatingimport Jinja2Templates

```

##  fastapi.templating.Jinja2Templates ¶
```
Jinja2Templates(
  directory: (
    str | PathLike[str] | Sequence[str | PathLike[str]]
  ),
  *,
  context_processors: (
    list[Callable[[Request], dict[str, Any]]] | None
  ) = None,
  **env_options: Any
)

```

```
Jinja2Templates(
  *,
  env: Environment,
  context_processors: (
    list[Callable[[Request], dict[str, Any]]] | None
  ) = None
)

```

```
Jinja2Templates(
  directory=None,
  *,
  context_processors=None,
  env=None,
  **env_options
)

```

templates = Jinja2Templates("templates")
return templates.TemplateResponse("index.html", {"request": request})
PARAMETER | DESCRIPTION  
---|---  
`directory` |  **TYPE:** `str | PathLike[str] | Sequence[str | PathLike[str]] | None` **DEFAULT:** `None`  
`context_processors` |  **TYPE:** `list[Callable[[Request], dict[str, Any]]] | None` **DEFAULT:** `None`  
`env` |  **TYPE:** `Environment | None` **DEFAULT:** `None`  
`**env_options` |  **TYPE:** `Any` **DEFAULT:** `{}`  
Source code in `starlette/templating.py`
```
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
```
| ```
def__init__(
  self,
  directory: str | PathLike[str] | typing.Sequence[str | PathLike[str]] | None = None,
  *,
  context_processors: list[typing.Callable[[Request], dict[str, typing.Any]]] | None = None,
  env: jinja2.Environment | None = None,
  **env_options: typing.Any,
) -> None:
  if env_options:
    warnings.warn(
      "Extra environment options are deprecated. Use a preconfigured jinja2.Environment instead.",
      DeprecationWarning,
    )
  assert jinja2 is not None, "jinja2 must be installed to use Jinja2Templates"
  assert bool(directory) ^ bool(env), "either 'directory' or 'env' arguments must be passed"
  self.context_processors = context_processors or []
  if directory is not None:
    self.env = self._create_env(directory, **env_options)
  elif env is not None: # pragma: no branch
    self.env = env
  self._setup_env_defaults(self.env)

```
  
---|---  
###  context_processors `instance-attribute` ¶
```
context_processors = context_processors or []

```

###  env `instance-attribute` ¶
```
env = _create_env(directory, **env_options)

```

###  get_template ¶
```
get_template(name)

```

PARAMETER | DESCRIPTION  
---|---  
`name` |  **TYPE:** `str`  
Source code in `starlette/templating.py`
```
130
131
```
| ```
defget_template(self, name: str) -> jinja2.Template:
  return self.env.get_template(name)

```
  
---|---  
###  TemplateResponse ¶
```
TemplateResponse(
  request: Request,
  name: str,
  context: dict[str, Any] | None = None,
  status_code: int = 200,
  headers: Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> _TemplateResponse

```

```
TemplateResponse(
  name: str,
  context: dict[str, Any] | None = None,
  status_code: int = 200,
  headers: Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> _TemplateResponse

```

```
TemplateResponse(*args, **kwargs)

```

PARAMETER | DESCRIPTION  
---|---  
`*args` |  **TYPE:** `Any` **DEFAULT:** `()`  
`**kwargs` |  **TYPE:** `Any` **DEFAULT:** `{}`  
Source code in `starlette/templating.py`
```
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
```
| ```
defTemplateResponse(self, *args: typing.Any, **kwargs: typing.Any) -> _TemplateResponse:
  if args:
    if isinstance(args[0], str): # the first argument is template name (old style)
      warnings.warn(
        "The `name` is not the first parameter anymore. "
        "The first parameter should be the `Request` instance.\n"
        'Replace `TemplateResponse(name, {"request": request})` by `TemplateResponse(request, name)`.',
        DeprecationWarning,
      )
      name = args[0]
      context = args[1] if len(args) > 1 else kwargs.get("context", {})
      status_code = args[2] if len(args) > 2 else kwargs.get("status_code", 200)
      headers = args[2] if len(args) > 2 else kwargs.get("headers")
      media_type = args[3] if len(args) > 3 else kwargs.get("media_type")
      background = args[4] if len(args) > 4 else kwargs.get("background")
      if "request" not in context:
        raise ValueError('context must include a "request" key')
      request = context["request"]
    else: # the first argument is a request instance (new style)
      request = args[0]
      name = args[1] if len(args) > 1 else kwargs["name"]
      context = args[2] if len(args) > 2 else kwargs.get("context", {})
      status_code = args[3] if len(args) > 3 else kwargs.get("status_code", 200)
      headers = args[4] if len(args) > 4 else kwargs.get("headers")
      media_type = args[5] if len(args) > 5 else kwargs.get("media_type")
      background = args[6] if len(args) > 6 else kwargs.get("background")
  else: # all arguments are kwargs
    if "request" not in kwargs:
      warnings.warn(
        "The `TemplateResponse` now requires the `request` argument.\n"
        'Replace `TemplateResponse(name, {"context": context})` by `TemplateResponse(request, name)`.',
        DeprecationWarning,
      )
      if "request" not in kwargs.get("context", {}):
        raise ValueError('context must include a "request" key')
    context = kwargs.get("context", {})
    request = kwargs.get("request", context.get("request"))
    name = typing.cast(str, kwargs["name"])
    status_code = kwargs.get("status_code", 200)
    headers = kwargs.get("headers")
    media_type = kwargs.get("media_type")
    background = kwargs.get("background")
  context.setdefault("request", request)
  for context_processor in self.context_processors:
    context.update(context_processor(request))
  template = self.get_template(name)
  return _TemplateResponse(
    template,
    context,
    status_code=status_code,
    headers=headers,
    media_type=media_type,
    background=background,
  )

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
