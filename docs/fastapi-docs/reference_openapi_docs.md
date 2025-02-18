Skip to content 
# OpenAPI `docs`¶
Utilities to handle OpenAPI automatic UI documentation, including Swagger UI (by default at `/docs`) and ReDoc (by default at `/redoc`).
##  fastapi.openapi.docs.get_swagger_ui_html ¶
```
get_swagger_ui_html(
  *,
  openapi_url,
  title,
  swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
  swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
  swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
  oauth2_redirect_url=None,
  init_oauth=None,
  swagger_ui_parameters=None
)

```

Generate and return the HTML that loads Swagger UI for the interactive API docs (normally served at `/docs`).
You would only call this function yourself if you needed to override some parts, for example the URLs to use to load Swagger UI's JavaScript and CSS.
Read more about it in the FastAPI docs for Configure Swagger UI and the FastAPI docs for Custom Docs UI Static Assets (Self-Hosting).
PARAMETER | DESCRIPTION  
---|---  
`openapi_url` |  The OpenAPI URL that Swagger UI should load and use. This is normally done automatically by FastAPI using the default URL `/openapi.json`. **TYPE:** `str`  
`title` |  The HTML `<title>` content, normally shown in the browser tab. **TYPE:** `str`  
`swagger_js_url` |  The URL to use to load the Swagger UI JavaScript. It is normally set to a CDN URL. **TYPE:** `str` **DEFAULT:** `'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js'`  
`swagger_css_url` |  The URL to use to load the Swagger UI CSS. It is normally set to a CDN URL. **TYPE:** `str` **DEFAULT:** `'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css'`  
`swagger_favicon_url` |  The URL of the favicon to use. It is normally shown in the browser tab. **TYPE:** `str` **DEFAULT:** `'https://fastapi.tiangolo.com/img/favicon.png'`  
`oauth2_redirect_url` |  The OAuth2 redirect URL, it is normally automatically handled by FastAPI. **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`init_oauth` |  A dictionary with Swagger UI OAuth2 initialization configurations. **TYPE:** `Optional[Dict[str, Any]]` **DEFAULT:** `None`  
`swagger_ui_parameters` |  Configuration parameters for Swagger UI. It defaults to swagger_ui_default_parameters. **TYPE:** `Optional[Dict[str, Any]]` **DEFAULT:** `None`  
Source code in `fastapi/openapi/docs.py`
```
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
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
 57
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
105
106
107
108
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
150
151
152
153
154
155
156
157
158
```
| ```
defget_swagger_ui_html(
  *,
  openapi_url: Annotated[
    str,
    Doc(
"""
      The OpenAPI URL that Swagger UI should load and use.
      This is normally done automatically by FastAPI using the default URL
      `/openapi.json`.
      """
    ),
  ],
  title: Annotated[
    str,
    Doc(
"""
      The HTML `<title>` content, normally shown in the browser tab.
      """
    ),
  ],
  swagger_js_url: Annotated[
    str,
    Doc(
"""
      The URL to use to load the Swagger UI JavaScript.
      It is normally set to a CDN URL.
      """
    ),
  ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
  swagger_css_url: Annotated[
    str,
    Doc(
"""
      The URL to use to load the Swagger UI CSS.
      It is normally set to a CDN URL.
      """
    ),
  ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
  swagger_favicon_url: Annotated[
    str,
    Doc(
"""
      The URL of the favicon to use. It is normally shown in the browser tab.
      """
    ),
  ] = "https://fastapi.tiangolo.com/img/favicon.png",
  oauth2_redirect_url: Annotated[
    Optional[str],
    Doc(
"""
      The OAuth2 redirect URL, it is normally automatically handled by FastAPI.
      """
    ),
  ] = None,
  init_oauth: Annotated[
    Optional[Dict[str, Any]],
    Doc(
"""
      A dictionary with Swagger UI OAuth2 initialization configurations.
      """
    ),
  ] = None,
  swagger_ui_parameters: Annotated[
    Optional[Dict[str, Any]],
    Doc(
"""
      Configuration parameters for Swagger UI.
      It defaults to [swagger_ui_default_parameters][fastapi.openapi.docs.swagger_ui_default_parameters].
      """
    ),
  ] = None,
) -> HTMLResponse:
"""
  Generate and return the HTML that loads Swagger UI for the interactive
  API docs (normally served at `/docs`).
  You would only call this function yourself if you needed to override some parts,
  for example the URLs to use to load Swagger UI's JavaScript and CSS.
  Read more about it in the
  [FastAPI docs for Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
  and the [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).
  """
  current_swagger_ui_parameters = swagger_ui_default_parameters.copy()
  if swagger_ui_parameters:
    current_swagger_ui_parameters.update(swagger_ui_parameters)
  html = f"""
  <!DOCTYPE html>
  <html>
  <head>
  <link type="text/css" rel="stylesheet" href="{swagger_css_url}">
  <link rel="shortcut icon" href="{swagger_favicon_url}">
  <title>{title}</title>
  </head>
  <body>
  <div id="swagger-ui">
  </div>
  <script src="{swagger_js_url}"></script>
  <!-- `SwaggerUIBundle` is now available on the page -->
  <script>
  const ui = SwaggerUIBundle({{
    url: '{openapi_url}',
  """
  for key, value in current_swagger_ui_parameters.items():
    html += f"{json.dumps(key)}: {json.dumps(jsonable_encoder(value))},\n"
  if oauth2_redirect_url:
    html += f"oauth2RedirectUrl: window.location.origin + '{oauth2_redirect_url}',"
  html += """
  presets: [
    SwaggerUIBundle.presets.apis,
    SwaggerUIBundle.SwaggerUIStandalonePreset
    ],
  })"""
  if init_oauth:
    html += f"""
    ui.initOAuth({json.dumps(jsonable_encoder(init_oauth))})
    """
  html += """
  </script>
  </body>
  </html>
  """
  return HTMLResponse(html)

```
  
---|---  
##  fastapi.openapi.docs.get_redoc_html ¶
```
get_redoc_html(
  *,
  openapi_url,
  title,
  redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
  redoc_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
  with_google_fonts=True
)

```

Generate and return the HTML response that loads ReDoc for the alternative API docs (normally served at `/redoc`).
You would only call this function yourself if you needed to override some parts, for example the URLs to use to load ReDoc's JavaScript and CSS.
Read more about it in the FastAPI docs for Custom Docs UI Static Assets (Self-Hosting).
PARAMETER | DESCRIPTION  
---|---  
`openapi_url` |  The OpenAPI URL that ReDoc should load and use. This is normally done automatically by FastAPI using the default URL `/openapi.json`. **TYPE:** `str`  
`title` |  The HTML `<title>` content, normally shown in the browser tab. **TYPE:** `str`  
`redoc_js_url` |  The URL to use to load the ReDoc JavaScript. It is normally set to a CDN URL. **TYPE:** `str` **DEFAULT:** `'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'`  
`redoc_favicon_url` |  The URL of the favicon to use. It is normally shown in the browser tab. **TYPE:** `str` **DEFAULT:** `'https://fastapi.tiangolo.com/img/favicon.png'`  
`with_google_fonts` |  Load and use Google Fonts. **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/openapi/docs.py`
```
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
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
```
| ```
defget_redoc_html(
  *,
  openapi_url: Annotated[
    str,
    Doc(
"""
      The OpenAPI URL that ReDoc should load and use.
      This is normally done automatically by FastAPI using the default URL
      `/openapi.json`.
      """
    ),
  ],
  title: Annotated[
    str,
    Doc(
"""
      The HTML `<title>` content, normally shown in the browser tab.
      """
    ),
  ],
  redoc_js_url: Annotated[
    str,
    Doc(
"""
      The URL to use to load the ReDoc JavaScript.
      It is normally set to a CDN URL.
      """
    ),
  ] = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
  redoc_favicon_url: Annotated[
    str,
    Doc(
"""
      The URL of the favicon to use. It is normally shown in the browser tab.
      """
    ),
  ] = "https://fastapi.tiangolo.com/img/favicon.png",
  with_google_fonts: Annotated[
    bool,
    Doc(
"""
      Load and use Google Fonts.
      """
    ),
  ] = True,
) -> HTMLResponse:
"""
  Generate and return the HTML response that loads ReDoc for the alternative
  API docs (normally served at `/redoc`).
  You would only call this function yourself if you needed to override some parts,
  for example the URLs to use to load ReDoc's JavaScript and CSS.
  Read more about it in the
  [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).
  """
  html = f"""
  <!DOCTYPE html>
  <html>
  <head>
  <title>{title}</title>
  <!-- needed for adaptive design -->
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  """
  if with_google_fonts:
    html += """
  <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
  """
  html += f"""
  <link rel="shortcut icon" href="{redoc_favicon_url}">
  <!--
  ReDoc doesn't change outer page styles
  -->
  <style>
   body {{
    margin: 0;
    padding: 0;
}}
  </style>
  </head>
  <body>
  <noscript>
    ReDoc requires Javascript to function. Please enable it to browse the documentation.
  </noscript>
  <redoc spec-url="{openapi_url}"></redoc>
  <script src="{redoc_js_url}"> </script>
  </body>
  </html>
  """
  return HTMLResponse(html)

```
  
---|---  
##  fastapi.openapi.docs.get_swagger_ui_oauth2_redirect_html ¶
```
get_swagger_ui_oauth2_redirect_html()

```

Generate the HTML response with the OAuth2 redirection for Swagger UI.
You normally don't need to use or change this.
Source code in `fastapi/openapi/docs.py`
```
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
```
| ```
defget_swagger_ui_oauth2_redirect_html() -> HTMLResponse:
"""
  Generate the HTML response with the OAuth2 redirection for Swagger UI.
  You normally don't need to use or change this.
  """
  # copied from https://github.com/swagger-api/swagger-ui/blob/v4.14.0/dist/oauth2-redirect.html
  html = """
  <!doctype html>
  <html lang="en-US">
  <head>
    <title>Swagger UI: OAuth2 Redirect</title>
  </head>
  <body>
  <script>
    'use strict';
    function run () {
      var oauth2 = window.opener.swaggerUIRedirectOauth2;
      var sentState = oauth2.state;
      var redirectUrl = oauth2.redirectUrl;
      var isValid, qp, arr;
      if (/code|token|error/.test(window.location.hash)) {
        qp = window.location.hash.substring(1).replace('?', '&');
      } else {
        qp = location.search.substring(1);
      }
      arr = qp.split("&");
      arr.forEach(function (v,i,_arr) { _arr[i] = '"' + v.replace('=', '":"') + '"';});
      qp = qp ? JSON.parse('{' + arr.join() + '}',
          function (key, value) {
            return key === "" ? value : decodeURIComponent(value);
          }
      ) : {};
      isValid = qp.state === sentState;
      if ((
       oauth2.auth.schema.get("flow") === "accessCode" ||
       oauth2.auth.schema.get("flow") === "authorizationCode" ||
       oauth2.auth.schema.get("flow") === "authorization_code"
      ) && !oauth2.auth.code) {
        if (!isValid) {
          oauth2.errCb({
            authId: oauth2.auth.name,
            source: "auth",
            level: "warning",
            message: "Authorization may be unsafe, passed state was changed in server. The passed state wasn't returned from auth server."
          });
        }
        if (qp.code) {
          delete oauth2.state;
          oauth2.auth.code = qp.code;
          oauth2.callback({auth: oauth2.auth, redirectUrl: redirectUrl});
        } else {
          let oauthErrorMsg;
          if (qp.error) {
            oauthErrorMsg = "["+qp.error+"]: " +
              (qp.error_description ? qp.error_description+ ". " : "no accessCode received from the server. ") +
              (qp.error_uri ? "More info: "+qp.error_uri : "");
          }
          oauth2.errCb({
            authId: oauth2.auth.name,
            source: "auth",
            level: "error",
            message: oauthErrorMsg || "[Authorization failed]: no accessCode received from the server."
          });
        }
      } else {
        oauth2.callback({auth: oauth2.auth, token: qp, isValid: isValid, redirectUrl: redirectUrl});
      }
      window.close();
    }
    if (document.readyState !== 'loading') {
      run();
    } else {
      document.addEventListener('DOMContentLoaded', function () {
        run();
      });
    }
  </script>
  </body>
  </html>
    """
  return HTMLResponse(content=html)

```
  
---|---  
##  fastapi.openapi.docs.swagger_ui_default_parameters `module-attribute` ¶
```
swagger_ui_default_parameters = {
  "dom_id": "#swagger-ui",
  "layout": "BaseLayout",
  "deepLinking": True,
  "showExtensions": True,
  "showCommonExtensions": True,
}

```

Default configurations for Swagger UI.
You can use it as a template to add any other configurations needed.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
