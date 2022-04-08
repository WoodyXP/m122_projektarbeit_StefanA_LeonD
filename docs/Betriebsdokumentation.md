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
es, dass die Packages nicht oder nicht richtig installiert geworden sind. 

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

