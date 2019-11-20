def transpozycja(macierz):
    print('Macierz:')
    for i in macierz:
        print()
        for j in i:
            print(j, end = ' ')
    print('\nMacierz transponowana: ')
    for j in range(3):
        print()
        for i in macierz:
            print(i[j], end=' ')
    


mac = [[1,2,0], [0,0,3], [5,1,1]]
transpozycja(mac)