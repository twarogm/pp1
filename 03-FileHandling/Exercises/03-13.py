tab=[32, 16, 5, 8, 24, 7]
with open('tablicadotxt.txt', 'w') as file:
    for x in tab:
        file.write(f'{x}\n')
    