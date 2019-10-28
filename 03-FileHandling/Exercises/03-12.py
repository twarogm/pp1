with open('shoppinglist.txt', 'a') as file:
    while True:
        produkt=input('Wprowadź nazwę produktu: ')
        if produkt=='':
            break
        else:
            file.write(f'{produkt}\n')
