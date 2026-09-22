days = int(input())

count = 0

while 2 ** (count + 1) <= days:
    count = count + 1

print(2 ** count * 100)