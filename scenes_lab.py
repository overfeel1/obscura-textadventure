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

