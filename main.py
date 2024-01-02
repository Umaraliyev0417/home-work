son = int(input("Son kiriting: "))
x = 1
while x <= son:
    num = 2 ** x
    if son >= num:
        print(x, num)
    x += 1