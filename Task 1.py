# Фрукты
# Пользователь вводит число K - количество фруктов.
# Затем он вводит K фруктов в формате: название фрукта и его количество.
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

num = int(input("Enter number: "))
user = list()
for i in range(num):
    firstnam = input('Enter fruit: ')
    number = input('Enter number: ')
    user.append({firstnam: number})
  
print(user)