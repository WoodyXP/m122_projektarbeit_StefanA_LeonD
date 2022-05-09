# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

TODO: In 2-3 Sätzen beschreiben was die Skripte grundsaetzlich tun.

#### Script 1: Git clone update repos
Das erste Skript dient dazu schnell viele Repos von einer List in einem Inputfile zu clonen.

#### Script 2: Git exract commits
Mit dem zweitem Skript sollte man können, Logs von verschiedenen Repos in einem Basedir zu nehmen und in einem File speichern, aber auch mit den Daten ein Diagram herstellen in dem man sieht wer, wann commited hat.

## Installationsanleitung für Administratoren

### Installation

TODO: Wie ist das skript zu installieren. (z.B. apt-get install ... oder tar xvf .... oder ...)

Da dieses Projekt auf Git ist, kann man es mit einem Git clone bei sich lokal holen.

    git clone https://github.com/WoodyXP/m122_projektarbeit_StefanA_LeonD.git

Nachdem man das Gitprojekt lokal hat muss man einige Packages installieren damit alles funktioniert.

Wir haben ein setup skript, das uns erlaubt mit einem Kommando alles zu installieren was man braucht.

1. Wir müssen die Berechtigungen geben damit das Setupskript funktioniert.
Navigieren Sie zum bin Ordner. Hier müssen wir dem setup_script.sh die Rechte geben.

    sudo chmod 755 setup_script.sh


2. Danach führen wir das Skript aus.


    ./setup_script.sh
        

Jetzt sollte alles installiert sein. Um sicher zu sein, dass alles da ist, können Sie.

    python3

und 

    pip3

In der Commandline eingeben.

Falls "-bash: pip3: command not found" oder "-bash: python3: command not found" angezeigt wird, bedeutet
es, dass die Packages nicht oder nicht richtig installiert worden sind. 

Bei diesem Fall können Sie Leon Domiter oder Stefan Arsic kontaktieren.

### Konfiguration

TODO: Beschreibung der Konfigurationsfiles (Beispiel-Files erstellen im Repo)

TODO: Wie ist ein allfaelliger Cronjob einzurichten

TODO: Wie sind User-Home-Templates einzurichten

....

Keine nötig für Skript 1 und Skript 2

## Bediensanleitung Benutzer

TODO: Erzeugen der Input-Files beschreiben, falls noetig

TODO: beschreiben des Scriptaufruf

TODO: beschreiben der erzeugt files (falls solche erzeugt werden)

TODO: Lokation von logfiles und bekannte Fehlermeldungen beschreiben.

#### Script 1: Git clone update repos
Nur das erste Skript wird Input-Files benötigen, und diese sind ganz leicht zu erstellen.

Unser Git clone update repos Skript kann mit CSV, aber auch mit anderen Datenformat wie z.B. TXT arbeiten.

Wir benützten keine Headers sondern fangen gleich mit den Daten an.

Das Inputfile sieht so aus:

    <<GIT-URL>> <<Targetdirectory>>

Das GIT-URL ist einfach der Link, dem man benützt um ein Git Repo zu clonen.

Das Targetdirectory ist der Name des Ordners wo die Repo geclont werden soll.

Ein funktionalbares Inputfile würde so aussehen:

    https://github.com/iotkitv3/http IOTHTTP
    https://github.com/WoodyXP/m122_projektarbeit_StefanA_LeonD M122_Vagrant
    https://github.com/WoodyXP/Plantify Plantify
    https://github.com/WoodyXP/Fast_Calculator UK_Modul

Für das Teilen der GIT-Url und Targetdirectory benützten wir ein Whitespace.

Wichtig für das Inputfile ist noch, das die URL stimmt und dass der Targetdirectory Name keine speziellen Zeichen
beinhaltet. A-Z, 0-9 und -,_


Das Script wird wie schon in der [Projektdokumenation] (docs/Projektdokumentation.md) aufgerufen.

Für das normale starten ohne logs wird nur der Pfad zum Basedir und der Pfad zum Inputfile gebraucht.

Ohne zusätztliche Logs

        python3 ./gitrepoupdater.py BASEDIR REPO_INPUT_FILE

Mit zusätliche Logs

        python3 ./gitrepoupdaer.py -d BASEDIR REPO_INPUT_FILE

Das einzige Outputfile vom erstem Skript werden die Logs sein.
Diese werden im gleichen Order erstellt in dem sich das Skript befindet.

Das Logfile beinhaltet alle Infos der estellten Repos und welche Repos getpulled und gelöscht werden,
falls im Inputfile etwas nicht stimmt, werden Errors ins File gelegt mit der Fehlermeldung.

#### Script 2: Git Extract Commits

Das Script braucht keine externen Inputfiles und keine Conifg und Inputfiles, jedoch braucht es den Absoluten Pfad vom 
Homedirectory bis zum Base/Targetdir.

Wie auch schon Oben bescrhieben braucht das Script nur den Pfad um zu funktionieren, es kann aber mit zusätzlichen Flags
aufgerufen werden um Kleinigkeiten zu ändern/konfigurieren.

##### Ausführung

1. Script mit nur Base/Targetdir aufrufen

   Flags: -t

        python3 ./gitExtractCommit.py -t BASEDIR

   Output:

   - Default_Commit_Log Outputfile mit Git Commits wird im gleichen Ordner generiert
   - YYYYMMDDHH-MM-SS_gitComitExtract.log wird im normal Falls unter dem Ordner ../log/ generiert werden.
   

2. Script mit dem Base/Targetdir und neuen Outputfile Namen

   Flags: -t -n

        python3 ./gitExtractCommit.py -t BASEDIR -n OUTPUTFILENAME

   Output:

   - OUTPUTFILENAME Outputfile mit Git Commits wird im gleichen Ordner generiert
   - YYYYMMDDHH-MM-SS_gitComitExtract.log wird im normal Falls unter dem Ordner ../log/ generiert werden.
   

3. Script mit dem Base/Targetdir und neuen Outputfile Namen mit zusätzlichen Logs

   Flags: -t -n -verbose

        python3 ./gitExtractCommit.py -t BASEDIR -n OUTPUTFILENAME -verbose

   Output:

   - OUTPUTFILENAME Outputfile mit Git Commits wird im gleichen Ordner generiert
   - YYYYMMDDHH-MM-SS_gitComitExtract.log wird im normal Falls unter dem Ordner ../log/ generiert werden.
   - Es werden zusätzlich Logs in der Console ausgegeben.


4. Script mit dem Base/Targetdir, neuen Outputfile Namen und ausgewählter Logsfile Speicherlokation

   Flags: -t -n -l

        python3 ./gitExtractCommit.py -t BASEDIR -n OUTPUTFILENAME -l LOGSAVELOCATION

   Output:

   - OUTPUTFILENAME Outputfile mit Git Commits wird im gleichen Ordner generiert
   - YYYYMMDDHH-MM-SS_gitComitExtract.log wird im Pfad gespeichert die angegeben worde, falls Ordner nicht exestieren, werden diese erstellt.
   

Beim erzeugten CommitLogs File werden 4 Sachen Header benützt.

Diese sind:

   - ***Targetdir***: Lokalen Pfad und Namen des Lokalem Repos
   - ***Date***: Datum des Commits, Formet= YYYYMMDD
   - ***Commit Hash***: Commit Hash des Commits
   - ***Author***: Author des erstellten Commits


##### Fehler   
   
Das Script wird Fehler ausgeben falls der Input nicht richtig gemacht wird.

Bekannte Fehler sind:

1. Flag -t wird nicht benützt
- gitExtractCommits: error: the following arguments are required: -t/--Targetdir

2. Ein unbekanntes Argument wird verwendet
- gitExtractCommits: error: unrecognized arguments: -p

Alle anderen Fehler werden vom Script selber gehandled und geben Meldungen im Logfile aus.

