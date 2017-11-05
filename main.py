from view import View
from item import TodoItem


class ToDo:

    def __init__(self):

        self.todo_list = []
        self.view = View()

    def getch(self):

        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def add_item(self):

        todo_name = self.get_name_or_description()
        todo_details = self.get_name_or_description(False)
        self.todo_list.append(TodoItem(todo_name, todo_details))

    def get_name_or_description(self, name=True):

        while True:
            if name:
                self.view.print_interface("add_title")
                text = input()
                if len(text) <= 20:
                    return text
            else:
                self.view.print_interface("add_description")
                text = input()
                if len(text) <= 150:
                    return text

    def control_todo_list(self):

        self.view.print_interface("list", self.todo_list)
        while True:
            selection = self.getch()
            if selection == "0":
                break
            if selection in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if 0 < int(selection) <= len(self.todo_list):
                    self.control_item(self.todo_list[int(selection) - 1], selection)
                    break

    def control_item(self, item, ID):

        self.view.print_interface("details", item, ID)
        while True:
            details_selection = self.getch()
            if details_selection == "6":
                item.marked = True
                item.mark()
                break
            if details_selection == "7":
                self.view.print_interface("add_title")
                item.name = self.get_name_or_description()
                item.mark()
                break
            if details_selection == "8":
                self.view.print_interface("add_description")
                item.description = self.get_name_or_description(False)
                break
            if details_selection == "9":
                self.todo_list.remove(item)
                break
            if details_selection == "0":
                break

    def main(self):

        while True:
            self.view.print_interface("main")
            selection = self.getch()
            if selection == "0":
                break
            elif selection == "1":
                self.control_todo_list()
            elif selection == "2":
                self.add_item()

if __name__ == "__main__":
    ToDo().main()
