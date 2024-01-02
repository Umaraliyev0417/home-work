def process_list(input_list):
    input_number = int(input("Son: "))
    if input_number in input_list:
        input_list.remove(input_number)
        input_list.append(input_number)
        print(my_list)
    else:
        print("Xato!")

my_list = [3, 6, 9, 12, 15,]
process_list(my_list)