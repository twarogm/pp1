def potega(x,n):
    if n == 0:
        return 1    
    if n > 0:
        return x*potega(x,n-1)

print(f'5 do potęgi 3 wynosi: {potega(5,3)}')