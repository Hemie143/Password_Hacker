import itertools

for first, middle in itertools.product(first_names, middle_names):
    print(f'{first} {middle}')
