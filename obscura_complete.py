import time
import random
import string
import os

pfad = None


# --- functions ---

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# druckt Text Wort für Wort mit kleinen Pausen
def slow_print_word_by_word(text, delay=0.3, dot_delay=0.15):
    words = text.split()
    for word in words:
        print(word, end='', flush=True)
        if word.endswith(('.', '!')):
            for _ in range(2):
                print('.', end='', flush=True)
                time.sleep(dot_delay)
        print(' ', end='', flush=True)
        time.sleep(delay)
    print()

# simuliert einen blinkenden Cursor = '/'
def blink_cursor(times=6, interval=0.5):
    for _ in range(times):
        print('/', end='', flush=True)
        time.sleep(interval)
        print('\r \r', end='', flush=True)
        time.sleep(interval)
    print()

# Kombination aus Wort-für-Wort-Druck und blinkendem Cursor
def print_with_unheimliche_pause(text, min_pause=0.5, max_pause=1.5):
    slow_print_word_by_word(text)
    blink_cursor(3, 0.3)
    time.sleep(random.uniform(min_pause, max_pause))

# druckt blinkende punkte
def blink_dots(times=2, interval=0.75):
    for _ in range(times):
        print('...', end='', flush=True)
        time.sleep(interval)
        print('\r   \r', end='', flush=True)
        time.sleep(interval)
    print('...', flush=True)

# DNA ASCII Animation für eines der Labor - Enden
def dna_animation(duration=3, interval=0.2):
    frames = [
        """
         A     T
          \\   /
           G-C
          /   \\
         T     A
        """,
        """
          \\   /
         A-G T-C
          /   \\
           T-A
        """,
        """
         T     A
          /   \\
           C-G
          \\   /
         A     T
        """,
        """
          /   \\
         T-C A-G
          \\   /
           G-C
        """
    ]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            clear_console()
            print(frame)
            time.sleep(interval)

# Ein Matrix ähnlicher Effekt, der "das booten des Terminals" simulieren soll
def matrix_effect(duration=3, width=60, height=15, interval=0.05):
    # Zeichnet einen Matrix-Effekt
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:',.<>?/\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        clear_console()
        for _ in range(height):
            line = ''.join(random.choice(chars) for _ in range(width))
            print(line)
        time.sleep(interval)

# --- Hauptmenü ---

def show_start_menu():
    clear_console()
    print("\n" * 2)
    print("     [=============================]")
    print("     [        WELCOME TO           ]")
    print("     [         'OBSCURA'           ]")
    print("     [      by robin koppers       ]")
    print("     [=============================]")
    print("     [   1. START                  ]")
    print("     [    2. HILFE                 ]")
    print("     [     3. BEENDEN              ]")
    print("     [=============================]")
    print()
    while True:
        auswahl = input("     Wähle eine Option (1–3): ")
        if auswahl == "1":
            print("\n     Spiel wird gestartet...\n")
            time.sleep(1)
            return "start"
        elif auswahl == "2":
            print("\n   >> Du befindest dich in einer Raumstation...")
            print("     >> Nutze deine Entscheidungen weise...")
            input("     >> Enter zum Zurückkehren...")
        elif auswahl == "3":
            print("\n     Programm wird beendet...")
            time.sleep(1)
            exit()
        else:
            print("     Ungültige Eingabe.")

# --- Labor ---

def labor_runde1():
    text = [
        "Du öffnest die Schleuse zum Labor.",
        "Ein Hauch gefrorener Luft streicht dir über das Gesicht.",
        "Die Probe liegt noch an ihrem Platz – aber der Behälter ist beschlagen, von innen.",
        "Ein tiefes Summen durchzieht den Raum – nicht von den Geräten, sondern aus der Wand selbst.",
        "Auf dem Boden: feine Spuren, wie von etwas, was erst geschmolzen und dann verdampft ist. Säure?",
        "Ein Display neben dem Behälter blinkt: 'Zellaktivität außerhalb des Isolationsbereichs registriert'.",
        "Du siehst die Probe – doch etwas stimmt nicht.",
        "Das Eis um die Probe pulsiert leicht, als ob es lebt.",
        "Plötzlich zuckt eine Form darin, diffus und schwer zu fassen.",
        "Dann fällt das Licht aus – Dunkelheit, die alles verschluckt."
        ]

    for satz in text:
        print_with_unheimliche_pause(satz)

def labor_TLMS():
    text = [
        "Die verbliebenen Teile klickst du aus der Halterung – der Weg nach innen ist jetzt frei.",
        "Du bewegst dich gebückt nach vorne, durch das riesige System der Schächte",
        "Als du gerade eine Leiter hinauf kletterst, hörst du wie dein Funkgerät anspringt",
        "Rauschen. Dann sagt eine Stimme: 'DON'T COME CLOSER' ",
        "Du hörst nicht auf die Stimme und kletterst weiter, bis du den Escape Pod erspähst",
        "'ESCAPE SYSTEM OFFLINE' zeigt der Boardcomputer"
        "Du näherst dich der Konsole. Dort ist noch etwas eingetragen, wurde aber nicht durchgeführt",
        "systemctl --force restart core.escape.pod"

    ]

    for satz in text:

        print_with_unheimliche_pause(satz)

def labor_TRMNL():

    text = [

    "Du tippst: > /usr/core/initiate.override(protokoll_δ)",
    "Du drückst ENTER – aber nichts passiert.",
    "Die Tür bleibt geschlossen, doch hinter dir... ein kratzendes Geräusch.",
    "Auf dem Terminal erscheint plötzlich: 'IT'S ALREADY INSIDE'.",
    "Der Alarm geht los. Die Dunkelheit wird von rotem, blinkendem Licht erhellt",
    "Dann siehst du es - Ein Xenomorph steht vor dir",
    "Bisher hast du nur von ihnen gehört und nicht an ihre Existenz geglaubt",
    "So wie die obersten Offiziere von Weyland-Yutani",
    "Das einzige was dir übrig bleibt ist kämpfen, denn du kannst nicht raus",
    "Du schnappst dir eine Brechstange und schlägst drauf los, doch du bewirkst nichts",
    "Du hast keine Chance gegen den perfekten Organismus. Es tötet dich nicht einfach,",
    "Es quält dich und frisst dich bei lebendigem Leib,",
    "So wie es den Rest der Crew getötet hat",
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)


def labor_EPV():

    text = [

        "Du öffnest die Luke des Escape Pods.",
        "Ein kalter Luftzug strömt herein – seltsam, denn der Sektor sollte druckdicht sein.",
        "Die Gänge draußen sind still, doch irgendetwas hat sich verändert.",
        "Die Wände atmen leise, als ob das Schiff selbst lebendig wäre.",
        "Ein leises Piepen ertönt. Dein HUD flackert: „IDENTITÄT UNBEKANNT – VORSICHT“.",
        "Du gehst weiter. Jeder Schritt hallt doppelt – als wärst du nicht allein.",
        "Ein Lichtblitz. Dann Dunkelheit.",
        "Als du wieder zu dir kommst, stehst du auf einer Raumbrücke, die es laut Plänen gar nicht geben dürfte.",
        "Eine Stimme ertönt in deinem Kopf: „Wir haben lange auf dich gewartet.“"
    ]



def labor_ENDEKOLONIE():
    text = [
        "Ruckartig koppelt sich der Escape Pod an das Andockmodul der Kolonie",
           "Eine künstliche Intelligenz begrüßt dich. Dann siehst du 2 Sanitäter auf dich zukommen",
           "Du wirst nach dem Notfall-ABCDE Schema untersucht, alles unauffällig",
           "Die Kolonialmediziner nehmen dir routiniert eine Blutprobe",
           "Doch wenige Minuten später ruft dich der leitende Arzt mit blassem Gesicht zurück in den Diagnoseraum.",
           "'Ihr Blutbild ist... identisch mit einem Crewmitglied der *Odyssey*.,"
           "Sergeant Vale. Gestorben vor drei Jahren beim Absturz auf LV-426B.'",
           "Du willst widersprechen, doch das Analysegerät blinkt plötzlich auf – ",
           "der Bildschirm zeigt keine Werte, sondern nur einen Satz:",
           "ES IST SCHON IN DIR ES IST SCHON IN DIR ES IST SCHON IN DIR ES IST SCHON IN DIR ES IST SCHON IN DIR ",
   ]

    for satz in text:
        print_with_unheimliche_pause(satz)
    time.sleep(1)
    dna_animation(duration=7)
    return


def laborA_Luftschacht():
    text = [
        "Die verbliebenen Teile klickst du aus der Halterung – der Weg nach innen ist jetzt frei.",
        "Du bewegst dich gebückt nach vorne, durch das riesige System der Schächte",
        "Als du gerade eine Leiter hinauf kletterst, hörst du wie dein Funkgerät anspringt",
        "Rauschen. Dann sagt eine Stimme: 'DON'T COME CLOSER' ",
        "Du hörst nicht auf die Stimme und kletterst weiter, bis du den Weg zum Escape Pod erspähst",
        "'ESCAPE SYSTEM OFFLINE' zeigt der Boardcomputer",
        "Du näherst dich der Konsole. Dort ist noch etwas eingetragen, wurde aber nicht durchgeführt",
        "systemctl --force restart core.escape.service"
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)

def labor_REBOOTESCAPEPOD():
    matrix_effect(duration=4)
    print_with_unheimliche_pause("\n "),
    text = [
            "########################################################100% ",
            "'SYSTEM HAS BEEN REBOOTED SUCCESSFULLY'",
            "'ALL SYSTEMS READY TO DEPLOY ESCAPE POD 1227-F'",
            "'3...2...1...'",
            "Du merkst, wie der Pod beschleunigt und dich vom Mutterschiff entfernt",
            "'PREDETERMINED ROUTE : MARS COLONY 86V DELTA / ETA = 221 DAYS'",
            "Du atmest auf... Zündest dir eine Zigarette an und lehnst dich zurück... Du schläfst ein",
            "Als du wach wirst, spürst du ein leichtes Kratzen im Hals...",
            "Zur Sicherheit machst du einen Med-Scan, doch dieser zeigt an 'NO ANOMALIES DETECTED'",
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)


def labor_ENDE_changeroute():
    text = [
        "'CHANGING ROUTE...TO... EARTH - ETA 2 YEARS 328 DAYS'",
        "Die Anzeige 'LIFE SUPPORT: NOMINAL' beginnt zu flackern.",
        "Plötzlich erscheint eine rote Meldung: 'O₂ RESERVE BELOW CRITICAL – 24:00:00 REMAINING'.",
        "Du bist an Sauerstoffmangel gestorben.",
        "2 Jahre später wird deine Leiche auf Planet HBLA-1 geborgen.",
        "Man hat bei deiner Autopsie multiple DNA-Fragmente eines weiteren Organismus gefunden.",
        "Dieser Organismus kann nicht supprimiert werden und hat 67% der dort ansässigen Bevölkerung getötet.",
        "Durch den Organismus in dir sind 3.198.299 Menschen gestorben."
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)
    return

    #LABOR B ABSCHNITT

def labor_HUDEND():

        text = [
            "Mit zitternden Fingern tippst du auf das Steuerfeld deines Helms.",
            ">> HUD ONLINE << blinkt auf, begleitet von einem kalten Summen im Schädel.",
            "Dein Sichtfeld überlagert sich mit Schaltplänen, Diagnosen, fremden Codes – zu schnell, zu viele.",
            "Eine Stimme flüstert durch den Funkkanal. Es ist deine. Aber... verzerrt, wie aus einem anderen Leben.",
            ">> SYSTEMZUGRIFF: GEHIRNSTAMM <<",
            "Dein Körper gehorcht nicht mehr dir – du bewegst dich, aber nicht aus eigenem Willen.",
            "Dein Puls steigt. Doch dein HUD zeigt: 'HERZFREQUENZ = 0 BPM'.",
            "Dein letzter Gedanke ist kein Gedanke – sondern ein Befehl, der nicht von dir stammt.",
            "Dann löscht sich das HUD selbst. Alles wird schwarz.",
            "Niemand wird je herausfinden, ob du gestorben bist – oder weiter funktionierst."
        ]

        for satz in text:
            print_with_unheimliche_pause(satz)


# --- DISSTRESS SIGNAL  ---

def NS_runde1():
    text = [
        "Du startest die Analyse des Signals",
        "Die Waveform sieht aus wie ein klassisches 'Save Our Souls'",
        "Aber die Tonspur passt nicht - ",
        "Ein Fragment: 'bitte...' - dann Stille",
        "'...sie hört nicht auf... sie... hört nicht...auf...'",
        "Nächster Abschnitt: '...alles ist...falsch hier', doch diesmal eine andere Stimme",
        "Jede Stimme klingt menschlich - doch nicht wie aus deiner Crew ",
        "Die Analyse ergibt: Es sind 12 verschiedene Sprecher."
        "Ein anderes Schiff. Kein Transponder. Kein Name. ",
       "Aber es sendet SOS. Ununterbrochen... "
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)

def NS_EVA():
    text = [
        "Du steigst in den EVA-Anzug",
        "Der Helm klickt ein, das visuelle HUD aktiviert sich ",
        "Ein kurzes Zischen - Druckausgleich. ",
        "Die Schleuse fährt surrend auf. Kaltes, klares Vakuum. −270,45 °C. Absolute Stille",
        "Vor Dir : Ein Schiff. Es ist wie deines - aber auf dem Kopf ",
        "Die Kennzeichnung fehlt. Kein Transponder, kein Name",
        "Du stößt dich ab. Mit langsamen Bewegungen näherst du dich dem fremden Schiff",
        "Der Funk bleibt still - Nur dein Herzschlag im Helm ist zu hören",
        "Die Schleuse des anderen Schiffes steht offen ",
        "Du schwebst hinein. Die Innenstruktur gleicht deiner bis ins letzte Detail ",
        "Doch irgendetwas stimmt nicht. Die Gravitation ist leicht versetzt, die Räume fühlen sich anders an",
        "Dein integrierter Kompass dreht sich ohne Kontrolle",
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)


def NS_KONTAKTPROTOKOLL():

    text = [

    "Das Kontaktprotokoll startet - Dein Atem beschlägt das Visier ",
    "Eine Stimme erklingt - sanft, vertraut 'Alles ist gut.. Komm Heim..' ",
    "Das Terminal zeigt:  >> PSYCHOMETRISCHE SYNCHRONISIERUNG LAUFEND << ",
    "Dein Herz beginnt schneller zu schlagen – du kennst diese Stimme.",
    "Es ist Mira. Deine Frau. Doch sie ist auf der Erde…",
    "Die Konsole flackert. Ihr Gesicht erscheint – älter, aber vertraut. Tränen glänzen in ihren Augen.",
    "'Ich hab dich nie verlassen', sagt sie. 'Du musst nicht mehr kämpfen.'",
    "Etwas in dir gibt nach. Schwerelosigkeit – aber diesmal innerlich.",
    "Du schließt die Augen. Du riechst Lavendel. Ihr Parfüm.",
    "Als du sie wieder öffnest, sitzt du auf eurer Veranda. Sommerabend. Miras Hand in deiner.",
    "Die Sonne geht unter. Vögel singen. Keine Alarme. Kein Notrufsignal.",
    "Obscura ist verschwunden. Vielleicht war sie nie real.",
    "Vielleicht bist du jetzt endlich frei."

    ]

    for satz in text:
        print_with_unheimliche_pause(satz)
    return

def NS_ENDEEH():

    text = [

    "Du näherst dich dem Gravitationskern.",
    "Er dreht sich immer schneller, das Licht bricht in unmöglichen Winkeln.",
    "Ein Kreischen durchdringt deinen Helm – nicht laut, sondern innerlich.",
    "Der Kern öffnet sich. Ein irisierendes Portal. Dahinter: Bewegung, rot, pulsierend.",
    "Du wirst hineingezogen – dein Körper verliert Form, Identität und Richtung.",
    "Als du wieder etwas siehst, ist alles... falsch.",
    "Der Raum lebt. Metall glüht. Stimmen beten in Latein.",
    "Wände sind aus Fleisch. Der Boden aus Knochen. Ein Herz schlägt – es ist nicht deines.",
    "Du rennst, doch alles bleibt gleich. Du schreist, aber dein Mund ist versiegelt.",
    "Etwas kriecht über deine Haut – von innen.",
    "Du begreifst: Das ist kein Ort. Es ist ein Wille. Und du bist jetzt Teil davon.",
    "Für immer. Du kannst nicht zurück. Du darfst nicht zurück.",
    ]

    for satz in text:
        print_with_unheimliche_pause(satz)

def NS_ENDEANOMALIEN():

    text = [

    "Du folgst dem Gang und den Anomalien – oder sie folgen dir.",
    "Die Gravitation kehrt sich um. Deine Füße sind oben, dein Kopf unten.",
    "Dann wieder umgekehrt. Dein Körper rotiert, ohne dass du dich bewegst.",
    "Wände atmen. Die Schwerkraft zieht dich an etwas – aber nicht an einen Ort.",
    "Ein Riss erscheint im Gang, als hätte jemand Raum und Zeit aufgeschlitzt.",
    "Du blickst hinein. Du erkennst nichts. Und dann erkennst du dich.",
    "Du bist das Schiff. Der Gang. Die Leere. Und niemand hat dich je gerufen.",
    "Doch plötzlich flackert etwas am Rand deines Sichtfelds...",
    "Ein blinkender Cursor. Eine Eingabeaufforderung: > run /escape/emergence",
    "Du drückst 'ENTER' ",
    "Ein Riss öffnet sich. Weißes Licht. Wärme. Der Geruch von Erde.",
    "Du wachst auf – in einem Feld, unter echtem Himmel, Die Sonne über dir. Kein Alarm. Keine Stimmen.",
    "Obscura? Hat nie existiert.."
]
    for satz in text:
        print_with_unheimliche_pause(satz)


# --- Hauptlogik ---

def main():
    global pfad
    pfad = None

    for runde in range(0, 5):

        if runde == 0:

            for satz in [
                #INTRO TEXT
                "Du wachst aus dem Kryoschlaf auf",
                "Die Kapsel öffnet sich mit einem zischenden Laut",
                "Es ist kalt - ZU kalt für die Systeme, die eigentlich aktiv sein sollten",
                "Dunkelheit flutet den Raum, nur ein rotes Notlicht pulsiert wie ein langsamer Herzschlag",
                "Ein metallischer Geruch liegt in der Luft",
                "Du erinnerst dich an deine Forschung : Ein Organismus in einer Petrischale im Labortrakt",
                "Dein Körper fühlt sich fremd an, taub und zu leicht",
                "Irgendwas stimmt nicht mit dir..."
                "Das Boardterminal vor dir flackert nervös.",
                "Eine rote Meldung blinkt im Takt des Notlichts:",
                "INCOMING DISTRESS SIGNAL – MATCH: U.S.S. OBSCURA [ID: 33A-7].",
                "Das ist… dein Schiff. Deine Kennung.",
                "Aber du bist doch hier.",
                "Dein Name ist 'Elena Voss' ",

            ]:
                print_with_unheimliche_pause(satz)

        elif runde == 1:
            for satz in [">[1] Du gehst ins Labor um nach der Petrischale zu sehen"]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du untersuchst das DISSTRESS Signal"]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                pfad = "A"
                labor_runde1()
            elif wahl == "2":
                pfad = "B"
                NS_runde1()
            else:
                print("Ungültige Eingabe")

        elif runde == 2 and pfad == "A":
            for satz in [">[1] Du schaltest deine Taschenlampe ein "]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du versuchst über das Terminal die Tür zu öffnen "]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                labor_TLMS()
            elif wahl == "2":
                labor_TRMNL()
            else:
                print("Ungültige Eingabe")

        elif runde == 2 and pfad == "B":
            for satz in [">[1] Du ziehst den Raumanzug an und machst dich auf, zum verlassenen Schiff "]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du versuchst, über das Terminal Kontakt mit dem fremden Schiff aufzunehmen"]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                NS_EVA()
            elif wahl == "2":
                NS_KONTAKTPROTOKOLL()
                return

        elif runde == 3 and pfad == "A":
            for satz in [">[1] Du kletterst in den Lüftungsschacht "]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du aktivierst dein internes HUD "]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                laborA_Luftschacht()
            elif wahl == "2":
                labor_HUDEND()

        elif runde == 3 and pfad == "B":
            for satz in [">[1] Du steigst den Gravitationstrakt hinab"]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du folgst den Anomalien "]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                NS_ENDEEH()
                return
            elif wahl == "2":
                NS_ENDEANOMALIEN()
                return

        elif runde == 4 and pfad == "A":
            for satz in [">[1] Du gibst den Befehl ein und rebootest den Escape Pod"]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du verlässt den Escape Pod, irgendwas stimmt hier nicht..."]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                matrix_effect(3)
                labor_REBOOTESCAPEPOD()
            elif wahl == "2":
                labor_EPV()

        elif runde == 4 and pfad == "B":
            for satz in [">[1] "]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] "]:
                print_with_unheimliche_pause(satz)

        elif runde == 5 and pfad == "A":
            for satz in [">[1] Du bleibst auf der Kolonie-Route"]:
                print_with_unheimliche_pause(satz)
            for satz in [">[2] Du änderst die Route zu 'Erde' "]:
                print_with_unheimliche_pause(satz)

            wahl = input(">Tippe 1 oder 2< ")
            if wahl == "1":
                labor_ENDEKOLONIE()
            elif wahl == "2":
                labor_ENDE_changeroute()

if __name__ == "__main__":
    status = show_start_menu()
    if status == "start":
        main()



