import random

def losowa():
    return random.randrange(1,51)

base = []
par = []
niepar = []

for i in range(1,1001):
    base.append(losowa())

for j in base:
    if j%2 == 0:
        par.append(j)
    else:
        niepar.append(j)

print('Dla 1000 losowych liczb z przedziału <1,50>:')
print(f'Liczby parzyste stanowią: {len(par)/10}%')
print(f'Liczby nieparzyste stanowią: {len(niepar)/10}%')



