with open('students.txt') as file:
    for line in file:
        sepline = line.split(',')
        if sepline[2] == 'age':
            continue
        if int(sepline[2]) < 30:
            print(f'{sepline[0]} {sepline[1]} {sepline[4]}', end = '')