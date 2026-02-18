# ==========================================
# Thema: Tiere und Haustiere
# Vererbung mit self und super()
# ==========================================

class Tier:
    """
    Basisklasse für alle Tiere.
    """

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}"

    def statusAnzeigen(self):
        """
        Gibt den Status des Tieres aus.
        """
        print(self)

    def geraeuschMachen(self):
        """
        Standardverhalten für Tiere.
        """
        print("Das Tier macht ein Geräusch.")


class Hund(Tier):
    """
    Unterklasse von Tier.
    """

    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)
        self.rasse = rasse

    def __str__(self):
        return (
            f"Name: {self.name}, Alter: {self.alter}, "
            f"Rasse: {self.rasse}"
        )

    def geraeuschMachen(self):
        super().geraeuschMachen()
        print(f"{self.name} bellt: Wuff!")


class Katze(Tier):
    """
    Unterklasse von Tier.
    """

    def __init__(self, name, alter, lieblingsSpielzeug):
        super().__init__(name, alter)
        self.lieblingsSpielzeug = lieblingsSpielzeug

    def __str__(self):
        return (
            f"Name: {self.name}, Alter: {self.alter}, "
            f"Lieblingsspielzeug: {self.lieblingsSpielzeug}"
        )

    def geraeuschMachen(self):
        print(f"{self.name} miaut: Miau!")


class Vogel(Tier):
    """
    Unterklasse von Tier.
    """

    def geraeuschMachen(self):
        print(f"{self.name} zwitschert: Piep!")


# ==========================================
# Testbereich
# ==========================================

hund = Hund("Bello", 5, "Labrador")
katze = Katze("Minka", 3, "Ball")
vogel = Vogel("Tweety", 1)

hund.statusAnzeigen()
hund.geraeuschMachen()

print()

katze.statusAnzeigen()
katze.geraeuschMachen()

print()

vogel.statusAnzeigen()
vogel.geraeuschMachen()
