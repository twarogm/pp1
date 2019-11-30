from dane import pobierzDane
from obliczenia import srednia, mediana, maksimum, minimum

dane = pobierzDane()
miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiećeń', 'Maj', 'Czerwiec']


def pokazWyniki():
    print('RAPORT Z WYDATKÓW')
    print(f'%s %12s'%('MIESIAC', 'WYDATKI'))
    for i in range(len(miesiace)):
        print(f'%-8s %11s'%(miesiace[i], '%.2f'%dane[i]))
    
    print('\nSTATYSTYKA WYDATKÓW')
    statystyki = ['Średnia:', 'Mediana:', 'Maksimum:', 'Minimum:']
    wartoscistat = [srednia(), mediana(), maksimum(), minimum()]
    for i in range(len(wartoscistat)):
        print(f'%-9s %10s'%(statystyki[i], '%.2f'%wartoscistat[i]))

def pokazWykres():
    print('\nGRAFICZNA REPREZENTACJA WYDATKÓW')
    for i in range(len(miesiace)):
        graph = ('#'*(int(dane[i])//100))
        print(f'%-9s %-4s'%((str(miesiace[i])+':'), graph))

pokazWyniki()
pokazWykres()