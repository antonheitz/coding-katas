## Kata

Level-Counter mit einem CouchDB-Server

## Story

Ihr seid in einer spannenen Runde Munchkin, wobei es zuweilen sehr hitzig wird.

Leider kommen ab und zu einige Spieler mit ihren Stufen (1-10) und ihrer Angriffskraft (1-100) durcheinander.

Als guter Entwickler gilt für dich: Warum etwas in 5 Minuten manuell machen, wenn man es in 5 Stunden automatisieren kann!

## Aufgabe

Es gibt eine Couch-DB für euer Spiel: http://104.248.251.247:80/kata (keine Auth nötig)

Schreibe ein Skript mittels JS/TS und PouchDB die folgende Schitte ausführt:
 - Erstellen einer lokalen Datenbank
 - Aktivierung der Replizierung mit der externen CouchDB
 - Abfrage des Spielernamens
 - Falls der Spielername noch nicht bekannt ist, erstelle einen in der Lokalen DB
 - Nun soll auf eine eingabe gewartet werden: 
    - *status* zeigt alle spieler mit Namen, Level und Angriffskraft
    - *level <wert>* ändert das Level des Benutzers um den Wert (Achtung! Der Wert kann sowohl positiv als auch negativ sein!)
    - *kraft <wert>* ändert die Angriffskraft des Benutzers um den Wert (Achtung! Der Wert kann sowohl positiv als auch negativ sein!)