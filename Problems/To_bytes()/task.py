num = int(input())
num = (num).to_bytes(2, byteorder='little')
print(sum(num))