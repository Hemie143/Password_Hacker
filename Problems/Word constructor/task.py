word1 = input()
word2 = input()
print(''.join(f'{c1}{c2}' for c1, c2 in zip(word1, word2)))
