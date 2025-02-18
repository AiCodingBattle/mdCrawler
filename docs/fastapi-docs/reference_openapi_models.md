Skip to content 
# OpenAPI `models`¶
OpenAPI Pydantic models used to generate and validate the generated OpenAPI.
##  fastapi.openapi.models ¶
###  SchemaOrBool `module-attribute` ¶
```
SchemaOrBool = Union[Schema, bool]

```

###  SecurityScheme `module-attribute` ¶
```
SecurityScheme = Union[
  APIKey, HTTPBase, OAuth2, OpenIdConnect, HTTPBearer
]

```

###  BaseModelWithConfig ¶
Bases: `BaseModel`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Contact ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  name `class-attribute` `instance-attribute` ¶
```
name = None

```

####  url `class-attribute` `instance-attribute` ¶
```
url = None

```

####  email `class-attribute` `instance-attribute` ¶
```
email = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  License ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  name `instance-attribute` ¶
```
name

```

####  identifier `class-attribute` `instance-attribute` ¶
```
identifier = None

```

####  url `class-attribute` `instance-attribute` ¶
```
url = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Info ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  title `instance-attribute` ¶
```
title

```

####  summary `class-attribute` `instance-attribute` ¶
```
summary = None

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  termsOfService `class-attribute` `instance-attribute` ¶
```
termsOfService = None

```

####  contact `class-attribute` `instance-attribute` ¶
```
contact = None

```

####  license `class-attribute` `instance-attribute` ¶
```
license = None

```

####  version `instance-attribute` ¶
```
version

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  ServerVariable ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  enum `class-attribute` `instance-attribute` ¶
```
enum = None

```

####  default `instance-attribute` ¶
```
default

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Server ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  url `instance-attribute` ¶
```
url

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  variables `class-attribute` `instance-attribute` ¶
```
variables = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Reference ¶
Bases: `BaseModel`
####  ref `class-attribute` `instance-attribute` ¶
```
ref = Field(alias='$ref')

```

###  Discriminator ¶
Bases: `BaseModel`
####  propertyName `instance-attribute` ¶
```
propertyName

```

####  mapping `class-attribute` `instance-attribute` ¶
```
mapping = None

```

###  XML ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  name `class-attribute` `instance-attribute` ¶
```
name = None

```

####  namespace `class-attribute` `instance-attribute` ¶
```
namespace = None

```

####  prefix `class-attribute` `instance-attribute` ¶
```
prefix = None

```

####  attribute `class-attribute` `instance-attribute` ¶
```
attribute = None

```

####  wrapped `class-attribute` `instance-attribute` ¶
```
wrapped = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  ExternalDocumentation ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  url `instance-attribute` ¶
```
url

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Schema ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  schema_ `class-attribute` `instance-attribute` ¶
```
schema_ = Field(default=None, alias='$schema')

```

####  vocabulary `class-attribute` `instance-attribute` ¶
```
vocabulary = Field(default=None, alias='$vocabulary')

```

####  id `class-attribute` `instance-attribute` ¶
```
id = Field(default=None, alias='$id')

```

####  anchor `class-attribute` `instance-attribute` ¶
```
anchor = Field(default=None, alias='$anchor')

```

####  dynamicAnchor `class-attribute` `instance-attribute` ¶
```
dynamicAnchor = Field(default=None, alias='$dynamicAnchor')

```

####  ref `class-attribute` `instance-attribute` ¶
```
ref = Field(default=None, alias='$ref')

```

####  dynamicRef `class-attribute` `instance-attribute` ¶
```
dynamicRef = Field(default=None, alias='$dynamicRef')

```

####  defs `class-attribute` `instance-attribute` ¶
```
defs = Field(default=None, alias='$defs')

```

####  comment `class-attribute` `instance-attribute` ¶
```
comment = Field(default=None, alias='$comment')

```

####  allOf `class-attribute` `instance-attribute` ¶
```
allOf = None

```

####  anyOf `class-attribute` `instance-attribute` ¶
```
anyOf = None

```

####  oneOf `class-attribute` `instance-attribute` ¶
```
oneOf = None

```

####  not_ `class-attribute` `instance-attribute` ¶
```
not_ = Field(default=None, alias='not')

```

####  if_ `class-attribute` `instance-attribute` ¶
```
if_ = Field(default=None, alias='if')

```

####  then `class-attribute` `instance-attribute` ¶
```
then = None

```

####  else_ `class-attribute` `instance-attribute` ¶
```
else_ = Field(default=None, alias='else')

```

####  dependentSchemas `class-attribute` `instance-attribute` ¶
```
dependentSchemas = None

```

####  prefixItems `class-attribute` `instance-attribute` ¶
```
prefixItems = None

```

####  items `class-attribute` `instance-attribute` ¶
```
items = None

```

####  contains `class-attribute` `instance-attribute` ¶
```
contains = None

```

####  properties `class-attribute` `instance-attribute` ¶
```
properties = None

```

####  patternProperties `class-attribute` `instance-attribute` ¶
```
patternProperties = None

```

####  additionalProperties `class-attribute` `instance-attribute` ¶
```
additionalProperties = None

```

####  propertyNames `class-attribute` `instance-attribute` ¶
```
propertyNames = None

```

####  unevaluatedItems `class-attribute` `instance-attribute` ¶
```
unevaluatedItems = None

```

####  unevaluatedProperties `class-attribute` `instance-attribute` ¶
```
unevaluatedProperties = None

```

####  type `class-attribute` `instance-attribute` ¶
```
type = None

```

####  enum `class-attribute` `instance-attribute` ¶
```
enum = None

```

####  const `class-attribute` `instance-attribute` ¶
```
const = None

```

####  multipleOf `class-attribute` `instance-attribute` ¶
```
multipleOf = Field(default=None, gt=0)

```

####  maximum `class-attribute` `instance-attribute` ¶
```
maximum = None

```

####  exclusiveMaximum `class-attribute` `instance-attribute` ¶
```
exclusiveMaximum = None

```

####  minimum `class-attribute` `instance-attribute` ¶
```
minimum = None

```

####  exclusiveMinimum `class-attribute` `instance-attribute` ¶
```
exclusiveMinimum = None

```

####  maxLength `class-attribute` `instance-attribute` ¶
```
maxLength = Field(default=None, ge=0)

```

####  minLength `class-attribute` `instance-attribute` ¶
```
minLength = Field(default=None, ge=0)

```

####  pattern `class-attribute` `instance-attribute` ¶
```
pattern = None

```

####  maxItems `class-attribute` `instance-attribute` ¶
```
maxItems = Field(default=None, ge=0)

```

####  minItems `class-attribute` `instance-attribute` ¶
```
minItems = Field(default=None, ge=0)

```

####  uniqueItems `class-attribute` `instance-attribute` ¶
```
uniqueItems = None

```

####  maxContains `class-attribute` `instance-attribute` ¶
```
maxContains = Field(default=None, ge=0)

```

####  minContains `class-attribute` `instance-attribute` ¶
```
minContains = Field(default=None, ge=0)

```

####  maxProperties `class-attribute` `instance-attribute` ¶
```
maxProperties = Field(default=None, ge=0)

```

####  minProperties `class-attribute` `instance-attribute` ¶
```
minProperties = Field(default=None, ge=0)

```

####  required `class-attribute` `instance-attribute` ¶
```
required = None

```

####  dependentRequired `class-attribute` `instance-attribute` ¶
```
dependentRequired = None

```

####  format `class-attribute` `instance-attribute` ¶
```
format = None

```

####  contentEncoding `class-attribute` `instance-attribute` ¶
```
contentEncoding = None

```

####  contentMediaType `class-attribute` `instance-attribute` ¶
```
contentMediaType = None

```

####  contentSchema `class-attribute` `instance-attribute` ¶
```
contentSchema = None

```

####  title `class-attribute` `instance-attribute` ¶
```
title = None

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  default `class-attribute` `instance-attribute` ¶
```
default = None

```

####  deprecated `class-attribute` `instance-attribute` ¶
```
deprecated = None

```

####  readOnly `class-attribute` `instance-attribute` ¶
```
readOnly = None

```

####  writeOnly `class-attribute` `instance-attribute` ¶
```
writeOnly = None

```

####  examples `class-attribute` `instance-attribute` ¶
```
examples = None

```

####  discriminator `class-attribute` `instance-attribute` ¶
```
discriminator = None

```

####  xml `class-attribute` `instance-attribute` ¶
```
xml = None

```

####  externalDocs `class-attribute` `instance-attribute` ¶
```
externalDocs = None

```

####  example `class-attribute` `instance-attribute` ¶
```
example = None

```

Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Example ¶
Bases: `TypedDict`
####  summary `instance-attribute` ¶
```
summary

```

####  description `instance-attribute` ¶
```
description

```

####  value `instance-attribute` ¶
```
value

```

####  externalValue `instance-attribute` ¶
```
externalValue

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  ParameterInType ¶
Bases: `Enum`
####  query `class-attribute` `instance-attribute` ¶
```
query = 'query'

```

####  header `class-attribute` `instance-attribute` ¶
```
header = 'header'

```

####  path `class-attribute` `instance-attribute` ¶
```
path = 'path'

```

####  cookie `class-attribute` `instance-attribute` ¶
```
cookie = 'cookie'

```

###  Encoding ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  contentType `class-attribute` `instance-attribute` ¶
```
contentType = None

```

####  headers `class-attribute` `instance-attribute` ¶
```
headers = None

```

####  style `class-attribute` `instance-attribute` ¶
```
style = None

```

####  explode `class-attribute` `instance-attribute` ¶
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` ¶
```
allowReserved = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  MediaType ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  schema_ `class-attribute` `instance-attribute` ¶
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` ¶
```
example = None

```

####  examples `class-attribute` `instance-attribute` ¶
```
examples = None

```

####  encoding `class-attribute` `instance-attribute` ¶
```
encoding = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  ParameterBase ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  required `class-attribute` `instance-attribute` ¶
```
required = None

```

####  deprecated `class-attribute` `instance-attribute` ¶
```
deprecated = None

```

####  style `class-attribute` `instance-attribute` ¶
```
style = None

```

####  explode `class-attribute` `instance-attribute` ¶
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` ¶
```
allowReserved = None

```

####  schema_ `class-attribute` `instance-attribute` ¶
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` ¶
```
example = None

```

####  examples `class-attribute` `instance-attribute` ¶
```
examples = None

```

####  content `class-attribute` `instance-attribute` ¶
```
content = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Parameter ¶
Bases: `ParameterBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  required `class-attribute` `instance-attribute` ¶
```
required = None

```

####  deprecated `class-attribute` `instance-attribute` ¶
```
deprecated = None

```

####  style `class-attribute` `instance-attribute` ¶
```
style = None

```

####  explode `class-attribute` `instance-attribute` ¶
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` ¶
```
allowReserved = None

```

####  schema_ `class-attribute` `instance-attribute` ¶
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` ¶
```
example = None

```

####  examples `class-attribute` `instance-attribute` ¶
```
examples = None

```

####  content `class-attribute` `instance-attribute` ¶
```
content = None

```

####  name `instance-attribute` ¶
```
name

```

####  in_ `class-attribute` `instance-attribute` ¶
```
in_ = Field(alias='in')

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Header ¶
Bases: `ParameterBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  required `class-attribute` `instance-attribute` ¶
```
required = None

```

####  deprecated `class-attribute` `instance-attribute` ¶
```
deprecated = None

```

####  style `class-attribute` `instance-attribute` ¶
```
style = None

```

####  explode `class-attribute` `instance-attribute` ¶
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` ¶
```
allowReserved = None

```

####  schema_ `class-attribute` `instance-attribute` ¶
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` ¶
```
example = None

```

####  examples `class-attribute` `instance-attribute` ¶
```
examples = None

```

####  content `class-attribute` `instance-attribute` ¶
```
content = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  RequestBody ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  content `instance-attribute` ¶
```
content

```

####  required `class-attribute` `instance-attribute` ¶
```
required = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Link ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  operationRef `class-attribute` `instance-attribute` ¶
```
operationRef = None

```

####  operationId `class-attribute` `instance-attribute` ¶
```
operationId = None

```

####  parameters `class-attribute` `instance-attribute` ¶
```
parameters = None

```

####  requestBody `class-attribute` `instance-attribute` ¶
```
requestBody = None

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  server `class-attribute` `instance-attribute` ¶
```
server = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Response ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `instance-attribute` ¶
```
description

```

####  headers `class-attribute` `instance-attribute` ¶
```
headers = None

```

####  content `class-attribute` `instance-attribute` ¶
```
content = None

```

####  links `class-attribute` `instance-attribute` ¶
```
links = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Operation ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  tags `class-attribute` `instance-attribute` ¶
```
tags = None

```

####  summary `class-attribute` `instance-attribute` ¶
```
summary = None

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  externalDocs `class-attribute` `instance-attribute` ¶
```
externalDocs = None

```

####  operationId `class-attribute` `instance-attribute` ¶
```
operationId = None

```

####  parameters `class-attribute` `instance-attribute` ¶
```
parameters = None

```

####  requestBody `class-attribute` `instance-attribute` ¶
```
requestBody = None

```

####  responses `class-attribute` `instance-attribute` ¶
```
responses = None

```

####  callbacks `class-attribute` `instance-attribute` ¶
```
callbacks = None

```

####  deprecated `class-attribute` `instance-attribute` ¶
```
deprecated = None

```

####  security `class-attribute` `instance-attribute` ¶
```
security = None

```

####  servers `class-attribute` `instance-attribute` ¶
```
servers = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  PathItem ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  ref `class-attribute` `instance-attribute` ¶
```
ref = Field(default=None, alias='$ref')

```

####  summary `class-attribute` `instance-attribute` ¶
```
summary = None

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  get `class-attribute` `instance-attribute` ¶
```
get = None

```

####  put `class-attribute` `instance-attribute` ¶
```
put = None

```

####  post `class-attribute` `instance-attribute` ¶
```
post = None

```

####  delete `class-attribute` `instance-attribute` ¶
```
delete = None

```

####  options `class-attribute` `instance-attribute` ¶
```
options = None

```

####  head `class-attribute` `instance-attribute` ¶
```
head = None

```

####  patch `class-attribute` `instance-attribute` ¶
```
patch = None

```

####  trace `class-attribute` `instance-attribute` ¶
```
trace = None

```

####  servers `class-attribute` `instance-attribute` ¶
```
servers = None

```

####  parameters `class-attribute` `instance-attribute` ¶
```
parameters = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  SecuritySchemeType ¶
Bases: `Enum`
####  apiKey `class-attribute` `instance-attribute` ¶
```
apiKey = 'apiKey'

```

####  http `class-attribute` `instance-attribute` ¶
```
http = 'http'

```

####  oauth2 `class-attribute` `instance-attribute` ¶
```
oauth2 = 'oauth2'

```

####  openIdConnect `class-attribute` `instance-attribute` ¶
```
openIdConnect = 'openIdConnect'

```

###  SecurityBase ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  type_ `class-attribute` `instance-attribute` ¶
```
type_ = Field(alias='type')

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  APIKeyIn ¶
Bases: `Enum`
####  query `class-attribute` `instance-attribute` ¶
```
query = 'query'

```

####  header `class-attribute` `instance-attribute` ¶
```
header = 'header'

```

####  cookie `class-attribute` `instance-attribute` ¶
```
cookie = 'cookie'

```

###  APIKey ¶
Bases: `SecurityBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  type_ `class-attribute` `instance-attribute` ¶
```
type_ = Field(default=apiKey, alias='type')

```

####  in_ `class-attribute` `instance-attribute` ¶
```
in_ = Field(alias='in')

```

####  name `instance-attribute` ¶
```
name

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  HTTPBase ¶
Bases: `SecurityBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  type_ `class-attribute` `instance-attribute` ¶
```
type_ = Field(default=http, alias='type')

```

####  scheme `instance-attribute` ¶
```
scheme

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  HTTPBearer ¶
Bases: `HTTPBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  type_ `class-attribute` `instance-attribute` ¶
```
type_ = Field(default=http, alias='type')

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  scheme `class-attribute` `instance-attribute` ¶
```
scheme = 'bearer'

```

####  bearerFormat `class-attribute` `instance-attribute` ¶
```
bearerFormat = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuthFlow ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` ¶
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` ¶
```
scopes = {}

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuthFlowImplicit ¶
Bases: `OAuthFlow`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` ¶
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` ¶
```
scopes = {}

```

####  authorizationUrl `instance-attribute` ¶
```
authorizationUrl

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuthFlowPassword ¶
Bases: `OAuthFlow`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` ¶
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` ¶
```
scopes = {}

```

####  tokenUrl `instance-attribute` ¶
```
tokenUrl

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuthFlowClientCredentials ¶
Bases: `OAuthFlow`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` ¶
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` ¶
```
scopes = {}

```

####  tokenUrl `instance-attribute` ¶
```
tokenUrl

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuthFlowAuthorizationCode ¶
Bases: `OAuthFlow`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` ¶
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` ¶
```
scopes = {}

```

####  authorizationUrl `instance-attribute` ¶
```
authorizationUrl

```

####  tokenUrl `instance-attribute` ¶
```
tokenUrl

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuthFlows ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  implicit `class-attribute` `instance-attribute` ¶
```
implicit = None

```

####  password `class-attribute` `instance-attribute` ¶
```
password = None

```

####  clientCredentials `class-attribute` `instance-attribute` ¶
```
clientCredentials = None

```

####  authorizationCode `class-attribute` `instance-attribute` ¶
```
authorizationCode = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OAuth2 ¶
Bases: `SecurityBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  type_ `class-attribute` `instance-attribute` ¶
```
type_ = Field(default=oauth2, alias='type')

```

####  flows `instance-attribute` ¶
```
flows

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OpenIdConnect ¶
Bases: `SecurityBase`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  type_ `class-attribute` `instance-attribute` ¶
```
type_ = Field(default=openIdConnect, alias='type')

```

####  openIdConnectUrl `instance-attribute` ¶
```
openIdConnectUrl

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Components ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  schemas `class-attribute` `instance-attribute` ¶
```
schemas = None

```

####  responses `class-attribute` `instance-attribute` ¶
```
responses = None

```

####  parameters `class-attribute` `instance-attribute` ¶
```
parameters = None

```

####  examples `class-attribute` `instance-attribute` ¶
```
examples = None

```

####  requestBodies `class-attribute` `instance-attribute` ¶
```
requestBodies = None

```

####  headers `class-attribute` `instance-attribute` ¶
```
headers = None

```

####  securitySchemes `class-attribute` `instance-attribute` ¶
```
securitySchemes = None

```

####  links `class-attribute` `instance-attribute` ¶
```
links = None

```

####  callbacks `class-attribute` `instance-attribute` ¶
```
callbacks = None

```

####  pathItems `class-attribute` `instance-attribute` ¶
```
pathItems = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  Tag ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  name `instance-attribute` ¶
```
name

```

####  description `class-attribute` `instance-attribute` ¶
```
description = None

```

####  externalDocs `class-attribute` `instance-attribute` ¶
```
externalDocs = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

###  OpenAPI ¶
Bases: `BaseModelWithConfig`
####  model_config `class-attribute` `instance-attribute` ¶
```
model_config = {'extra': 'allow'}

```

####  openapi `instance-attribute` ¶
```
openapi

```

####  info `instance-attribute` ¶
```
info

```

####  jsonSchemaDialect `class-attribute` `instance-attribute` ¶
```
jsonSchemaDialect = None

```

####  servers `class-attribute` `instance-attribute` ¶
```
servers = None

```

####  paths `class-attribute` `instance-attribute` ¶
```
paths = None

```

####  webhooks `class-attribute` `instance-attribute` ¶
```
webhooks = None

```

####  components `class-attribute` `instance-attribute` ¶
```
components = None

```

####  security `class-attribute` `instance-attribute` ¶
```
security = None

```

####  tags `class-attribute` `instance-attribute` ¶
```
tags = None

```

####  externalDocs `class-attribute` `instance-attribute` ¶
```
externalDocs = None

```

####  Config ¶
#####  extra `class-attribute` `instance-attribute` ¶
```
extra = 'allow'

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
