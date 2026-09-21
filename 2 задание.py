days = int(input())
count = 1
while 2**count < days:
    count = count +1
count = count - 1
print(2**count * 100)

