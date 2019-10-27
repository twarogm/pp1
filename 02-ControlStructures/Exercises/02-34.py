PESEL=input("Podaj nr PESEL: ")
wiek=2019-1900-int(PESEL[:2])
if int(PESEL[9])%2==0:
    płeć="Żeńska"
elif int(PESEL[9])%2!=0:
    płeć="Męska"
print(f"PESEL: {PESEL}",f"Płeć: {płeć}",f"Wiek: {wiek}")
