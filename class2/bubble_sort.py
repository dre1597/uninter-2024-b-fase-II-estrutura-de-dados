def bubble_sort(data):
    length = len(data)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


data = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort(data))
