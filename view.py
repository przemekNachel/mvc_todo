class View:

    def __init__(self):

        self.interfaces = {
            "main": "1. Display ToDo list\n2. Add ToDo item\n0. Quit",
            "list": "0. Back",
            "details": "6. Mark\n7. Change name\n8. Change description\n9. Delete\n0. Back to main menu",
            "add_title": "Type name of ToDo item (Max 20 characters)...",
            "add_description": "Describe ToDo item (Max 150 characters)..."
        }

    def clear(self):

        print(chr(27) + "[2J")

    def print_interface(self, name, data_to_show=None, ID=None):

        self.clear()
        if data_to_show:
            if type(data_to_show) == list:
                for item in data_to_show:
                    print(str(data_to_show.index(item) + 1) + ". " + item.name)
            else:
                print(ID + ".", data_to_show)
        print(self.interfaces[name])
