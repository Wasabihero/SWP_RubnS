names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

personen = zip(names, ages, scores)

gefiltert = filter(lambda p: p[1] >= 18 and p[2] >= 80, personen)

result = list(map(lambda p: {"name": p[0], "age": p[1], "score": p[2]}, gefiltert))

print(result)

