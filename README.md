# ClickCounter
- on press farbe ändern
- Counter pro Tag speichern
- Datenbank beschreiben pro Tag -> (Webserver() auslesen und Graph erstellen
- mehrere Mäuse(CRUD) 
- Delete -> sind sie Sicher, dass die Maus gelöscht werden soll?
- start stop session
- neuer Tag = neue Session
- Summe aller klicks anzeigne in GUI
- Gui schöner machen
- Hintergrund ausführbar machen
- maybe spielzeit (neu, stop, start, ende)

Graph
- Sessions
- durschn Sessionlaufzeit
- Summe aller klicks mit dieser Maus

Maus
- ID(PK)
- Name
- Beschreibung
- Hersteller
- Teilenr
- kaufdatum
- Links klick summe
- mittelklick Summe
- rechts klick summe
- Sessions insgesamt = letzte Session_ID
- 
Session
- session_ID(PK)
- maus_ID(FK)
- Datum
- sesion start(timestamp) 
- session end(timestamp)
- links klicks
- rechts klicks
- 