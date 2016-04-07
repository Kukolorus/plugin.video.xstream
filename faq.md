# FAQ xStream
- [1. Was ist xStream?](#1-was-ist-xstream)
    - [a. Wo bekomme ich xStream?](#a-wo-bekomme-ich-xstream)
    - [b. Gibt es für mich Rechtliche Konsequenzen?](#b-gibt-es-für-mich-rechtliche-konsequenzen)
    - [c. Welche Seiten sind im Addon enthalten?](#c-welche-seiten-sind-im-addon-enthalten)
- [2. Konfigurieren von xStream](#2-konfigurieren-von-xstream)
    - [a. Bestimmte Seiten an/ausschalten?](#a-bestimmte-seiten-anausschalten)
    - [b. Was stelle ich am besten in den Settings ein?](#b-was-stelle-ich-am-besten-in-den-settings-ein)
    - [c. Manuelle oder automatische Hosterwahl?](#c-manuelle-oder-automatische-hosterwahl)
- [3. Fehler!](#3-fehler)
    - [a. Fehler bei der Installation](#a-fehler-bei-der-installation)
    - [b. Fehler bei der Globalen Suche](#b-fehler-bei-der-globalen-suche)
    - [c. Fehler beim Öffnen einzelner Seiten im Addon](#c-fehler-beim-Öffnen-einzelner-seiten-im-addon)
    - [d. Fehlermeldung bei den Hostern](#d-fehlermeldung-bei-den-hostern)
- [4. Kodi LOG-File](#4-kodi-log-file)
    - [a. Was ist ein Log-File?](#a-was-ist-ein-log-file)
    - [b. Wo finde ich das Log File/die Log Datei?](#b-wo-finde-ich-das-log-filedie-log-datei)
    - [c. Log Erstellen & Hochladen mittels Addon](#c-log-erstellen--hochladen-mittels-addon)

## 1. Was ist xStream?
xStream ist ein Video Addon für das Media-Center Kodi. Es beinhaltet mehrere Streaming-Seiten in einem Plugin, mit welchem man Filme und Serien Streamen kann, wir bilden praktisch die Brücke.

### a. Wo bekommt man xStream?
Entweder von einer Downloadquelle xStream herunterladen (dann wird aber nicht über Updates informiert), oder das xStream Repo installieren. Dieses ist momentan hier verfügbar:
* https://github.com/Lynx187/xStreamRepo/archive/master.zip

Alternativ Download des Repos:
* https://superrepo.org/kodi/addon/repository.xstream/

Zusätzlich kann man auch die neuste Version von xStream benutzen, wenn man die Nightly bzw. Beta Version herunterladen.
* Beta:
   https://github.com/StoneOffStones/plugin.video.xstream/tree/beta
* Nightly:
   https://github.com/StoneOffStones/plugin.video.xstream/tree/nightly

Wird die aktuelle 2.1.16 Beta installiert, ist es _vorher_ notwendig das script.modul Cryptopy  zu installieren:
* https://www.github.com/StoneOffStones/script.modul.cryptopy/archive/xstream.zip

**ACHTUNG!** *Für die Beta Version gibt es keinen Fehler-Support, für die Nightly erst recht nicht! Die Beta ist keine Finale Version und die Nightly ein Experimenteller Stand in denen getestet wird! Support gibt es nur für die Finale xStream Version!*

### b. Gibt es Rechtliche Konsequenzen?
Nein, durch unser Addon ist es möglich aus Kodi über dieses Addon einfach von den oben genannten Seiten zu streamen. Das bloße Streaming hat in Deutschland (Momentan) keine Rechtlichen Konsequenzen. Die meisten Streaming Seiten loggen ohnehin keine IP-Adressen usw. Genaueres findet man auf den einzelnen Seiten, hier ist nochmal ein Video über das Thema Streaming verlinkt. xStream an sich bringt, allgemein keine Konsequenzen mit sich, das Addon ist die bloße Brücke.

[![Nutzerfragen: Legalität von Streaming, Arbeitszeiten und Bild.de | Rechtsanwalt Christian Solmecke](http://img.youtube.com/vi/cDmvhJrLkmM/0.jpg)](http://www.youtube.com/watch?v=cDmvhJrLkmM)

### c. Welche Seiten sind im Addon enthalten?
Kinox.to, Movie4k.to, DDL.me, hdFilme.tv, BS.to, SeriesEver.to, Szene-Streams.com, Filmpalast.to, sind die Seiten die momentan enthalten sind.
Wir nehmen gerne neue Vorschläge an von Seiten die man hinzufügen könnte, wenn diese Seiten das nötige Potenzial bzw. Größe vorweist, werden sie vielleicht hinzugefügt.
Wir arbeiten stätig am erweitern des Addons.

## 2. Konfigurieren von xStream
### a. Bestimmte Seiten an/ausschalten?
In den Settings besteht die Möglichkeit bestimmte Seiten an bzw. auszuschalten. Dies kann von Nutzen sein, wenn Sie kein Interesse an bestimmte Medien haben. Diese werden dann auch in der Globalen Suche nicht angezeigt.

Bei den Seiten hinter denen ein blauer Punkt ist sind an. Entfernen des Punkt durch einen einfachen Klick und die Seite wird nicht mehr angezeigt.

### b. Was stellt man am besten in den Settings ein?
Am besten die bevorzugte Sprache auf Deutsch, wenn denn so gewünscht. Sonst am besten alles so wie es ist, die Views leer lassen, sowie die Downloads.

Wenn gesehene Filme auf einmal weg sind, liegt das an den Einstellungen im Seitenmenü. Hier die Markierung „gesehene Filme“ deaktivieren!

### c. Manuelle oder automatische Hosterwahl?
Wenn man nicht fitt in dem Vereich der Hosterauswahl ist, verwenden sie die Automatische Hosterwahl, in dieser werden auch nicht funktionierende Hoster rausgefiltert. Wenn nicht, dann ist die Hosterwahl auch nicht schwer, sondern sehr übersichtlich. Es ist ähnlich wie bei den Seiten Movie4K und Kinox.

## 3. Fehler!
### a. Fehler bei der Installation
Fehler können verschiedene Ursachen haben. Bei Hilfe bitte immer folgendes bekannt geben:
Log, Kodi Version, Betriebssystem, xStream Version, genaue Fehlerbeschreibung!
Wird die aktuelle 2.1.16 Beta installiert, ist es vorher notwendig das script.modul Cryptopy  zu installieren:
* https://www.github.com/StoneOffStones/script.modul.cryptopy/archive/xstream.zip

Bitte, schauen, ob der Fehler in einem früheren Post schon beantwortet wurde!

Es kann auch eine fehlerhafte Datei vorliegen, oder die .zip ist falsch aufbereitet.

### b. Fehler bei der Globalen Suche
Falls bei der Globalen Suche eine Fehlermeldung bekommen, dass eine Seite nicht erreichbar war bzw. die Suche durch eine Meldung unterbrochen wurde, liegt dies meist an der Seite. Meistens sind die Seiten in diesem Moment nicht erreichbar, dagegen können wir auch nichts tun. Einfach abwarten!
Es kann auch vorkommen, dass bei der Globalen Suche keine Treffer angezeigt werden, dann bitte in der gewünschten Seite die Suche nutzen (manchmal stören die Seiten, die Globale Suche)

*Bei den Seiten Kinox.to und Movie4K.to haben sie in den Settings die Chance die Domain in z.B. Kinox.tv oder .se zu verwenden. Nutzen sie diese Alternativen, die Seiten zu erreichen!*

### c. Fehler beim Öffnen einzelner Seiten im Addon

Das kann verschiedene Ursachen haben. Meistens liegt es aber an der Homepage Seite.
Denn wenn dort auch nur eine Kleinigkeit geändert wird, kann es schon sein, dass  das Site-Plugin nicht mehr geht.
Die Entwickler wissen es meist und arbeiten an einer Lösung. Bitte Sachlich bleiben und nicht jammern!
Die Seite im Browser aufrufen und auf Funktion überprüfen.
Im Anschluss das Problem schildern.

### d. Fehlermeldung bei den Hostern

Sollte dies der Fall sein, bitte den aktuellen URL Resolver installieren:
* https://offshoregit.com/tvaresolvers/tva-common-repository/raw/master/zips/script.module.urlresolver/

Bitte den gewünschten Film auf der Homepage auf Funktion kontrollieren.

## 4. Kodi LOG-File
### a. Was ist ein Log-File?
In dem log File werden alle Aktivitäten/Programmabläufe von Kodi protokolliert und gespeichert. Wenn man nun Probleme mit Kodi hat, ist es sehr hilfreich, dieses Log File im Forum zu Posten. Nur so kann eine schnelle und Zielgerichtete Lösung erfolgen.

### b. Wo finde ich das Log File/die Log Datei?
Den Speicherpfad von Kodi anzeigen lassen – Scroll weiter runter zum Punk Debug_Loggin und folgen den Beschreibungen.

Das ist immer vom Betriebssystem abhängig.
Im Folgenden werden bekannte Ordnerstrukturen der jeweiligen Betriebssysteme aufgelistet. Anstelle von "xbmc" kann in den Ordnern auch "kodi" stehen
(die Ordnerstruktur kann jedoch auch leicht von dieser Anleitung abweichen):

- Windows XP
    - `Documents and Settings\<your_user_name>\Application Data\Kodi`
- Vista/Windows 7
    - `C:\Users\<your_user_name>/%APPDATA%/Roaming/Kodi/Kodi.log`
- Mac OS X
    - `/Users/<username>/Library/Logs/ oder`
    - `/Users/<your_user_name>/Library/Application Support/Kodi/userdata`
- iOS
    - `/private/var/mobile/Library/Preferences`
- Linux
    - `$HOME/.kodi/temp/`
    - `$HOME/.kodi/userdata/temp/xbmc.log`
    - `$HOME/.kodi/userdata`
- OpenElec
    - `$HOME/.xbmc/userdata/temp/xbmc.log`
    - `$HOME/.kodi/temp/`
- Raspberry Pi 1-3
    - `/home/pi/.kodi/temp/`
    - `/home/pi/.xbmc/temp/xbmc.log`
- Android
    - `/android/data/org.xbmc.Kodi/files/.kodi/temp`
    - `data/data/org.xbmc.Kodi/cache/temp`

Die Ordner sind meist versteckt und müssen sichtbar gemacht werden, im Windows Explorer oder auf Android mit dem ESDateiexplorer.

Das Log File kann am besten mit Notepad++  unter Windows oder gedit unter Linux betrachtet werden.
Auch der normale Texteditor unter Windows geht, Notepad ist aber übersichtlicher.
Auf Android einen Texteditor verwenden zum Betrachten.
Übrigens die Kodi „log.old“ ist die Logdatei vom letzten Neustart/Crash. Also wenn man keine mehr erstellen kann, dann diese nehmen.

### c. Log Erstellen & Hochladen mittels Addon
Kodi hat Standardmäßig die beiden wichtigen Log Addons integriert (eines zum Lesen der Log, das andere zum Hochladen). Damit ist das Erstellen der Log Datei und Posten im Forum sehr viel einfacher.

In Kodi gehe zu:
* Desktop-Optionen
* Einstellungen
* Addons
* Suche

In die Zeile "log" ein und Klicks auf Fertig.

Folgende Addons auswählen und installieren diese:

Log Viewer für Kodi (nur zum Lesen der Log-Datei)
Kodi Log Uploader (zum Auslesen & Uploaden der Log-Datei)

Mit dem LogViewer kann man die Log Datei ansehen, mit dem LogUploaded das Log-File auf http://xbmclogs.com hochladen.

Bei der Installation eine E-Mail Adresse angeben. An diese wird dir dann nach dem LogUpload ein Link zur Log Datei geschickt.
Diesen Link im Forum Posten oder alles in einen Texteditor koperien, Die Datei speicherun und im Forum hochladen.

Debug-Logging (Kodi GUI):

Manchmal ist es gut das Debug Logging in Kodi zu aktivieren um noch mehr Informationen zu erhalten.

Folgendes Ausführen:
* Desktop-Optionen
* Einstellungen
* System
* Debugging
* "Debug-Logging aktivieren" anklicken

Fertig

Es wird nun am oberen Rand eine Statuszeile eingeblendet mit Infos; **Hier ist auch der Speicherort der Log-Datei zu sehen!**

Starte Kodi neu und öffne das Addon welches einen Fehler verursacht. Erstellen dann sofort eine Log-Datei (dann ist der Fehler leichter herauszulesen).

Das Debug-Logging kann im Anschluss wieder deaktiviert werden.

Unter dem Punkt  Komponentenspezifische Protokollierung kann man bei der Kategorie "Konfiguration der Komponentenspezifischen Protokollierung" noch Einstellen was alles im Debug-Log Protokolliert werden soll.
