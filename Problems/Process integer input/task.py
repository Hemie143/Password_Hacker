num_list = []
while True:
    num = int(input())
    if num > 100:
        break
    if num >= 10:
        num_list.append(str(num))
print('\r\n'.join(num_list))
