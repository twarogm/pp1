def isInside():
    n = int(input('Wprowadź n: '))
    x = int(input('Wprowadź x: '))
    y = int(input('Wprowadź y: '))
    
    if n >= x:
        if n <= y:
            print(f'Liczba {n} znajduje się w przedziale <{x},{y}>.')
        else:
            print(f'Liczba {n} nie znajduje się w przedziale <{x},{y}>.')
    else:
        print(f'Liczba {n} nie znajduje się w przedziale <{x},{y}>.')

    
isInside()