"""Example from the book."""


class PartyAnimal:  # noqa; pylint: disable=C0115,R0903
    x = 0

    def party(self):  # noqa; pylint: disable=C0116
        self.x = self.x + 1  # pylint: disable=C0103
        print("So far", self.x)


an = PartyAnimal()
print("Type", type(an))
print("Dir ", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))
