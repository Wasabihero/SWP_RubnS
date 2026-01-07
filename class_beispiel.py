# ==========================================
# Thema: Tiere und Haustiere
# Vererbung mit self und super()
# ==========================================

class Tier:
    """
    Basisklasse für alle Tiere.
    """

    def __init__(self, name, alter):
        # Attribute des Objekts
        self.name = name
        self.alter = alter

    def statusAnzeigen(self):
        # Gibt Basisdaten aus
        print(f"Name: {self.name}, Alter: {self.alter}")

    def geraeuschMachen(self):
        # Standardverhalten
        print("Das Tier macht ein Geräusch.")


class Hund(Tier):
    """
    Unterklasse von Tier.
    """

    def __init__(self, name, alter, rasse):
        # Konstruktor der Basisklasse
        super().__init__(name, alter)

        self.rasse = rasse

    def geraeuschMachen(self):
        # Erweitert das Verhalten der Basisklasse
        super().geraeuschMachen()
        print(f"{self.name} bellt: Wuff!")


class Katze(Tier):
    """
    Unterklasse von Tier.
    """

    def __init__(self, name, alter, lieblingsSpielzeug):
        super().__init__(name, alter)
        self.lieblingsSpielzeug = lieblingsSpielzeug

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

katze.statusAnzeigen()
katze.geraeuschMachen()

vogel.statusAnzeigen()
vogel.geraeuschMachen()
