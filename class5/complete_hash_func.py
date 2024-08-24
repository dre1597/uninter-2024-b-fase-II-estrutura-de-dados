def hash_func (k, n):
    return k % n

def hash_func_variation(k, n):
    k = list(k)
    return (ord(k[0]) + ord(k[1])) % n

n = 10
hash_table = [None] * n

while True:
    print('1 - Insert')
    print('2 - Remove')
    print('3 - List')
    print('4 - Exit')

    option = int(input("Choice: "))

    if option == 1:
        key = input('Key: ')
        pos = hash_func_variation(key, n)
        if hash_table[pos] is None:
            hash_table.insert(pos, key)
        else:
            print('Collision')
    elif option == 2:
        key = input('Key: ')
        pos = hash_func(key, n)
        if hash_table[pos] == key:
            hash_table.pop(pos)
        else:
            print('Key not found')
    elif option == 3:
        print(hash_table)
    elif option == 4:
        print('Bye')
        break
    else:
        print('Invalid option')
