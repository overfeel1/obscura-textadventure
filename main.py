from game.menu import show_start_menu
from game.engine import run_game

if __name__ == "__main__":
    status = show_start_menu()
    if status == "start":
        run_game()

