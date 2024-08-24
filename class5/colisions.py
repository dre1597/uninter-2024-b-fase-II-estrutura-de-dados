def linear_try(k, n, pos, hash_table):
    guess = pos
    while hash_table[guess] is not None:
        guess += 1
        if guess == n:
            guess = 0
        if guess == pos:
            guess = -1
            break
    return guess

def linear_try_del(k,n,pos,hash_table):
    guess = pos
    while (hash_table[guess] is not None) and (hash_table[guess] != k):
        guess += 1
        if guess == n:
            guess = 0
        if guess == pos:
            guess = -1
            break
    return guess
