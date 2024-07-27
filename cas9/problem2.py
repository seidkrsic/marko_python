def koliko_parnih(n):
    if n == 0:
        return 0
    else:
        if (n % 10) % 2 == 0:
            return 1 + koliko_parnih(n // 10)
        else:
            return 0 + koliko_parnih(n // 10)



print(koliko_parnih(123))