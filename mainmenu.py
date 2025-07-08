import time
from game.effects import clear_console

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

