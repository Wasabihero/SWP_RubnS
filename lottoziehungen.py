import random

def zieheLottozahlen():
    zahlen = random.sample(range(1, 46), 6)
    return zahlen;

def simuliereZiehungen(anzahl):
    ergebnisse = {}
    for i in range(1, 46):
        ergebnisse[i] = 0;

    for x in range(anzahl):
        ziehung = zieheLottozahlen();


        for zahl in ziehung:
            ergebnisse[zahl] = ergebnisse[zahl] + 1
    return ergebnisse;


def ausgabeErgebnisse(ergebnisse):

    print("Lotto-Auswertung nach Simulation:")
    print("---------------------------------")

    for zahl in range(1, 46):
        haeufigkeit = ergebnisse[zahl]
        print(f"Zahl {zahl:2d}: {haeufigkeit} mal")


def main():

    anzahlZiehungen = 1000
    ergebnisse = simuliereZiehungen(anzahlZiehungen)
    ausgabeErgebnisse(ergebnisse)


# Programmstart
if __name__ == "__main__":
    main()
