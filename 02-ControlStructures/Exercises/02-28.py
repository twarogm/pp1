a=int(input("Wprowadź długość boku a: "))
b=int(input("Wprowadź długość boku b: "))
for i in range(1,a+1):
    if i==1:
        print("*"*b)
    elif i>=2 and i<a:
        print("*"+" "*(b-2)+"*")
    elif i==a:
        print("*"*b)
        