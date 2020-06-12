class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @property
    def on_take(self):
        return f'You have picked up {self.name}'
