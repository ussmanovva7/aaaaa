#  module OS.
# import os
# # print(os.name) Назавание операционной системы
# # print(os.getlogin()) # имя пользователя операционной системы
# print(os.uname()) # информация оперционной системы

# модуль Sys Модуль sys обеспечивает доступ к некоторым переменным и
#  функциям, взаимодействующим с интерпретатором python.
# import sys
# print(sys.platform) оперционна система

# print(sys.argv) путь в котором вы на
# # ходитесь
# print(sys.version) # версия пайтона


# from datetime import *
# import time


# print(datetime.now()) показывают действующее время
# print(datetime.today())
# a = datetime(2023,1,13,19,1,13) задается полная да от года до секунды(по вашему усмотрению)
# print(a)
# b = time(11,34,56)задается нужное вам время
# print(b)
# c = time(hour = 11,minute=33,second=12) детально выводим время
# print(c)

# print("Agil")
# time.sleep(5) задержка времени на 5 сек
# print("hello")

# for i in range(5):
#     print("Agil pomolchi po bratski")
#     time.sleep(3) задержка в три секунды для вывода строки  5 раз 
# d = date(2023,1,13)
# print(d) задается дата

# inform = datetime(2023,1,13,19,14)
# print("year=",inform.year)  вытаскиевает по значениям 
# print("month=",inform.month)
# print("hour=",inform.hour)
# print("hour=",inform.minute)

# from datetime import *

# now = datetime.now()
# t = now.strftime("%H:%M:%S") формат сокращкния по часу, минутам и секундам
# print("time:", t)


# s = now.strftime("%A,%Y,%m,%d") сокращение по недели, году, месяцу и дню

# print(s)


# import random


# my_list = ["agil","banan","apple","Egida"]
# random.shuffle(my_list) перемешивает список
# print(my_list)
# print(random.choice(my_list)) достает случайный элемент из списка

# print(random.randint(1,50)) диапозон от 1 до 50, случное число вытаскивает
# print(random.randrange(0,10,2))

# print(random.random())

# import urllib.request модуль для открытия Url адресов

# a = urllib.request.urlopen("https://www.itcbootcamp.com/#/")
# print(a.read()) считывается html код страницы
# print(a.getcode()) код доступа 200, что значит сайт подходит для получения информации


# Простейший пример записи CSV файла:
# import csv
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Duration"])
#     writer.writerow([1, 'Aktan', 'Python'])
#     writer.writerow([2, 'Dima', 'JS'])
#     writer.writerow([3, 'Amal', 'Flutter'])

 
# import datetime
# b = datetime.time.sleep()
# print(b)
# import math
# from math import pi, cos, radians, perm ,sqrt
# print(math.ceil(9.1))
# print(math.floor(9.6))
# s = 0
# print(math.isfinite(s))

# import secrets
# token = secrets.token_hex(2)
# print(token)

# elem = secrets.choice([21,'ff', 43, True])
# print(elem)


# import collections
# a = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala', 'arkadiy_kidala']
# c = collections.Counter()
# for word in a:
#     c[word] +=1
# print(c)