"""Example from the book."""


class PartyAnimal:  # noqa, pylint: disable=C0115,R0903
    x = 0

    def party(self):  # noqa, pylint: disable=C0116
        self.x = self.x + 1  # pylint: disable=C0103
        print("So far", self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
