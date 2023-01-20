# a = (1,2,3,6,2,2,3,5,"hello")
# print(type(a))
# b = [1,2,3,3,5,234,"hello"]
# b.append("Nurzada")
# print(b)
# print(b.count(3))
# b.pop(0)
# print(b)
# print(b.index(5))

# lst = ['ermek', 'vlad', 'nooruz', 'baytik', 'umar', 'janybek', 'ermek', 'nurzada']

# print(len(lst))
# start stop step 
# print(lst[:])
# print(lst[0:8:2])
# print(lst[3:])
# print(lst[:3])
# print(lst[1:5])
# print(lst[-1])
# print(lst[1:6:3])
# print(lst[0], lst[3], lst[5])
# a = 'Hello'
# print(len(a))
# print(a[1:4])

# lst1 = ['hello', 'python', 'love', 'i']
# print(lst1[0], lst1[3], lst1[2], lst1[1])



# lst.append('agil') # добавляет элемент в конец списка
# lst.append('azat') 
# # print(lst)
# name = input('Enter your name: ')
# lst.append(name)
# lst.append(1)
# print(lst)


# lst = ['ermek', 'vlad', 'nooruz', 'baytik', 'umar', 'janybek', 'ermek', 'nurzada']

# lst1 = ['blablabla']
# lst.append(lst1)
# lst.remove('ermek')# удаляет элемент по названию
# lst.pop(1)# удаляет по индексу
# print(lst.index('nooruz'))# находит индекс элемента по названию
# print(lst.count('ermek'))# считает количество элементов

# lst2 = [1,2,3,4,5,6,7,8,9]
# lst.extend(lst2) # обьеденяет два массива в один
# len1 = len(lst)
# l = len1 // 2
# print(lst[:l])
# names = []
# name1 = input('Enter name 1: ')
# name2 = input('Enter name 2: ')
# name3 = input('Enter name 3: ')
# name4 = input('Enter name 4: ')
# name5 = input('Enter name 5: ')
# name6 = input('Enter name 6: ')
# names.append((name1, name2))
# print(names)

# lst = ['ermek', 'vlad', 'nooruz', 'baytik', 'umar', 'janybek', 'ermek', 'nurzada']
# name = input('Введи имя для удаления: ')
# if name in lst:
#     lst.remove(name)
# else:
#     print(f'В списке нету имени {name}')
# print(lst)


# names = [('Maga', 40), ('Sultan', 18)]

# name = input('Введи имя: ')
# age = int(input('Введи возраст: '))
# names.append((name, age))
# print(names)

# text = '123456789'
# text = list(text)
# print(text)



# lst = ['ermek', 'vlad', 'nooruz', 'baytik', 'umar', 'janybek', 'ermek', 'nurzada']

# print(lst[::-1])
# print(lst[-2:-8:-2])

# a = list(range(0,100,4))
# a.reverse()# разворачивает список
# print(a[::-1])

# tuple_1 = ('alex', 'john', 'bob')# tuple не изменяемый тип данных

# list1 = list(tuple_1)
# print(list1)

# lst1 = ['alex', 'john', 'bob','bakai', 'azat', 'cholpon']
# lst2 = ['bakai', 'azat', 'cholpon']

# lst1.extend(lst2)
# print(lst1.index('bob'))
# lst1.pop(2)
# print(lst1)

# start = int(input('Введи старт: '))
# stop = int(input('Введи stop: '))
# step = int(input('Введи step: '))

# if step == 0:
#     print('Шаг не может быть 0')

# else:
#     print(lst1[start:stop:step])


# 1-ЗД Создать список и 5 вложенных кортежей.
# d = (2,"iphone","redmi",1,7)
# print(type(d))

# 2-ЗД Создать Tuple из 3 элементов и вывести каждый из них по индексу.
# f = (2,5,"friends")
# print(f.index(5))
# print(f.index(2))
# print(f.index("friends"))

# 3-ЗД Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.
# u = [34,'73',True ,123.23,[12]]
# print(type(u))

# 4- ЗД 1.Создать Лист из 5 разных имён.

# 2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.

# a = ['artur','joomart','agil','nurzada','bayas']
# print("/".join(a))

# 5-ЗД Создать 2 списка(List) заполнить данными, к первому списку добавить все объекты второго списка 
# f = ['bmw','toyota','77','audi','mers']
# b = ['egida','agil','nurzada','25']
# f.extend(b)
# print(f)

# 6-ЗД Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack".
