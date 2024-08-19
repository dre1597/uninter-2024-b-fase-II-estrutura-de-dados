queue = []
length = 5

while True:
    print('1 - Insert')
    print('2 - Remove')
    print('3 - List')
    print('4 - Exit')

    option = int(input("Choice: "))

    if option == 1:
        data = int(input('Value: '))
        if len(queue) < length:
            queue.append(data)
        else:
            print('Queue is full')
    if option == 2:
        if len(queue) > 0:
            queue.pop(0)
        else:
            print('Queue is empty')
    if option == 3:
        for item in queue:
            print(item, end=' ')
        print('\n')
    if option == 4:
        print('Bye')
        break
    else:
        print('Invalid option')
