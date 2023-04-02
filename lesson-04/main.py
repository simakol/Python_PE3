# def print_message():
#     print("hello world!")


# print_message()
# print_message()
# print_message()
# print_message()
# print_message()
# print_message()

# def num():
#     print("Це ф-ція, яка вміє повертати результат")
#     return 10

# result = num() + 7

# print(result)


# def sum(a, b):  # a, b - параметри(звичайні змінні, які отримують свої значення на момент виклику ф-ції)
#     return a + b  # return - повертає результат виконання ф-ції, який можна використовувати у місці її виклику


# print(sum(5, 3))  # 5, 3 - аргументи
# print(sum(10, 60))

'''
створіть 2 ф-ції, які просто повертають якесь число.
збережіть результати виконання цих ф-цій у 2 окремі змінні
і виведіть у консоль добуток цих 2х змінних
'''

# def num1():
#     return 53

# def num2():
#     return 198

# x = num1() # x = 53
# y = num2()

# print(x * y)


'''
напишіть функцію, яка в якості параметра очікує якусь строку і повртає її довжину (без використання len())
'''


# def str_length(str):
#     counter = 0
#     for char in str:
#         counter += 1 # counter = counter + 1
#     return counter


# print(str_length("hello!"))  # 6
# print(str_length("hello, my name is Alex")) # 22


'''
напишіть функцію, яка приймає строку і повертає цю саму строку, але перевернуту
'''

'''
1. нова строка, в яку ми будемо накопичувати букви в зворотньому порядку
2. довижина нашої строки
3. запустити цикл в діапазоні довижи строки
4. отримувати букви з кінця строки і додавати до нової строки
'''


# def reverseStr(str):
#     new_str = ""
#     str_len = len(str) # 5
#     for i in range(str_len): # 0 до 4
#         new_str += str[str_len - i - 1]
#         #1 str[5 - 0 - 1] -> str[4] -> o
#         #2 str[5 - 1 - 1] -> str[3] -> l
#         #3 str[5 - 2 - 1] -> str[2] -> l
#         #4 str[5 - 3 - 1] -> str[1] -> e
#         #5 str[5 - 4 - 1] -> str[0] -> h
#     return new_str

# print(reverseStr("hello")) # olleh
# print(reverseStr("laptop")) # potpal
# print(reverseStr("привіт")) # тівирп


'''
написати функцію калькулятор. функція очікує 3 параметри: 1 число, 2 число і знак операції. функція повинна повернути результат математичної операції
'''




def calculate(first_number, second_number, operation):
    result = 0

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    else:
        result = "Неправильна операція"

    return result


print(calculate(5, 8, "+"))  # 13
print(calculate(15, 3, "/"))  # 5
print(calculate(11, 9, "*"))  # 

first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))
operation = input("Введіть знак операції: ")

print(calculate(first_number, second_number, operation))