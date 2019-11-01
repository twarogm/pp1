tab = []
sum = 0
nums = 0

with open('numbersinrows.txt') as file:
    for line in file:
        sepline = line.split(',')
        nums += len(sepline)
        for i in sepline:
            sum += int(i)

print(f'Ilość liczb w pliku: {nums}. Ich suma: {sum}')