import re
reduta = '''Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na
pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się
szeregi, Prosto, długo, daleko, jako morza brzegi.'''
x = re.findall('[a,ą,e,ę,i,o,ó,u,y]', reduta)
print(reduta)
print(f'Długość tekstu: {len(x)}')