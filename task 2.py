#Старший и младший
#Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

num = int(input("Введите колличество детей: "))
data = dict()
i = 0
while i < num:
    key = input('Введите имя: ')
    value = input('Введите возраст: ')

    data[key] = value
    i +=1
min = value
for value in data.values():
    if min > value:
        min = value
print(data)
print('Самый младший :', min)