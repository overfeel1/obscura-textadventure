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
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:',.<>?/\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        clear_console()
        for _ in range(height):
            line = ''.join(random.choice(chars) for _ in range(width))
            print(line)
        time.sleep(interval)

