n=(int(input("Podaj ilość liczb pierwszych: ")))
pierwsza = []
count=0
prop=1
while prop>0:
    prop+=1
    isPierw = True
    for num in range(2, prop):
        if prop%num==0:
            isPierw=False
      
    if isPierw:
        pierwsza.append(prop)
        count+=1
        if count==n:
            break
        
print(pierwsza)