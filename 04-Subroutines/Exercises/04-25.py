imie = input('Podaj imie: ')
def jestimie(imie, imiona):
        if imie in imiona:
            print(f'Podane imie: {imie}')
            print(f'Imiona: {imiona}')
            print('Rezultat: Imie znajduje sie w wykazie.')    
        else:
            print(f'Podane imie: {imie}')
            print(f'Imiona: {imiona}')
            print('Rezultat: Imie nie znajduje sie w wykazie.') 
             

jestimie(imie, ['Janek', 'Ania', 'Wojtek', 'Zosia'])