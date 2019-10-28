suma=0
with open('numbers.txt') as file:
    for line in file:
        suma+=int(line)
print(f'Suma: {suma}')