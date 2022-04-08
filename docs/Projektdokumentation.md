# Projekt Dokumentation

[[_TOC_]]

## Lösungsdesign
Anhand der Analyse wurde folgendes Lösungsdesign entworfen.

In der LB02 haben wir zur Aufgabe bekommen 2 Skripts zu schreiben.
Beide wurde mit Python programmiert.

#### Script 1: Git clone update repos
Das erste Skript dient dazu schnell viele Repos von einer List in einem Inputfile zu clonen.

#### Script 2: Git exract commits
Mit dem zweitem Skript sollte man können, Logs von verschiedenen Repos in einem Basedir zu nehmen und in einem File speichern, aber auch mit den Daten ein Diagram herstellen in dem man sieht wer, wann commited hat. 


### Aufruf der Skripte


TODO: schreiben sie wie die Skripte aufgerufen werden sollen (d.h. welche Parameter werden übergeben, gibt es Interaktionen mit dem Skript, läuft es automatisch täglich ab?)

Beide Skripte können mit einem -d aufgerufen werden, dieser wird zusätztliche Logs ausgeben.


#### Script 1: Git clone update repos
Für das erste Skript muss man 2 Parameter angeben.
1. BASEDIR, das Directory wo die Repos geclont werden sollen.
2. REPO_INPUT_FILE, das Inputfile mit den GIT Urls und dem Zieldirectory/Namen vom Folder wo das Repo geclont wird.

Ohne zusätztliche Logs

        ./gitrepoupdater.py BASEDIR REPO_INPUT_FILE

Mit zusätliche Logs

        ./gitrepoupdaer.py -d BASEDIR REPO_INPUT_FILE

Das Flag "-d" dient dazu dem Skript zu sagen, dass er alle Logs ausgeben soll.

#### Script 2: Git exract commits
Auch für das zweite Skript muss man nur 2 Parameter mitgeben.
1. BASEDIR, das Directory wo die Repos sich befinden.
2. COMMITOUTPUTFILE, der Name des Outputfiles

Ohne zusätztliche Logs

        ./gitextractcommits.py BASEDIR COMMITOUTPUTFILE

Mit zusätliche Logs

        ./gitextractcommits.py -d BASEDIR COMMITOUTPUTFILE
Wie beim Skript 1 macht das Flag "-d" logs auszugeben


### Ablauf der Automation

TODO: Hier kommt ihr UML-Activity Diagramm

#### Script 1: Git clone update repos

![image](img/script1_uml.png)

#### Script 2: Git exract commits

![image](img/script2_uml.png)


### Konfigurationsdateien

TODO: Definieren sie welche Parameter in welchen Konfigurationsdateien gespeichert werden.

#### Script 1: Git clone update repos

Für das erste Skript werden keine Configfiles gebraucht.

#### Script 2: Git exract commits

Auch für das zweite Skript werden wir kein Configfile brauchen.

## Abgrenzungen zum Lösungsdesign

TODO: Nachdem das Programm verwirklicht wurde hier die unterschiede von der Implemenatino zum Lösungsdesign beschreiben (was wurde anders gemacht, was wurde nicht gemacht, was wurde zusaetzlich gemacht)

#### Script 1: Git clone update repos

Die Aufgabenstellung des Skriptes 1 ist sehr simple und alle Kriterien sollte leicht zum implementieren sein.

#### Script 2: Git exract commits

Alles was in der Aufgavenstellung des Skriptes 2 steht, kann auch ohne grössere Probleme implementiert werden.
