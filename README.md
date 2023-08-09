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

## Hinweise

- Das Skript kann mit der Taste "q" beendet werden.
- Die Bewegungserkennung erfolgt nur während des in der Konfiguration festgelegten Zeitfensters.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

