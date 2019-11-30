def czytajWspolczynniki():
    a = float(input('Wprowadź współczynnik "a": '))
    b = float(input('Wporwadź współczynnik "b": '))
    c = float(input('Wprowadź współczynnik "c": '))
    wspolczynniki = [a,b,c]
    return wspolczynniki

def obliczDelte(wspolczynniki):
    delta = wspolczynniki[1]**2 - 4*wspolczynniki[0]*wspolczynniki[2]
    return delta

def obliczPierwiastki(wspolczynniki, delta):
    from math import sqrt
    if delta > 0:
        x1 = (-(wspolczynniki[1])-(sqrt(delta))/(2*wspolczynniki[0]))
        x2 = (-(wspolczynniki[1])+(sqrt(delta))/(2*wspolczynniki[0]))
        pierwiastki = [x1, x2]
    elif delta == 0:
        x1 = (-wspolczynniki[1])/2*wspolczynniki[0]
        pierwiastki = [x1]
    elif delta < 0:
        pierwiastki = []
    return pierwiastki

def wyswietlPierwiastki(wspolczynniki, delta, pierwiastki):
    if wspolczynniki[1] > 0 and wspolczynniki[2] > 0:
        print(f'Równanie kwadratowe {wspolczynniki[0]}x^2+{wspolczynniki[1]}x+{wspolczynniki[2]}')
    if wspolczynniki[1] > 0 and wspolczynniki[2] < 0:
        print(f'Równanie kwadratowe {wspolczynniki[0]}x^2+{wspolczynniki[1]}x{wspolczynniki[2]}')
    if wspolczynniki[1] < 0 and wspolczynniki[2] < 0:
        print(f'Równanie kwadratowe {wspolczynniki[0]}x^2{wspolczynniki[1]}x{wspolczynniki[2]}')
    if wspolczynniki[1] < 0 and wspolczynniki[2] > 0:
        print(f'Równanie kwadratowe {wspolczynniki[0]}x^2{wspolczynniki[1]}x+{wspolczynniki[2]}')
    
    if delta > 0:
        print(f'Pierwiastki równania: x1 = {pierwiastki[0]}, x2 = {pierwiastki[1]}.')
    if delta == 0:
        print(f'Pierwiastek równania x = {pierwiastki[0]}.')
    if delta < 0:
        print(f'Brak pierwiastków równania.')