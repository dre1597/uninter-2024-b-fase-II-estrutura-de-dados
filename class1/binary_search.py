import random


def binary_search(start, end, data, value_to_search):
    while start <= end:
        middle = int((start + end) / 2)

        if data[middle] == value_to_search:
            return middle
        elif data[middle] < value_to_search:
            start = middle + 1
        else:
            end = middle - 1

    return -1


random_data = random.sample(range(10), 10)
print(random_data)

value = int(input('Value: '))

has_found = binary_search(0, len(random_data) - 1, random_data, value)
