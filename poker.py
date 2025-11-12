import random


# ---------------- Hauptprogramm ----------------
def main():
    """
    Simuliert 100000 Pokerhände und berechnet die
    Häufigkeit und den prozentualen Anteil der Kombinationen.
    """
    totalGames = 100000
    results = simulateGames(totalGames)

    print(f"\nSimulation von {totalGames} Pokerhänden:")
    print("========================================")

    for combination, count in sorted(results.items(),
                                     key=lambda x: -x[1]):
        percent = (count / totalGames) * 100
        print(f"{combination:20s}: {count:8d}  ({percent:6.4f}%)")


# ---------------- Simulation ----------------
def simulateGames(gameCount):
    """
    Führt mehrere Poker-Spiele durch und zählt die Kombinationen.
    """
    combinations = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Four of a Kind": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Three of a Kind": 0,
        "Two Pair": 0,
        "One Pair": 0,
        "High Card": 0
    }

    for _ in range(gameCount):
        hand = drawUniqueValues(52, 5)
        combo = detectCombination(hand)
        combinations[combo] += 1

    return combinations


# ---------------- Hilfsfunktionen ----------------
def drawUniqueValues(poolSize, drawCount):
    """
    Zufällige eindeutige Zahlen aus Bereich [0, poolSize)
    ziehen (swap-to-end-Verfahren).
    """
    pool = list(range(poolSize))
    results = []

    for i in range(drawCount):
        index = random.randint(0, poolSize - 1 - i)
        results.append(pool[index])
        pool[index], pool[poolSize - 1 - i] = (
            pool[poolSize - 1 - i],
            pool[index]
        )
    return results


def getRanks(hand):
    """Gibt eine Liste der Kartenwerte (0–12) zurück."""
    return [card % 13 for card in hand]


def getSuits(hand):
    """Gibt eine Liste der Farben (0–3) zurück."""
    return [card // 13 for card in hand]


def countRanks(hand):
    """Zählt, wie oft jeder Kartenwert vorkommt."""
    counts = {}
    for rank in getRanks(hand):
        counts[rank] = counts.get(rank, 0) + 1
    return counts


def isPair(hand):
    """True, wenn genau ein Paar vorhanden ist."""
    return list(countRanks(hand).values()).count(2) == 1


def isTwoPair(hand):
    """True, wenn zwei verschiedene Paare vorhanden sind."""
    return list(countRanks(hand).values()).count(2) == 2


def isThreeOfKind(hand):
    """True, wenn ein Drilling vorhanden ist."""
    return 3 in countRanks(hand).values()


def isFourOfKind(hand):
    """True, wenn ein Vierling vorhanden ist."""
    return 4 in countRanks(hand).values()


def isFullHouse(hand):
    """True, wenn Drilling + Paar."""
    values = countRanks(hand).values()
    return 3 in values and 2 in values


def isFlush(hand):
    """True, wenn alle Karten die gleiche Farbe haben."""
    suits = getSuits(hand)
    return len(set(suits)) == 1


def isStraight(hand):
    """True, wenn fünf aufeinanderfolgende Werte."""
    ranks = sorted(getRanks(hand))
    # Ass kann auch niedrig sein (A,2,3,4,5)
    if ranks == [0, 1, 2, 3, 12]:
        return True
    return all(ranks[i] + 1 == ranks[i + 1] for i in range(4))


def isStraightFlush(hand):
    """True, wenn gleichzeitig Straight und Flush."""
    return isStraight(hand) and isFlush(hand)


def isRoyalFlush(hand):
    """True, wenn 10–Ass der gleichen Farbe."""
    ranks = sorted(getRanks(hand))
    return isFlush(hand) and ranks == [8, 9, 10, 11, 12]


def detectCombination(hand):
    """
    Ermittelt die Poker-Kombination der Hand.
    """
    if isRoyalFlush(hand):
        return "Royal Flush"
    if isStraightFlush(hand):
        return "Straight Flush"
    if isFourOfKind(hand):
        return "Four of a Kind"
    if isFullHouse(hand):
        return "Full House"
    if isFlush(hand):
        return "Flush"
    if isStraight(hand):
        return "Straight"
    if isThreeOfKind(hand):
        return "Three of a Kind"
    if isTwoPair(hand):
        return "Two Pair"
    if isPair(hand):
        return "One Pair"
    return "High Card"


# ---------------- Programmstart ----------------
if __name__ == "__main__":
    main()
