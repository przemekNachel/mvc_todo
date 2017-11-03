from todo_item import TodoItem
from menu import *


def main():
    menu_view = MenuView()
    menu_control = MenuControl()
    while True:
        menu_view.main_menu()

if __name__ == "__main__":
    main()