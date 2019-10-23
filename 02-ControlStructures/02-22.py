suma = 0
tablica = [15,8,31,47,2,19]
n = 0
for i in tablica:
    if i%2!=0:
        suma+=i
        n+=1
print(f"Średnia arytmetyczna liczb nieparzystych wynosi: {suma/n}")
    