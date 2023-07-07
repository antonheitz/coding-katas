## Munchkin CLI

A real time stats tracker counter with CouchDB server replication.

## Prerequisites

For this cata a running and open (no auth) [Couchdb](https://couchdb.apache.org/) must be accessible to all users (e.g. http://1.2.3.4:5984/kata).

You can use the display application in the data folder to monitor changes to the database in real time.

## Story

You're in an exciting round of munchkin, which gets very heated at times.

Unfortunately, sometimes some players get confused with their levels (1-10) and attack power (1-100).

To be a good developer, why do something manually in 5 minutes when you can automate it in 5 hours!

## Rules

There is a couch db for your game: http://your-database-here (no auth needed)

Write a script using JS/TS and PouchDB (http://www.pouchdb.com) that performs the following steps:
 - Create a local database
 - Enabling replication with the external CouchDB
 - Query the user for the current player name
 - If the player name is not known yet, create one in the Local DB (level 1 and attack power 1)
 - Now you should wait for an input (loop):
    - "status" -> shows all players with name, level and attack power
    - "level {value}" -> changes the user's level by the value (Attention! The value can be both positive and negative!)
    - "power {value}" -> changes the user's attack power by the value (Warning! The value can be both positive and negative!)