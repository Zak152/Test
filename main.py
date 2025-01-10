import random
print('Hello World')
print('Have a good day')
print(5+10)
a = input('Как дела? ')
if a == 'Нормально':
    print('У меня тоже')
elif a == 'Отлично':
    print('Хорошо!')
else:
    print('Понял!')

chance = random.randint(1,100)
if chance <= 70:
    print('Еда не сгорела!')
elif chance >=70:
    print('Твоя еда сгорела...')
