Skip to content
Menu
Return to top
# List​
GET
/deployments
List currently running deployments
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Responses​
200400401
Get all currently running deployments.
Content-Type
application/json
SchemaJSON
JSON
[
{
"id": 0,
"application_id": "string",
"deployment_uuid": "string",
"pull_request_id": 0,
"force_rebuild": true,
"commit": "string",
"status": "string",
"is_webhook": true,
"is_api": true,
"created_at": "string",
"updated_at": "string",
"logs": "string",
"current_process_id": "string",
"restart_only": true,
"git_type": "string",
"server_id": 0,
"application_name": "string",
"server_name": "string",
"deployment_url": "string",
"destination_id": "string",
"only_this_server": true,
"rollback": true,
"commit_message": "string"
}
]
GET
/deployments
## Samples​
Powered by  VitePress OpenAPI 
