# MotionDetection-Script

Dieses Python-Skript erkennt Bewegungen in Echtzeit mithilfe einer Webcam und gibt einen Sound aus, wenn eine bestimmte Anzahl von aufeinanderfolgenden Bewegungen erkannt wurde.

## Funktionen

- Erkennt Bewegungen in Echtzeit mithilfe der OpenCV-Bibliothek.
- Verwendet den Hintergrundsubtraktor-Algorithmus, um bewegte Objekte zu isolieren.
- Spielt einen Sound ab, wenn eine vordefinierte Anzahl von aufeinanderfolgenden Bewegungserkennungen erreicht wurde.
- Berücksichtigt eine Cooldown-Zeit, um wiederholte Tonausgaben zu vermeiden.
- Prüft, ob die Bewegungserkennung nur während eines bestimmten Zeitfensters erfolgen soll.

## Voraussetzungen

- Python 3.x
- OpenCV-Bibliothek
- Pygame-Bibliothek
- Colorama-Bibliothek
- commentjson-Bibliothek
- Eine Webcam oder Kamera, die von OpenCV unterstützt wird

## Installation

1. Stelle sicher, dass Python 3.x auf deinem System installiert ist.
2. Installiere die benötigten Bibliotheken, indem du den folgenden Befehl ausführst:

```
pip3 install opencv-python pygame colorama commentjson
```

## Konfiguration

Bearbeite die `config.json`-Datei, um die Einstellungen anzupassen:

- `sound_path`: Der Pfad zur Sounddatei, die abgespielt werden soll.
- `bg_subtractor_params`: Parameter für den Hintergrundsubtraktor-Algorithmus.
- `min_contour_area`: Die minimale Konturfläche, um als Bewegung erkannt zu werden.
- `min_motion_speed`: Die minimale Bewegungsgeschwindigkeit für starke Bewegungen.
- `threshold`: Die Anzahl der aufeinanderfolgenden Bewegungserkennungen für die Tonausgabe.
- `sound_cooldown`: Die Cooldown-Zeit in Sekunden zwischen aufeinanderfolgenden Tonausgaben.
- `start_hour`: Die Stunde, zu der die Bewegungserkennung starten soll.
- `end_hour`: Die Stunde, zu der die Bewegungserkennung enden soll.

## Verwendung

1. Stelle sicher, dass deine Webcam oder Kamera korrekt angeschlossen ist.
2. Führe das Skript aus:
```
python3 motiondetection.py
```
3. Das Skript öffnet das Kamerabild und beginnt mit der Bewegungserkennung.
4. Wenn eine Bewegung erkannt wird und die Anzahl der aufeinanderfolgenden Bewegungserkennungen den Schwellenwert erreicht, wird der Sound abgespielt.

## Ablauf des Skripts

1. Initialisierung der benötigten Bibliotheken und Lade der Konfiguration.
2. Initialisierung von Pygame für die Soundausgabe und Öffnen der Kamera.
3. Initialisierung des Hintergrundsubtraktors mit den angegebenen Parametern.
4. Willkommensnachricht und Version anzeigen.
5. Schleife zur Echtzeit-Bewegungserkennung.
   - Erfassung eines Kamerabildes.
   - Anwendung des Hintergrundsubtraktors, um bewegte Objekte zu isolieren.
   - Erkennung und Verarbeitung von Konturen bewegter Objekte.
   - Abspielen des Sounds bei starken Bewegungen und innerhalb des Zeitfensters.
6. Anzeigen des bearbeiteten Bildes und Status in der Konsole.
7. Beenden der Schleife durch Drücken der 'q'-Taste.
8. Aufräumen und Beenden des Skripts.

## Bewegungserkennung mit Sound-Ausgabe

Dieses Python-Skript erkennt Bewegungen durch die Kamera und gibt einen Sound aus, wenn bestimmte Bedingungen erfüllt sind.

### Funktionen und Erklärungen

1. **Importieren der benötigten Bibliotheken**
   Hier werden die benötigten Bibliotheken für die Bewegungserkennung, die Zeitsteuerung, die Sound-Ausgabe, die Konfigurationsverarbeitung, Farbformatierung und Datums-/Uhrzeitmanipulation importiert.

    ```python
    import cv2
    import time
    import pygame
    import commentjson
    from colorama import init, Fore, Style
    from datetime import datetime
    ```

2. **Initialisierung von Colorama**
   Die Colorama-Bibliothek wird verwendet, um farbige Ausgaben in der Konsole zu ermöglichen.

    ```python
    init(autoreset=True)
    ```

3. **Laden der Konfiguration aus der Datei**
   Die Konfigurationswerte werden aus einer JSON-Datei geladen, um verschiedene Parameter anzupassen.

    ```python
    with open("config.json") as config_file:
        config = commentjson.load(config_file)
    ```

4. **Initialisierung von Pygame für den Sound**
   Die Pygame-Bibliothek wird verwendet, um den Sound abzuspielen.

    ```python
    pygame.mixer.init()
    pygame.mixer.music.load(config["sound_path"])
    ```

5. **Öffnen der Kamera**
   Die Kamera wird mit OpenCV geöffnet, um Bilder aufzunehmen.

    ```python
    camera = cv2.VideoCapture(0)  # 0 steht für die Standardkamera, du kannst dies anpassen
    ```

6. **Initialisierung des Hintergrundsubtraktors**
   Der Hintergrundsubtraktor wird verwendet, um bewegte Objekte von statischem Hintergrund zu isolieren.

    ```python
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(
        history=config["bg_subtractor_params"]["history"],
        varThreshold=config["bg_subtractor_params"]["varThreshold"],
        detectShadows=config["bg_subtractor_params"]["detectShadows"]
    )
    ```

7. **Version und Willkommensnachricht anzeigen**
   Die aktuelle Version des Skripts und eine Willkommensnachricht werden in der Konsole angezeigt.

    ```python
    script_version = "1.0"
    print(Fore.YELLOW + Style.BRIGHT + "Willkommen zur Bewegungserkennung!")
    print(Fore.CYAN + f"Version: {script_version}\n")
    time.sleep(3)
    ```

8. **Initialisierung von Variablen für die Bewegungserkennung**
   Verschiedene Variablen werden für die Bewegungserkennung und Tonausgabe initialisiert.

    ```python
    bewegung_erkannt = False
    sound_abgespielt = False
    letzte_zeit_abgespielt = time.time() - config["sound_cooldown"]
    counter = 0
    ```

9. **Hauptschleife für die Bewegungserkennung**
   In dieser Schleife wird die Bewegungserkennung durchgeführt und der Sound bei Bedarf abgespielt.

    ```python
    while True:
        ret, frame = camera.read()

        if not ret:
            break

        fg_mask = bg_subtractor.apply(frame)

        # Rest des Codes...
    ```

10. **Anzeigen des bearbeiteten Bildes und Status in der Konsole**
    Das bearbeitete Bild wird angezeigt und der Status der Bewegungserkennung wird in der Konsole ausgegeben.

    ```python
    cv2.imshow('Motion Detection', frame)

    if bewegung_erkannt:
        timer = max(0, int(config["sound_cooldown"] - (time.time() - letzte_zeit_abgespielt)))
        timer_color = Fore.RED if timer > 0 else Fore.GREEN
        print(Fore.GREEN + f"Bewegung: ...")
    else:
        timer = max(0, int(config["sound_cooldown"] - (time.time() - letzte_zeit_abgespielt)))
        timer_color = Fore.RED if timer > 0 else Fore.GREEN
        print(Fore.RED + f"Bewegung: ...")
    ```

11. **Aufräumen und Beenden**
    Die Kamera wird freigegeben und die OpenCV-Fenster werden geschlossen.

    ```python
    camera.release()
    cv2.destroyAllWindows()
    ```

## Hinweise

- Das Skript kann mit der Taste "q" beendet werden.
- Die Bewegungserkennung erfolgt nur während des in der Konfiguration festgelegten Zeitfensters.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

