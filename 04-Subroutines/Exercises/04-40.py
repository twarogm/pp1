def fil(tab):
    even = filter(lambda x: x%2 == 0, tab)
    print('Liczby parzyste: ')
    print(list(even), end=', ')

tab = [1,2,3,4,5,6,7,8,9]

fil(tab)