x=0
while x>=0:
    if x%7==0 and x%2==1 and x%3==1 and x%4==1 and x%5==1 and x%6==1:
        print(f"Liczba podzielna przez 7 oraz dająca resztę 1 przy dzieleniu przez 2,3,4,5,6 to {x}")
        break
    x+=1