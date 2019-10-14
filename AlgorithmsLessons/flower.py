class Flower:

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def update_name(self, up_name):

        self._name = up_name

    def retrieve_name(self):
        return self._name

    def updat