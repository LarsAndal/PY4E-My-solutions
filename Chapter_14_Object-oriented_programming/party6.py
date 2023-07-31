"""Example from the book."""

from party import PartyAnimal  # pylint: disable=E0401


class CricketFan(PartyAnimal):  # noqa; pylint: disable=C0115.R0903
    points = 0

    def six(self):  # noqa; pylint:disable=C0116
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
