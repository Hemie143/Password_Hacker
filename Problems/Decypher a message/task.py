cipher = input()
key = int(input())
shift = sum((key).to_bytes(2, byteorder='little'))
text = ''.join([chr(ord(c) + shift) for c in cipher])
print(text)
