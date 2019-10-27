limit=int(input("Podaj limit prędkości (w km/h): "))
v=int(input("Podaj prędkość (w km/h): "))

if v<limit:
    print("Brak mandatu")
elif v>limit and v-limit<=10:
    roznica=v-limit
    mandat=roznica * 5
    print(f"Mandat wynosi: {mandat} zł")
elif v>limit and v-limit>10:
    roznica=v-limit
    mandat=roznica*5
    mandat2=(roznica-10)*10
    mandat3=mandat+mandat2
    print(f"Mandat wynosi: {mandat3} zł")