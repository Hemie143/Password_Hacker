import itertools

for i in range(1, 4):
    for bouquet in itertools.combinations(flower_names, i):
        print(bouquet)
