import csv
import statistics
with open('employees.csv', newline='') as f:
    x = 1
    wiek = []
    reader = csv.reader(f)
    print('#    ', end = '')
    for row in next(reader):
        print(f'%-15s'%row.upper(), end = '')
    print('')
    print('='*80)
    for row in reader:
        print(f'%-2s %-15s %-15s %-15s %-15s'%(x, row[1], row[0].upper(), row[2], row[3]))
        x += 1
        wiek.append(int(row[2]))
    print(f'Średnia wieku: ', end ='')
    print(statistics.mean(wiek))

        