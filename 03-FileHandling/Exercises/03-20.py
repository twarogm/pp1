allnums = []
with open('numbers.txt') as file:
    for line in file:
        if int(line)%2==0:
            allnums.append(line)

with open('evennumbers.txt', 'w') as file:
    for i in allnums:
        file.write(i)