import statistics

wynagrodzenie = [21600, 4350, 3920, 5590, 3250, 4010]

arytmetyczna = statistics.mean(wynagrodzenie)
mediana = statistics.median(wynagrodzenie)
odchylenie = statistics.stdev(wynagrodzenie)

print(f'Średnia arytmetyczna wynagrodzeń: {arytmetyczna}')
print(f'Mediania: {mediana}')
print(f'Odchylenie standardowe: {odchylenie}')