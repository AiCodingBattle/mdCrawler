Skip to content 
# Encoders - `jsonable_encoder`¶
##  fastapi.encoders.jsonable_encoder ¶
```
jsonable_encoder(
  obj,
  include=None,
  exclude=None,
  by_alias=True,
  exclude_unset=False,
  exclude_defaults=False,
  exclude_none=False,
  custom_encoder=None,
  sqlalchemy_safe=True,
)

```

Convert any object to something that can be encoded in JSON.
This is used internally by FastAPI to make sure anything you return can be encoded as JSON before it is sent to the client.
You can also use it yourself, for example to convert objects before saving them in a database that supports only JSON.
Read more about it in the FastAPI docs for JSON Compatible Encoder.
PARAMETER | DESCRIPTION  
---|---  
`obj` |  The input object to convert to JSON. **TYPE:** `Any`  
`include` |  Pydantic's `include` parameter, passed to Pydantic models to set the fields to include. **TYPE:** `Optional[IncEx]` **DEFAULT:** `None`  
`exclude` |  Pydantic's `exclude` parameter, passed to Pydantic models to set the fields to exclude. **TYPE:** `Optional[IncEx]` **DEFAULT:** `None`  
`by_alias` |  Pydantic's `by_alias` parameter, passed to Pydantic models to define if the output should use the alias names (when provided) or the Python attribute names. In an API, if you set an alias, it's probably because you want to use it in the result, so you probably want to leave this set to `True`. **TYPE:** `bool` **DEFAULT:** `True`  
`exclude_unset` |  Pydantic's `exclude_unset` parameter, passed to Pydantic models to define if it should exclude from the output the fields that were not explicitly set (and that only had their default values). **TYPE:** `bool` **DEFAULT:** `False`  
`exclude_defaults` |  Pydantic's `exclude_defaults` parameter, passed to Pydantic models to define if it should exclude from the output the fields that had the same default value, even when they were explicitly set. **TYPE:** `bool` **DEFAULT:** `False`  
`exclude_none` |  Pydantic's `exclude_none` parameter, passed to Pydantic models to define if it should exclude from the output any fields that have a `None` value. **TYPE:** `bool` **DEFAULT:** `False`  
`custom_encoder` |  Pydantic's `custom_encoder` parameter, passed to Pydantic models to define a custom encoder. **TYPE:** `Optional[Dict[Any, Callable[[Any], Any]]]` **DEFAULT:** `None`  
`sqlalchemy_safe` |  Exclude from the output any fields that start with the name `_sa`. This is mainly a hack for compatibility with SQLAlchemy objects, they store internal SQLAlchemy-specific state in attributes named with `_sa`, and those objects can't (and shouldn't be) serialized to JSON. **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/encoders.py`
```
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
254
255
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
```
| ```
defjsonable_encoder(
  obj: Annotated[
    Any,
    Doc(
"""
      The input object to convert to JSON.
      """
    ),
  ],
  include: Annotated[
    Optional[IncEx],
    Doc(
"""
      Pydantic's `include` parameter, passed to Pydantic models to set the
      fields to include.
      """
    ),
  ] = None,
  exclude: Annotated[
    Optional[IncEx],
    Doc(
"""
      Pydantic's `exclude` parameter, passed to Pydantic models to set the
      fields to exclude.
      """
    ),
  ] = None,
  by_alias: Annotated[
    bool,
    Doc(
"""
      Pydantic's `by_alias` parameter, passed to Pydantic models to define if
      the output should use the alias names (when provided) or the Python
      attribute names. In an API, if you set an alias, it's probably because you
      want to use it in the result, so you probably want to leave this set to
      `True`.
      """
    ),
  ] = True,
  exclude_unset: Annotated[
    bool,
    Doc(
"""
      Pydantic's `exclude_unset` parameter, passed to Pydantic models to define
      if it should exclude from the output the fields that were not explicitly
      set (and that only had their default values).
      """
    ),
  ] = False,
  exclude_defaults: Annotated[
    bool,
    Doc(
"""
      Pydantic's `exclude_defaults` parameter, passed to Pydantic models to define
      if it should exclude from the output the fields that had the same default
      value, even when they were explicitly set.
      """
    ),
  ] = False,
  exclude_none: Annotated[
    bool,
    Doc(
"""
      Pydantic's `exclude_none` parameter, passed to Pydantic models to define
      if it should exclude from the output any fields that have a `None` value.
      """
    ),
  ] = False,
  custom_encoder: Annotated[
    Optional[Dict[Any, Callable[[Any], Any]]],
    Doc(
"""
      Pydantic's `custom_encoder` parameter, passed to Pydantic models to define
      a custom encoder.
      """
    ),
  ] = None,
  sqlalchemy_safe: Annotated[
    bool,
    Doc(
"""
      Exclude from the output any fields that start with the name `_sa`.
      This is mainly a hack for compatibility with SQLAlchemy objects, they
      store internal SQLAlchemy-specific state in attributes named with `_sa`,
      and those objects can't (and shouldn't be) serialized to JSON.
      """
    ),
  ] = True,
) -> Any:
"""
  Convert any object to something that can be encoded in JSON.
  This is used internally by FastAPI to make sure anything you return can be
  encoded as JSON before it is sent to the client.
  You can also use it yourself, for example to convert objects before saving them
  in a database that supports only JSON.
  Read more about it in the
  [FastAPI docs for JSON Compatible Encoder](https://fastapi.tiangolo.com/tutorial/encoder/).
  """
  custom_encoder = custom_encoder or {}
  if custom_encoder:
    if type(obj) in custom_encoder:
      return custom_encoder[type(obj)](obj)
    else:
      for encoder_type, encoder_instance in custom_encoder.items():
        if isinstance(obj, encoder_type):
          return encoder_instance(obj)
  if include is not None and not isinstance(include, (set, dict)):
    include = set(include)
  if exclude is not None and not isinstance(exclude, (set, dict)):
    exclude = set(exclude)
  if isinstance(obj, BaseModel):
    # TODO: remove when deprecating Pydantic v1
    encoders: Dict[Any, Any] = {}
    if not PYDANTIC_V2:
      encoders = getattr(obj.__config__, "json_encoders", {}) # type: ignore[attr-defined]
      if custom_encoder:
        encoders.update(custom_encoder)
    obj_dict = _model_dump(
      obj,
      mode="json",
      include=include,
      exclude=exclude,
      by_alias=by_alias,
      exclude_unset=exclude_unset,
      exclude_none=exclude_none,
      exclude_defaults=exclude_defaults,
    )
    if "__root__" in obj_dict:
      obj_dict = obj_dict["__root__"]
    return jsonable_encoder(
      obj_dict,
      exclude_none=exclude_none,
      exclude_defaults=exclude_defaults,
      # TODO: remove when deprecating Pydantic v1
      custom_encoder=encoders,
      sqlalchemy_safe=sqlalchemy_safe,
    )
  if dataclasses.is_dataclass(obj):
    obj_dict = dataclasses.asdict(obj)
    return jsonable_encoder(
      obj_dict,
      include=include,
      exclude=exclude,
      by_alias=by_alias,
      exclude_unset=exclude_unset,
      exclude_defaults=exclude_defaults,
      exclude_none=exclude_none,
      custom_encoder=custom_encoder,
      sqlalchemy_safe=sqlalchemy_safe,
    )
  if isinstance(obj, Enum):
    return obj.value
  if isinstance(obj, PurePath):
    return str(obj)
  if isinstance(obj, (str, int, float, type(None))):
    return obj
  if isinstance(obj, UndefinedType):
    return None
  if isinstance(obj, dict):
    encoded_dict = {}
    allowed_keys = set(obj.keys())
    if include is not None:
      allowed_keys &= set(include)
    if exclude is not None:
      allowed_keys -= set(exclude)
    for key, value in obj.items():
      if (
        (
          not sqlalchemy_safe
          or (not isinstance(key, str))
          or (not key.startswith("_sa"))
        )
        and (value is not None or not exclude_none)
        and key in allowed_keys
      ):
        encoded_key = jsonable_encoder(
          key,
          by_alias=by_alias,
          exclude_unset=exclude_unset,
          exclude_none=exclude_none,
          custom_encoder=custom_encoder,
          sqlalchemy_safe=sqlalchemy_safe,
        )
        encoded_value = jsonable_encoder(
          value,
          by_alias=by_alias,
          exclude_unset=exclude_unset,
          exclude_none=exclude_none,
          custom_encoder=custom_encoder,
          sqlalchemy_safe=sqlalchemy_safe,
        )
        encoded_dict[encoded_key] = encoded_value
    return encoded_dict
  if isinstance(obj, (list, set, frozenset, GeneratorType, tuple, deque)):
    encoded_list = []
    for item in obj:
      encoded_list.append(
        jsonable_encoder(
          item,
          include=include,
          exclude=exclude,
          by_alias=by_alias,
          exclude_unset=exclude_unset,
          exclude_defaults=exclude_defaults,
          exclude_none=exclude_none,
          custom_encoder=custom_encoder,
          sqlalchemy_safe=sqlalchemy_safe,
        )
      )
    return encoded_list
  if type(obj) in ENCODERS_BY_TYPE:
    return ENCODERS_BY_TYPE[type(obj)](obj)
  for encoder, classes_tuple in encoders_by_class_tuples.items():
    if isinstance(obj, classes_tuple):
      return encoder(obj)
  try:
    data = dict(obj)
  except Exception as e:
    errors: List[Exception] = []
    errors.append(e)
    try:
      data = vars(obj)
    except Exception as e:
      errors.append(e)
      raise ValueError(errors) frome
  return jsonable_encoder(
    data,
    include=include,
    exclude=exclude,
    by_alias=by_alias,
    exclude_unset=exclude_unset,
    exclude_defaults=exclude_defaults,
    exclude_none=exclude_none,
    custom_encoder=custom_encoder,
    sqlalchemy_safe=sqlalchemy_safe,
  )

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
