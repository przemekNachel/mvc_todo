class TodoItem:

    def __init__(self, name, description):

        self.name = name
        self.description = description
        self.is_done = False
        self.marked = False

    def mark(self):

        if self.marked:
            self.name = '\033[94m' + self.name + '\033[0m'

    def __str__(self):

        return self.name + "\n" + self.description + "\n"
