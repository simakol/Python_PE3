'''
while умова:
    тіло циклу

цикл while виконує тіло циклу до тих пір, поки умова істинна
'''

# user_age = int(input("Введіть свій вік: "))

# while user_age < 18:
#     user_age = int(input("Введіть свій вік більше 18: "))

# print("Ваш вік:", user_age)

'''
Користувач вводить логін. Якщо його логін == admin, то ми запитуємо пароль. Якщо пароль == qwerty, то ми впускаємо адміна. Якщо ні, запитуємо пароль до тих пір, поки він не введе правильний. А я кщо логін не admin, то просто вітаємо юзера.
'''

# ADMIN_LOGIN = "admin"
# ADMIN_PASSWORD = "qwerty"

# login = input("Введіть логін: ")

# if login == ADMIN_LOGIN:
#     password = input("Вітаю! Введіть пароль: ")
#     while password != ADMIN_PASSWORD:
#         password = input("Невірний пароль! Спробуйте ще раз: ")
#     print("Вітаю, Адмін!")
# else:
#     print("Вітаю,", login)


# while True:
#     print("Hello")

'''
for змінна in що перебираємо:
    тіло циклу

цей цикл закінчиться тоді, коли закінчиться те, що ми перебираємо
'''

# word = "hello"

# for letter in word:
#     print(letter)

'''
1. for letter = "h" in word = "hello":
    print("h")
2. for letter = "e" in word = "hello":
    print("e")
3. for letter = "l" in word = "hello":
    print("l")
4. for letter = "l" in word = "hello":
    print("l")
5. for letter = "o" in word = "hello":
    print("o")

'''

# range(a, b) -> [a, b)
# range(1, 10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(5, 8) -> 5, 6, 7

# range(1, 11, 3) -> 1, 4, 7, 10

'''
вивести в консоль всі парні числа від 1 до 100
'''

# for index in range(2, 101, 2):
#     print(index)

'''
вивести в консоль всі парні числа від 1 до 100, крім тих, які кранті 4
'''

# for index in range(2, 101, 4):
#     print(index)

# for index in range(2, 101, 2):
#     if index % 4 != 0:
#         print(index)

'''
у нас є якесь речення, і у цьому реченні випадково вставлено багато цифр 5. наша задача перебрати речення і створити нове речення без випадкових цифр
'''

# sentence = "H5el5lo5 e5v5er5yo5ne5!5 N5i5ce5 t5o 5m5e5e5t5 y5o5u5"
# correctSentence = "" # "Hello everyone! Nice to meet you"

# for char in sentence:
#    if char != "5":
#       correctSentence += char
# #  correctSentence = correctSentence + char


# for char in sentence:
#     if char == "5":
#         continue
#     correctSentence += char

# print(correctSentence)


# sentence = "H1el4lo56 e9v0er2yo3ne5!4 N8i7ce5 t88o 5m2e8e10t5 y3o6u5"
# correctSentence = "" # "Hello everyone! Nice to meet you"

# for char in sentence:
#     if not char.isdigit():
#         correctSentence += char

# print(correctSentence)
# print("5".isdigit())
# print("t".isdigit())


# for number in range(1, 10):
#     if number == 5:
#         continue # переходить на наступну ітерацію (код нижче не виконується)
#     print(number)

# for number in range(1, 10):
#     if number == 10:
#         break # зупиняє цикл і виходить з нього
#     print(number)
# else: # else у циклі спрацювує тоді, коли не спрацював ні один break
#     print("Break не спрацював")



'''
користувач вводить слово і букву, яку він хоче перевірити.
якщо ця буква є у слові, ми про це пишемо
якщо букві у слові немає, ми кажемо, що цієї букви не має
'''

# word = input("Введіть слово: ").lower()
# letter = input("Введіть букву, яку хочете знайти: ").lower()

# if letter in word:
#     print("Буква", letter, "є у слові", word)
# else: 
#     print("Букви", letter, "немає у слові", word)


# print(letter in word)

# for char in word:
#     if char == letter:
#         print("Буква", letter, "є у слові", word)
#         break
# else:
#     print("Букви", letter, "немає у слові", word)




'''
1. запитати у користувача 2 числа - 1 це початок діапазону циклу і 2 - це кінець діапазону
2. якщо користувач ввів 1 число більше ніж 2, то потрібно запитувати у нього 2ге число до тих пір, поки він не введе правильно(щоб 1 число було менше за 2)
3. запитати у користувача 3 число, яке ми шукаємо у діапазоні
4. запускаємо цикл і в кінці виводмо повідомлення чи є число 3 у діапазоні, чи його там немає
'''

'''
>> Введіть початок діапазону: 4
>> Введіть кінець діапазону: 2
>> Невірно! Права сторона не може бути менша за ліву, спробуйте ще раз: 3
>> Невірно! Права сторона не може бути менша за ліву, спробуйте ще раз: 7
>> Введіть число, яке ви хочете перевірити: 5
>> Число 5 є у діапазоні
'''

# from_number = int(input("Введіть початок діапазону: "))
# to_number = int(input("Введіть кінець діапазону: ")) + 1

# while from_number >= to_number:
#     to_number = int(input("Невірно! Права сторона не може бути менша за ліву, спробуйте ще раз: ")) + 1


# search_number = int(input("Введіть число, яке ви хочете перевірити: "))


# for number in range(from_number, to_number):
#     if search_number == number:
#         print("Число", search_number, "є у діапазоні")
#         break
# else:
#     print("Числа", search_number, "немає у діапазоні")