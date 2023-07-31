"""Example from the book."""


class PartyAnimal:  # noqa; pylint: disable=C0115.R0903
    x = 0
    name = ""

    # trunk-ignore(codespell/misspelled)
    def __init__(self, nam):  # noqa
        # trunk-ignore(codespell/misspelled)
        self.name = nam
        print(self.name, "constructed")

    def party(self):  # noqa; pylint: disable=C0116
        self.x = self.x + 1  # pylint: disable=C0103
        print(self.name, "party count", self.x)
