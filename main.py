boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print('Кому-то не достанется пары!')
pairs = zip(sorted(boys), sorted(girls))
print('Идеальные пары: ')
for boy, girl in pairs:
    print(f'{boy} и {girl}')