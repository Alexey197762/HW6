# Еще немного о друзьях
#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
#  Создайте список friends и добавьте в него N словарей с ключами name и age.
#  Выведите средний возраст всех друзей и самое длинное имя.

num = int(input("Введите колличество друзей: "))
friends = dict()
i = 0
while i < num:
    name = input('Введите имя: ')
    age = input('Введите возраст: ')

    friends[name] = age
    i +=1
sum = 0
max = 0
for value in friends.values():
    sum += int(value)

for key in friends.keys():
    if len(key) > max:
        max = len(key)
        max_n = key
   
print("Имена друзей : ", friends)
print("Средний возраст : ", sum/num)
print("MAX ИМЯ : ", max_n)