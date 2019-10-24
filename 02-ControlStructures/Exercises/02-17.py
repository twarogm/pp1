sumap=0
sumanp=0
for i in range(1,51):
    if i%2==0:
        sumap+=i
    else:
        sumanp+=i
print(f"Suma liczb nieparzystych w przedziale [1,50] wynosi {sumanp}, a liczb parzystych {sumap}")

    