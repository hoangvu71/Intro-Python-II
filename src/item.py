class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @property
    def on_take(self):
        return f'-----------------------------\nYou have picked up {self.name}'

    @property
    def on_drop(self):
        return f'-----------------------------\nYou have dropped {self.name}'

