def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        left = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


data = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(data))
