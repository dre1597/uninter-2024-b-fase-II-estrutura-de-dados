def recursive_fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        return n * recursive_fatorial(n - 1)


def fatorial(n):
    fat = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return fat
    else:
        for i in range(2, n + 1):
            fat *= i
        return fat


n = int(input('Fatorial: '))
print(recursive_fatorial(n))
print(fatorial(n))
