import re

text = 'To be, or not to be, that is the question'
samo = re.findall('a|e|i|o|u', text)
print(f'Liczba samogłosek: {len(samo)}')
