i=1
x=0
count=0

while i>0:
    y=int(input("Podaj liczbę: "))
    if y==0:
        break
    else:
        x=x+y
        count+=1
        
print(f"Liczb={count}, Suma={x}, Średnia={x/count}")