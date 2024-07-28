import random


def sequencial_search(data, value_to_search):
    found = 0
    i = 0

    while (i < len(data)) and (found == 0):
        if data[i] == value_to_search:
            found = 1
        else:
            i = i + 1

    if found == 1:
        return i + 1
    else:
        return -1


random_data = random.sample(range(10), 10)
print(random_data)

value = int(input('Value: '))

has_found = sequencial_search(random_data, value)

if has_found == -1:
    print('Value not found')
else:
    print('Value found at position', has_found)
