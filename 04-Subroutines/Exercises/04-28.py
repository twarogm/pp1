lan = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
val = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

def rysujWykres(lan, val):
    for i in lan:
        print('%10s:'%i, end = ' ')
        for j in val:
            print('#'*j)
            val.remove(j)
            break

rysujWykres(lan, val)


