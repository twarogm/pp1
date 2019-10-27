import math

print("Wyznaczanie pierwiastków równania kwadratowego.")
a=int(input("Wprowadź wartośc 'a' równania kwadratowego: "))
b=int(input("Wprowadź wartośc 'b' równania kwadratowego: "))
c=int(input("Wprowadź wartośc 'c' równania kwadratowego: "))

delta=b**2-4*a*c
if delta>0:
    sqrt=math.sqrt(delta)
    x1=(-b-(sqrt))/(2*a)
    x2=(-b+(sqrt))/(2*a)
    print(f"Pierwiastki równania kwadratowego wynoszą: x1={x1}, x2={x2}")
elif delta==0:
    x0=(-b)/(2*a)
    print(f"Pierwiastek równania kwadratowego wynoi: x0={x0}")
elif delta<0:
    print("Równanie kwadratowe nie ma pierwiastków")



