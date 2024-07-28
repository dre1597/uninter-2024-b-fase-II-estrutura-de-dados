def merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data


data = [6, 5, 3, 1, 8, 7, 2, 4]
print(merge_sort(data))
