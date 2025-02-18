Skip to content 
# Static Files - `StaticFiles`¶
You can use the `StaticFiles` class to serve static files, like JavaScript, CSS, images, etc.
Read more about it in the FastAPI docs for Static Files.
You can import it directly from `fastapi.staticfiles`:
```
fromfastapi.staticfilesimport StaticFiles

```

##  fastapi.staticfiles.StaticFiles ¶
```
StaticFiles(
  *,
  directory=None,
  packages=None,
  html=False,
  check_dir=True,
  follow_symlink=False
)

```

PARAMETER | DESCRIPTION  
---|---  
`directory` |  **TYPE:** `PathLike | None` **DEFAULT:** `None`  
`packages` |  **TYPE:** `list[str | tuple[str, str]] | None` **DEFAULT:** `None`  
`html` |  **TYPE:** `bool` **DEFAULT:** `False`  
`check_dir` |  **TYPE:** `bool` **DEFAULT:** `True`  
`follow_symlink` |  **TYPE:** `bool` **DEFAULT:** `False`  
Source code in `starlette/staticfiles.py`
```
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
```
| ```
def__init__(
  self,
  *,
  directory: PathLike | None = None,
  packages: list[str | tuple[str, str]] | None = None,
  html: bool = False,
  check_dir: bool = True,
  follow_symlink: bool = False,
) -> None:
  self.directory = directory
  self.packages = packages
  self.all_directories = self.get_directories(directory, packages)
  self.html = html
  self.config_checked = False
  self.follow_symlink = follow_symlink
  if check_dir and directory is not None and not os.path.isdir(directory):
    raise RuntimeError(f"Directory '{directory}' does not exist")

```
  
---|---  
###  directory `instance-attribute` ¶
```
directory = directory

```

###  packages `instance-attribute` ¶
```
packages = packages

```

###  all_directories `instance-attribute` ¶
```
all_directories = get_directories(directory, packages)

```

###  html `instance-attribute` ¶
```
html = html

```

###  config_checked `instance-attribute` ¶
```
config_checked = False

```

###  follow_symlink `instance-attribute` ¶
```
follow_symlink = follow_symlink

```

###  get_directories ¶
```
get_directories(directory=None, packages=None)

```

Given `directory` and `packages` arguments, return a list of all the directories that should be used for serving static files from.
PARAMETER | DESCRIPTION  
---|---  
`directory` |  **TYPE:** `PathLike | None` **DEFAULT:** `None`  
`packages` |  **TYPE:** `list[str | tuple[str, str]] | None` **DEFAULT:** `None`  
Source code in `starlette/staticfiles.py`
```
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
```
| ```
defget_directories(
  self,
  directory: PathLike | None = None,
  packages: list[str | tuple[str, str]] | None = None,
) -> list[PathLike]:
"""
  Given `directory` and `packages` arguments, return a list of all the
  directories that should be used for serving static files from.
  """
  directories = []
  if directory is not None:
    directories.append(directory)
  for package in packages or []:
    if isinstance(package, tuple):
      package, statics_dir = package
    else:
      statics_dir = "statics"
    spec = importlib.util.find_spec(package)
    assert spec is not None, f"Package {package!r} could not be found."
    assert spec.origin is not None, f"Package {package!r} could not be found."
    package_directory = os.path.normpath(os.path.join(spec.origin, "..", statics_dir))
    assert os.path.isdir(
      package_directory
    ), f"Directory '{statics_dir!r}' in package {package!r} could not be found."
    directories.append(package_directory)
  return directories

```
  
---|---  
###  get_path ¶
```
get_path(scope)

```

Given the ASGI scope, return the `path` string to serve up, with OS specific path separators, and any '..', '.' components removed.
PARAMETER | DESCRIPTION  
---|---  
`scope` |  **TYPE:** `Scope`  
Source code in `starlette/staticfiles.py`
```
101
102
103
104
105
106
107
```
| ```
defget_path(self, scope: Scope) -> str:
"""
  Given the ASGI scope, return the `path` string to serve up,
  with OS specific path separators, and any '..', '.' components removed.
  """
  route_path = get_route_path(scope)
  return os.path.normpath(os.path.join(*route_path.split("/")))

```
  
---|---  
###  get_response `async` ¶
```
get_response(path, scope)

```

Returns an HTTP response, given the incoming path, method and request headers.
PARAMETER | DESCRIPTION  
---|---  
`path` |  **TYPE:** `str`  
`scope` |  **TYPE:** `Scope`  
Source code in `starlette/staticfiles.py`
```
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
```
| ```
async defget_response(self, path: str, scope: Scope) -> Response:
"""
  Returns an HTTP response, given the incoming path, method and request headers.
  """
  if scope["method"] not in ("GET", "HEAD"):
    raise HTTPException(status_code=405)
  try:
    full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, path)
  except PermissionError:
    raise HTTPException(status_code=401)
  except OSError as exc:
    # Filename is too long, so it can't be a valid static file.
    if exc.errno == errno.ENAMETOOLONG:
      raise HTTPException(status_code=404)
    raise exc
  if stat_result and stat.S_ISREG(stat_result.st_mode):
    # We have a static file to serve.
    return self.file_response(full_path, stat_result, scope)
  elif stat_result and stat.S_ISDIR(stat_result.st_mode) and self.html:
    # We're in HTML mode, and have got a directory URL.
    # Check if we have 'index.html' file to serve.
    index_path = os.path.join(path, "index.html")
    full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, index_path)
    if stat_result is not None and stat.S_ISREG(stat_result.st_mode):
      if not scope["path"].endswith("/"):
        # Directory URLs should redirect to always end in "/".
        url = URL(scope=scope)
        url = url.replace(path=url.path + "/")
        return RedirectResponse(url=url)
      return self.file_response(full_path, stat_result, scope)
  if self.html:
    # Check for '404.html' if we're in HTML mode.
    full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, "404.html")
    if stat_result and stat.S_ISREG(stat_result.st_mode):
      return FileResponse(full_path, stat_result=stat_result, status_code=404)
  raise HTTPException(status_code=404)

```
  
---|---  
###  lookup_path ¶
```
lookup_path(path)

```

PARAMETER | DESCRIPTION  
---|---  
`path` |  **TYPE:** `str`  
Source code in `starlette/staticfiles.py`
```
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
```
| ```
deflookup_path(self, path: str) -> tuple[str, os.stat_result | None]:
  for directory in self.all_directories:
    joined_path = os.path.join(directory, path)
    if self.follow_symlink:
      full_path = os.path.abspath(joined_path)
    else:
      full_path = os.path.realpath(joined_path)
      directory = os.path.realpath(directory)
    if os.path.commonpath([full_path, directory]) != str(directory):
      # Don't allow misbehaving clients to break out of the static files directory.
      continue
    try:
      return full_path, os.stat(full_path)
    except (FileNotFoundError, NotADirectoryError):
      continue
  return "", None

```
  
---|---  
###  file_response ¶
```
file_response(
  full_path, stat_result, scope, status_code=200
)

```

PARAMETER | DESCRIPTION  
---|---  
`full_path` |  **TYPE:** `PathLike`  
`stat_result` |  **TYPE:** `stat_result`  
`scope` |  **TYPE:** `Scope`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
Source code in `starlette/staticfiles.py`
```
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
```
| ```
deffile_response(
  self,
  full_path: PathLike,
  stat_result: os.stat_result,
  scope: Scope,
  status_code: int = 200,
) -> Response:
  request_headers = Headers(scope=scope)
  response = FileResponse(full_path, status_code=status_code, stat_result=stat_result)
  if self.is_not_modified(response.headers, request_headers):
    return NotModifiedResponse(response.headers)
  return response

```
  
---|---  
###  check_config `async` ¶
```
check_config()

```

Perform a one-off configuration check that StaticFiles is actually pointed at a directory, so that we can raise loud errors rather than just returning 404 responses.
Source code in `starlette/staticfiles.py`
```
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
```
| ```
async defcheck_config(self) -> None:
"""
  Perform a one-off configuration check that StaticFiles is actually
  pointed at a directory, so that we can raise loud errors rather than
  just returning 404 responses.
  """
  if self.directory is None:
    return
  try:
    stat_result = await anyio.to_thread.run_sync(os.stat, self.directory)
  except FileNotFoundError:
    raise RuntimeError(f"StaticFiles directory '{self.directory}' does not exist.")
  if not (stat.S_ISDIR(stat_result.st_mode) or stat.S_ISLNK(stat_result.st_mode)):
    raise RuntimeError(f"StaticFiles path '{self.directory}' is not a directory.")

```
  
---|---  
###  is_not_modified ¶
```
is_not_modified(response_headers, request_headers)

```

Given the request and response headers, return `True` if an HTTP "Not Modified" response could be returned instead.
PARAMETER | DESCRIPTION  
---|---  
`response_headers` |  **TYPE:** `Headers`  
`request_headers` |  **TYPE:** `Headers`  
Source code in `starlette/staticfiles.py`
```
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
217
218
219
```
| ```
defis_not_modified(self, response_headers: Headers, request_headers: Headers) -> bool:
"""
  Given the request and response headers, return `True` if an HTTP
  "Not Modified" response could be returned instead.
  """
  try:
    if_none_match = request_headers["if-none-match"]
    etag = response_headers["etag"]
    if etag in [tag.strip(" W/") for tag in if_none_match.split(",")]:
      return True
  except KeyError:
    pass
  try:
    if_modified_since = parsedate(request_headers["if-modified-since"])
    last_modified = parsedate(response_headers["last-modified"])
    if if_modified_since is not None and last_modified is not None and if_modified_since >= last_modified:
      return True
  except KeyError:
    pass
  return False

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
