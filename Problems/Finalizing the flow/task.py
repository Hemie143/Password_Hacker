entry = input()
if entry.count(' ') == 1:
    name, surname = entry.split()
    print(f'Welcome to our party, {name} {surname}')
else:
    print('You need to enter exactly 2 words. Try again!')
print('You will be more than welcome!')
