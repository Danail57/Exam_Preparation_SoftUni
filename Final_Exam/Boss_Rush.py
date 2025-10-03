import re

number = int(input())
pattern = r'(\|([A-Z]{4,})\|):#([A-Za-z]+ [A-Za-z]+)#'
is_valid = False

for _ in range(number):
    message = input()
    match = re.match(pattern, message)

    if match:
        boss_name = match.group(2)
        title = match.group(3)
        is_valid = True
        print(f'{boss_name}, The {title}')
        print(f'>> Strength: {len(boss_name)}')
        print(f'>> Armor: {len(title)}')
    else:
        print('Access denied!')
