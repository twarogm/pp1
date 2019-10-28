i=1
with open('NoEducation.txt','r') as file:
    for line in file:        
        print(i, line, end='')
        i+=1
