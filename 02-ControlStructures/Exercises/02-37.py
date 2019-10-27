import statistics

l1=float(input("Wprowadź pierwszą liczbę: "))
l2=float(input("Wprowadź drugą liczbę: "))
l3=float(input("Wprowadź trzecią liczbę: "))

liczby=[l1,l2,l3]

print(f"Mediana wynosi {statistics.median(liczby)}")

