var PouchDB = require('pouchdb');
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

async function main() {

  var local_db = new PouchDB('kata-test');
  var remote_db = new PouchDB('http://<your-database-here>');
  
  async function get_players() {
    var db_players = await local_db.allDocs({
      include_docs: true
    });
    return db_players.rows.map(item => item.doc).filter(item => item.type === "spieler")
  }

  PouchDB.replicate(remote_db, local_db);
  local_db.sync(remote_db, {live:true});

  var player_name = "empty";
  console.log("Wie ist dein Name?");
  const interaction = readline[Symbol.asyncIterator]();
  player_name = (await interaction.next()).value;
  console.log(" ");
  console.log("Hello " + player_name);

  if (!(await get_players()).map(item => item._id).includes(player_name)) {
    await local_db.put({
      _id: player_name,
      type: "spieler",
      level: 1,
      kraft: 1
    })
    console.log("Du scheinst neu zu sein! Willkommen!");
  } else {
    console.log("Dein Gesicht kam mir gleich bekannt vor!");
  }
  console.log(" ");

  console.log("Befehle mir etwas:");
  for await (const command of readline) {
    var command_list = command.split(" ");
    console.log(" ");
    switch(command_list[0]) {
      case "status":
        var current_players = await get_players()
        current_players.forEach(player => {
          console.log(player._id, player.level, player.kraft);
        })
        break;
      case "level":
        var current_player = (await get_players()).filter(item => item._id === player_name)[0];
        var neues_level = current_player.level + Number(command_list[1]);
        current_player.level = neues_level;
        local_db.put(current_player)
        console.log("Dein neues Level ist " + neues_level + "!");
        break;
      case "kraft":
        var current_player = (await get_players()).filter(item => item._id === player_name)[0];
        var neue_kraft = current_player.kraft + Number(command_list[1]);
        current_player.kraft = neue_kraft;
        local_db.put(current_player)
        console.log("Deine neue Kraft ist " + neue_kraft + "!");
        break;
      default:
        console.log("retry")
        break; 
    }

    console.log(" ");
    console.log("Befehle mir etwas:");
  }
}

main()