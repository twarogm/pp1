def norepeating(arr):
    right = []
    for i in arr:
        if arr.count(i) == 1:
            right.append(i)
    print(f'Niepowtarzające się numery: {right}')

tab = [1,2,1,2,7,9,9,11]

norepeating(tab)
