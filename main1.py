list = [30, 50, 70, 98, 102, 130]
def foiz(list):
    f = 100
    index = 0
    inp = int(input("Son: "))
    while index < len(list):
        current_number = list[index]
        m = current_number / f * inp
        print(m)
        index += 1
foiz(list)