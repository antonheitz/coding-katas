var PouchDB = require('pouchdb');

var local_db = new PouchDB('kata-display');
var remote_db = new PouchDB('http://<your-database-here>');

PouchDB.replicate(remote_db, local_db);
local_db.sync(remote_db, {live:true}).on('change', async change => {
    console.log(change.change.docs);
})