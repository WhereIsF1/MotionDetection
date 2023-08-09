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
pip install opencv-python pygame colorama commentjson
```
