def find_and_return_odd_repeating_number(input_list):
    odd_repeating_number = None
    counts = {}
    index = 0

    while index < len(input_list):
        current_number = input_list[index]
        if current_number in counts:
            counts[current_number] += 1
        else:
            counts[current_number] = 1
        index += 1

    for number, count in counts.items():
        if count % 2 != 0:
            odd_repeating_number = number
            continue

    return odd_repeating_number

list = [1, 3, 6, 4, 2, 4, 3, 2, 6]

result = find_and_return_odd_repeating_number(list)
print(result)