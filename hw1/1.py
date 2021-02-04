# 1-ое задание

user_a = 55
user_b = 13
c = (user_a + user_b)
print(user_a)
print(c)
name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
phone = ('Введите номер телефона: ')

# 2-ое задание

time = int(input('Введите время в секундах: '))
hours = time // 3600
min = (time - (hours * 3600)) // 60
sek = time-(hours*3600+min*60)
print('Ваше время: {}:{}:{}  ;формат чч:мм:сс'.format(hours, min, sek))