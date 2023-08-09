import cv2
import time
import pygame
import commentjson
from colorama import init, Fore, Style
from datetime import datetime

# Initialisiere Colorama für Farben in der Konsole
init(autoreset=True)

# Lade die Konfiguration aus der config.json-Datei
with open("config.json") as config_file:
    config = commentjson.load(config_file)

# Initialisiere Pygame für den Sound
pygame.mixer.init()
pygame.mixer.music.load(config["sound_path"])

# Öffne die Kamera
camera = cv2.VideoCapture(0)  # 0 steht für die Standardkamera, du kannst dies anpassen

# Initialisiere den Hintergrundsubtraktor mit angepassten Parametern
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=config["bg_subtractor_params"]["history"],
    varThreshold=config["bg_subtractor_params"]["varThreshold"],
    detectShadows=config["bg_subtractor_params"]["detectShadows"]
)

# Version des Scripts
script_version = "1.0"

# Willkommensnachricht und Version anzeigen
print(Fore.YELLOW + Style.BRIGHT + "Willkommen zur Bewegungserkennung!")
print(Fore.CYAN + f"Version: {script_version}\n")
time.sleep(3)  # Pause für 3 Sekunden, um die Willkommensnachricht anzuzeigen

# Initialisierung der Variablen für Bewegungserkennung und Tonausgabe
bewegung_erkannt = False
sound_abgespielt = False
letzte_zeit_abgespielt = time.time() - config["sound_cooldown"]  # Setze Timer auf Cooldown-Zeit vor dem Start
counter = 0  # Zähler für die benötigten Bewegungserkennungen

while True:
    ret, frame = camera.read()  # Lese ein Bild von der Kamera

    if not ret:
        break

    # Anwenden des Hintergrundsubtraktors, um bewegte Objekte zu isolieren
    fg_mask = bg_subtractor.apply(frame)

    # Entferne kleine Störungen im Vordergrundmaskenbild
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel=None)

    # Finde Konturen der bewegten Objekte
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    if len(contours) > 0:
        if not bewegung_erkannt:
            bewegung_erkannt = True
            sound_abgespielt = False

        # Filter für starke Bewegung
        strong_motion_detected = False
        for contour in contours:
            contour_area = cv2.contourArea(contour)
            if contour_area < config["min_contour_area"]:
                continue

            # Berechne die Geschwindigkeit der Bewegung
            elapsed_time = time.time() - letzte_zeit_abgespielt
            if elapsed_time > 0:
                motion_speed = contour_area / elapsed_time
                if motion_speed > config["min_motion_speed"]:
                    strong_motion_detected = True
                    break

        if not sound_abgespielt and strong_motion_detected:
            counter += 1
            if counter >= config["threshold"]:
                current_time = time.time()
                if current_time - letzte_zeit_abgespielt >= config["sound_cooldown"]:

                    # Aktuelle Systemzeit holen
                    current_time = datetime.now()

                    # Start- und Endzeitpunkte für die Bewegungserkennung erstellen
                    start_time = current_time.replace(hour=config["start_hour"], minute=0, second=0, microsecond=0)
                    end_time = current_time.replace(hour=config["end_hour"], minute=0, second=0, microsecond=0)
                    if start_time <= current_time <= end_time:
                        print(Fore.GREEN + f"Bewegung erkannt - Sound wird abgespielt")
                        pygame.mixer.music.play()
                        letzte_zeit_abgespielt = current_time.timestamp()
                        sound_abgespielt = True
                        counter = 0  # Setze den Counter zurück
                        pass
    else:
        bewegung_erkannt = False
        sound_abgespielt = False
        counter = 0  # Setze den Counter zurück

    # Zeige das bearbeitete Bild an
    cv2.imshow('Motion Detection', frame)

    # Zeige den Status der Bewegung in der Konsole an
    if bewegung_erkannt:
        timer = max(0, int(config["sound_cooldown"] - (time.time() - letzte_zeit_abgespielt)))
        timer_color = Fore.RED if timer > 0 else Fore.GREEN
        print(Fore.GREEN + f"Bewegung: {Fore.RESET}{Style.BRIGHT}JA | Timer: {timer_color}{timer}s{Fore.RESET}  {time.strftime('%H:%M:%S')} | Counter: {counter}/{config['threshold']}")
    else:
        timer = max(0, int(config["sound_cooldown"] - (time.time() - letzte_zeit_abgespielt)))
        timer_color = Fore.RED if timer > 0 else Fore.GREEN
        print(Fore.RED + f"Bewegung: {Fore.RESET}{Style.BRIGHT}NEIN | Timer: {timer_color}{timer}s{Fore.RESET}  {time.strftime('%H:%M:%S')} | Counter: {counter}/{config['threshold']}")

    # Beende die Schleife, wenn die 'q'-Taste gedrückt wird
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Räume auf und beende
camera.release()
cv2.destroyAllWindows()
