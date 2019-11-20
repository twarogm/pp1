def suma(nat):
    s = 0
    for i in str(nat):
        s += int(i)
    return s

N = int(input('Podaj liczbę naturalną: '))
print(f'Suma cyfr liczby naturalnej: {suma(N)}')
