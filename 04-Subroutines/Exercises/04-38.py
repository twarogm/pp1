def upcase():
    signs = input('Wprowadź ciąg znaków: ')
    upper = ('')
    for i in signs:
        if str.isupper(i) == True:
            upper += (i)
    print(upper)


upcase()

    
