stack = []
length = 5

while True:
    print('1 - Insert')
    print('2 - Remove')
    print('3 - List')
    print('4 - Exit')

    option = int(input("Choice: "))

    if option == 1:
        data = int(input('Value: '))
        if len(stack) < length:
            stack.append(data)
        else:
            print('Stack is full')
    if option == 2:
        if len(stack) > 0:
            stack.pop()
        else:
            print('Stack is empty')
    if option == 3:
        stack.reverse()
        for item in stack:
            print(item)
    if option == 4:
        print('Bye')
        break
    else:
        print('Invalid option')
