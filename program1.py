#1. Numbers divisible by 7 but not by 3
for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        print(i, end=",")