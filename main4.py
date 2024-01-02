list = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2]
def find_occur(list):
    i = 0
    while i < len(list):
        count = list.count(list[i])
        if count == 1:
            i += 1
        return count
print(find_occur(list))