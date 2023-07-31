"""Example from the book."""


class PartyAnimal:  # noqa; pylint: disable=C0115
    x = 0

    def __init__(self):  # noqa
        print("I am constructed")

    def party(self):  # noqa; pylint: disable=C0116
        self.x = self.x + 1  # pylint: disable=C0103
        print("So far", self.x)

    def __del__(self):  # noqa
        print("I am destructed", self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42  # pylint: disable=C0103
print("an contains", an)
