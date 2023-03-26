'''
float - числа з плаваючою крапкою
bool - true, false
str - строки
int - цілі числа
noneType - означає нічого

type() - перевіряє тип даних
input() - запитує у користувача якісь дані, завжди повертає str
'''

# value = input("Введи якесь значення: ")

# print("Користувач ввів", value, "Тип значення:", type(value))

# print("Привіт,", user_name, "! Раді вас вітати)")

# first_number = int(input("Введіть перше число: "))
# second_number = int(input("Введіть друге число: "))
# result = first_number + second_number

# print("Вираз", first_number, "+", second_number, "=", result)

#! Розгалудження

# user_number = int(input("Введіть число: "))

'''
if умова:
    тіло умови, якщо умова істина
'''
# print("До умови")

# if user_number > 10:
#     print("Число більше 10!")
# elif user_number < 10:
#     print("Число менше 10!")
# # elif user_number == 10:
# #     print("Число рівне 10!")
# else:
#     print("Число рівне 10!")

# print("Після умови")


'''
користувач вводить число і потрібно вивести повідомлення про те парне число чи ні
>> 5
>> Число 5 є непарним (odd)
>> 10
>> Число 10 є парним (even)
Ознака парності числа: ділиться на 2 без остачі
'''

# print(10 % 3) # 1 -> 9 / 3 = 3 -> 10 - 9 = 1
# print(15 % 5) # 0
# print(14 % 2) # 0
# print(14 % 3) # 2

# user_number = int(input('Введіть число: '))

# if user_number == 0:
#     print("Ваше число 0 - ні парне, ні непарне")
# elif user_number % 2 == 0:
#     print("Ваше число парне")
# else:
#     print("Ваше число непарне")


#! Логічні оператори

'''
- логічне І: and - повертає перше false, якщо не знайшло, повертає останній елемент
- логічне АБО: or - повертає перше true, якщо не знайшло, повертає останній елемент
- логічне НІ: not - змінює логічний тип на зворотній true -> false, false -> true
'''

'''

True: всі числа, крім 0 | будь-яка строка, в якій є символи, крім пустої

False: 0, ""(пуста строка), None

'''

# print(not False)
# print(not True)
# print(not not True) # not True -> False -> not False -> True

# print(not 0) # not False -> True

# print(not " ")

# print(0 or 10 or False)
# print(None or "" or "hello" or 0)
# print(0 or None or False or "" or 0)

# print("hello" and "python" and 158 and None and -59)

# print("hey" and 0 and "" and False and "python")

# print("Hello world" and "I love python" or None and "Hi there")

'''
1. "Hello world" and "I love python" -> "I love python"
2. None and "Hi there" -> None
3. "I love python" or None -> "I love python"

'''

# print("" or 0 and "hello" or 56 and 42)

'''
1. 0 and "hello" -> 0
2. 56 and 42 -> 42 | "" or 0 or 42
3. "" or 0 or 42 -> 42
'''

'''
1. користувач вводить 3 числа з консолі і нам потрібно вивести найбільше число
>> 5
>> 9
>> 4
>> Число 9 найбільше

2. написати консольний калькулятор: користувач вводить 1 число, 2 число і знак операції(+, -, *, /) і йому повертається результат розрахунку
>> Введіть 1 число: 10
>> Введіть 2 число: 4
>> Введіть знак операції: *
>> Результат: 40

3. Написати кофе машину
Користувач вносить кошти і вибирає напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)). Програма повинна видати йому напій і повернути решту, якщо коштів не вистачає - сказати про це.

>> Внесіть кошти: 15
>> Виберіть напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)): 3
>> Ось ваш чай, ваша решта - 5 грн

>> Внесіть кошти: 30
>> Виберіть напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)): 2
>> На жаль, недостатнько коштів, заберіть решту.
'''


'''
2. написати консольний калькулятор: користувач вводить 1 число, 2 число і знак операції(+, -, *, /) і йому повертається результат розрахунку
>> Введіть 1 число: 10
>> Введіть 2 число: 4
>> Введіть знак операції: *
>> Результат: 40
'''

# first_number = int(input("Введіть перше число: "))
# second_number = int(input("Введіть друге число: "))
# operation = input("Введіть знак операції: ")

# result = 0

# if operation == "+":
#     result = first_number + second_number
# elif operation == "-":
#     result = first_number - second_number
# elif operation == "*":
#     result = first_number * second_number
# elif operation == "/":
#     result = first_number / second_number
# else:
#     result = "Неправильна операція"

# print("Результат:", result)


'''
1. користувач вводить 3 числа з консолі і нам потрібно вивести найбільше число
>> 5
>> 9
>> 4
>> Число 9 найбільше
'''

# print("Введіть 3 числа: ")
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# biggest_num = num1

# if num1 > num2 and num1 > num3:
#     biggest_num = num1
# elif num2 > num1 and num2 > num3:
#     biggest_num = num2
# else:
#     biggest_num = num3

# print("Число", biggest_num, "найбільше")


'''
3. Написати кофе машину
Користувач вносить кошти і вибирає напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)). Програма повинна видати йому напій і повернути решту, якщо коштів не вистачає - сказати про це.

>> Внесіть кошти: 15
>> Виберіть напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)): 3
>> Ось ваш чай, ваша решта - 5 грн

>> Внесіть кошти: 30
>> Виберіть напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)): 2
>> На жаль, недостатнько коштів, заберіть решту.
'''

# cash = int(input("Внесіть кошти: "))
# print("Виберіть напій: \n 1 - Лате(25 грн), \n 2 - Капучино(50 грн), \n 3 - Чай (10 грн):")
# drink = int(input())

# if drink == 1 and cash >= 25:
#     print("Ось ваш Лате, ваша решта -", cash - 25, "грн")
# elif drink == 2 and cash >= 50:
#     print("Ось ваш Капучино, ваша решта -", cash - 50, "грн")
# elif drink == 3 and cash >= 10:
#     print("Ось ваш Чай, ваша решта -", cash - 10, "грн")
# else:
#     print("Помилка! Заберіть ваші кошти!")