arr = [21, 19, 6, 12, 23, 16, 21, 8, 31, 6, 25, 30, 10, 9, 3, 13, 31, 19, 15, 15]
dlina = len(arr)
for i in range(dlina-1):
    chislo = arr[i]
    if chislo % 4 == 0:
        print("не подходит")
    elif chislo % 6 == 0:
        print("идеальный!")
    elif chislo % 4 == 0 and chislo % 6 == 0:
        print("жесть...")
    elif chislo % 4 != 0 and chislo % 6 != 0:
        print("норм")