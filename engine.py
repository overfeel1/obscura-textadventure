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


