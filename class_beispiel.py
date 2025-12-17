# ==========================================
# Thema: Tiere und Haustiere
# Demonstration von Vererbung, self und super()
# ==========================================


class Tier:
    """
    Basisklasse für alle Tiere.
    Enthält Eigenschaften und Verhalten,
    die alle Tiere gemeinsam haben.
    """

    def __init__(self, name, alter):
        # self verweist auf das aktuelle Objekt
        # (das konkrete Tier, das gerade erstellt wird)
        self.name = name
        self.alter = alter

    def statusAnzeigen(self):
        """
        Gibt allgemeine Informationen zum Tier aus.
        """
        print(f"Name: {self.name}, Alter: {self.alter}")

    def geraeuschMachen(self):
        """
        Standardmethode, die von Unterklassen
        überschrieben wird.
        """
        print("Das Tier macht ein Geräusch.")


class Hund(Tier):
    """
    Unterklasse von Tier.
    Repräsentiert einen Hund.
    """

    def __init__(self, name, alter, rasse):
        # super() ruft den Konstruktor (__init__)
        # der Basisklasse Tier auf
        # Dadurch werden name und alter dort gesetzt
        super().__init__(name, alter)

        # Eigenes Attribut der Unterklasse Hund
        self.rasse = rasse

    def geraeuschMachen(self):
        # Zugriff auf Attribute dieses konkreten Objekts
        # über self
        print(f"{self.name} bellt: Wuff!")


class Katze(Tier):
    """
    Unterklasse von Tier.
    Repräsentiert eine Katze.
    """

    def __init__(self, name, alter, lieblingsSpielzeug):
        # Aufruf des Konstruktors der Basisklasse Tier
        super().__init__(name, alter)

        self.lieblingsSpielzeug = lieblingsSpielzeug

    def geraeuschMachen(self):
        print(f"{self.name} miaut: Miau!")


class Vogel(Tier):
    """
    Unterklasse von Tier.
    Repräsentiert einen Vogel.
    """

    def geraeuschMachen(self):
        # Kein eigener Konstruktor nötig,
        # daher wird automatisch der der Basisklasse genutzt
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
