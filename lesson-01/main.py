'''
print("Hello everyone!")  # print - виводить будь-що у консоль

first_number = 10
second_number = 5

print(first_number + second_number)
print(first_number - second_number)
print(first_number * second_number)
print(first_number / second_number)
# 5^2 = 25 (5 * 5)
# 3^3 = 27 (3 * 3 * 3)
# 2^5 = 2 * 2 * 2 * 2 * 2 = 32
print(first_number ** 3)
print(second_number ** 5)    
print(5 % 3) # 3 5 -> 5 - 3 = 2
print(12 % 5) # від 1 до 12 -> 10 -> 12 - 10 = 2
print(12 % 4) # 0
print(14 % 2) # 0
'''
'''
print(15 > 2)
print(15 < 2)
print(10 >= 10)
print(10 <= 9)
print(10 == 10)
print(10 == 8)
print(8 != 8)
'''

#! Типи даних

user_age = 28  # Integer(int) - цілочисельний тип даних (-6, 548, 0, 100254)
user_height = 1.80  # Float - всі числа з плаваючою точкою (дробові числа)
user_name = "Oleg"  # String(str) - строковий тип даних
# print(user_name * 2)
# print("Hello, " + user_name)
# Boolean(bool) - логічний тип даних, він вміє зберігати тільки два значення: True(правда) і False(неправда)
is_user_play_games = True
user_city = None  # NoneType - нічого не означає

# type() - ф-ція, яка перевіє тип даних

# print(type(0.5))

'''
 int() - перетворює на цілочисельний тип
 float() - перетворює на число з плаваючою крапкою
 bool() - перетворює на логічний тип(True or False)
 str() - перетворює на строку
'''

# number = "5"
# print(type(number))

# number = int(number)

# print(type(number))
# print(number + 8)


print(user_height)
print(type(user_height))

user_height = str(user_height)
print(type(user_height))
print(user_height)

