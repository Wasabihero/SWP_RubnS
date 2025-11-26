import random


def main():
    # Vergleichswerte aus dem Internet in %
referenceOdds = {
    "Royal Flush": 0.000154,
    "Straight Flush": 0.00139,
    "Four of a Kind": 0.0240,
    "Full House": 0.1441,
    "Flush": 0.1965,
    "Straight": 0.3925,
    "Three of a Kind": 2.1128,
    "Two Pair": 4.7539,
    "One Pair": 42.2569,
    "High Card": 50.1177
}
    totalGames = 100000
    results = simulateGames(totalGames)

    print(f"\nSimulation von {totalGames} Pokerhänden:")
    print("========================================\n")

    items = list(results.items())
    items.sort(key=countSort, reverse=True)

    for combination, count in items:
        percent = (count / totalGames) * 100
        ref = referenceOdds[combination]
        difference = percent - ref

        print(f"{combination:20s}: {count:8d}  "
              f"({percent:7.4f}% | ref {ref:7.4f}% | "
              f"Δ {difference:+7.4f}%)")

def countSort(entry):
    return entry[1]


# ---------------- Simulation ----------------
def simulateGames(gameCount):
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
    pool = list(range(poolSize))
    results = []

    for i in range(drawCount):
        index = random.randint(0, poolSize - 1 - i)
        results.append(pool[index])
        pool[index], pool[poolSize - 1 - i] = (
            pool[poolSize - 1 - i], pool[index]
        )
    return results


def getRanks(hand):
    return [card % 13 for card in hand]


def getSuits(hand):
    return [card // 13 for card in hand]


def countRanks(hand):
    counts = {}
    for rank in getRanks(hand):
        counts[rank] = counts.get(rank, 0) + 1
    return counts


def isPair(hand):
    return list(countRanks(hand).values()).count(2) == 1


def isTwoPair(hand):
    return list(countRanks(hand).values()).count(2) == 2


def isThreeOfKind(hand):
    return 3 in countRanks(hand).values()


def isFourOfKind(hand):
    return 4 in countRanks(hand).values()


def isFullHouse(hand):
    values = countRanks(hand).values()
    return 3 in values and 2 in values


def isFlush(hand):
    suits = getSuits(hand)
    return len(set(suits)) == 1


def isStraight(hand):
    ranks = sorted(getRanks(hand))
    # ternärer Operator anstelle von if/else
    return True if ranks == [0, 1, 2, 3, 12] \
        else all(ranks[i] + 1 == ranks[i + 1] for i in range(4))


def isStraightFlush(hand):
    return isStraight(hand) and isFlush(hand)


def isRoyalFlush(hand):
    ranks = sorted(getRanks(hand))
    return isFlush(hand) and ranks == [8, 9, 10, 11, 12]


def detectCombination(hand):
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
