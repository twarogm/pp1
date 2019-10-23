wiekpsa = int(input("Podaj wiek psa: "))
if wiekpsa<=2:
    wiekpsalud = wiekpsa*(10.5)
elif wiekpsa>2:
    wiekpsalud = ((10.5*2)+(wiekpsa-2)*4)
print(f"Wiek psa w psich latach: {wiekpsalud}")
