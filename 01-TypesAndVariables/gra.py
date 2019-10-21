import random
kostka = ["1","2","3","4","5","6"]
nr = (random.choice(kostka))
traf = input("Podaj ile wyrzucił komputer ")
print(f"Komputer wyrzucił: {nr}")
print(f"Zgadłeś: {nr is traf}")