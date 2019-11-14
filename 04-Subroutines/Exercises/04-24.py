def miesiąc(n):
    nazwy = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    if n > 0 and n < 13:
        return nazwy[n-1]
    else:
        return 'Błąd'
print(miesiąc(7), miesiąc(9))