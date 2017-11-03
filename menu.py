class MenuView:

    def __init__(self):
        self.main_menu_positions = [
            "1. Add ToDo item",
            "2. Modify item",
            "3. Delete item",
            "4. Mark item as done",
            "5. Display items' list",
            "6. Display specific todo item's details",
            "0. Quit"
        ]

    def main_menu(self):
        self.clear()
        for position in self.main_menu_positions:
            print(position)

    def clear(self):
        print(chr(27) + "[2J")


class MenuControl:

    def __init__(self):
        menu_selection = None

    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

