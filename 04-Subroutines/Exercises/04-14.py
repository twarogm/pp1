def wystepuje(liczba, tablica):
    for i in tablica:
        if i==liczba:
            print(f'Tablica: {tablica}')
            print(f'Liczba: {liczba}')
            print('Podana liczba występuje w tablicy')

wystepuje(23, [15, 38, 7, 23, 14])
        