Realtime Server Reference
# Self-Hosting Realtime
Supabase Realtime is a server built with Elixir using the Phoenix Framework that allows you to listen to changes in your PostgreSQL database via logical replication and then broadcast those changes via WebSockets.
There are two versions of this server: `Realtime` and `Realtime RLS`.
`Realtime` server works by:
  1. Listening to PostgreSQL's replication functionality (using PostgreSQL's logical decoding)
  2. Converting the byte stream into JSON
  3. Broadcasting to all connected clients over WebSockets


`Realtime RLS` server works by:
  1. Polling PostgreSQL's replication functionality (using PostgreSQL's logical decoding and wal2json output plugin)
  2. Passing database changes to a Write Ahead Log Realtime Unified Security (WALRUS) PostgresSQL function and receiving a list of authorized subscribers depending on Row Level Security (RLS) policies
  3. Converting the changes into JSON
  4. Broadcasting to authorized subscribers over WebSockets


## Why not just use PostgreSQL's `NOTIFY`?#
A few reasons:
  1. You don't have to set up triggers on every table.
  2. `NOTIFY` has a payload limit of 8000 bytes and will fail for anything larger. The usual solution is to send an ID and then fetch the record, but that's heavy on the database.
  3. `Realtime` server consumes two connections to the database, then you can connect many clients to this server. Easier on your database, and to scale up you just add additional `Realtime` servers.


## Benefits#
  1. The beauty of listening to the replication functionality is that you can make changes to your database from anywhere - your API, directly in the DB, via a console, etc. - and you will still receive the changes via WebSockets.
  2. Decoupling. For example, if you want to send a new slack message every time someone makes a new purchase you might build that functionality directly into your API. This allows you to decouple your async functionality from your API.
  3. This is built with Phoenix, an extremely scalable Elixir framework.


## Does this server guarantee delivery of every data change?#
Not yet! Due to the following limitations:
  1. Postgres database runs out of disk space due to Write-Ahead Logging (WAL) buildup, which can crash the database and prevent Realtime server from receiving and broadcasting changes. This can be mitigated in the Realtime RLS version of this server by setting the Postgres config `max_slot_wal_keep_size` to a reasonable size.
  2. Realtime server can crash due to a larger replication lag than available memory, forcing the creation of a new replication slot and resetting replication to read from the latest WAL data.
  3. When Realtime server falls too far behind for any reason, for example disconnecting from database as WAL continues to build up, then database can delete WAL segments the server still needs to read from, for example after reconnecting.


### Client libraries#
  * JavaScript
  * Dart


### Additional links#
  * Source code
  * Known bugs and issues
  * Realtime guides


