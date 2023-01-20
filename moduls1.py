# module OS.
# import os
# print(os.name) # Название операционной системы
# print(os.getlogin())# имя пользавателя 
# print(os.name) #Информация информационной системы



# from datetime import *
# import time

# print(datetime.now()) показ действущее время
# print(datetime.today())
# a = datetime(2023,1,13,19,9,13) задается полная да от года до секунды(по вашему усмотрению)
# print(a)
# b = time(11,34,56)
# print(b)
# c = time(hour = 11) детально выводим время
# print(c)
# print('Agil')
# time.sleep(5)
# print('hello')

# for i in range (5):
#     print("Agil pomolchi")
#     time.sleep(3)

# d = date(2023,1,13) задается дата
# print (d)

# inform = datetime(2023,2,13,19,14,13)
# print("year =",inform.year)вытаскивает по значениям
# print("month=",inform.month)


# from datetime import *

# now = datetime.now()
# t = now.strftime("%H:%M:%S") формат сокращ. по часу,минутам
# # print("time:, t")

# s = now.strftime("%A,%Y,%m,%d") сокращ.по недели, году
# print(s)

# import random

# memoryview_list =["agil","banan","Egida"]
# random.shuffle(my_list)
# print(my_list)
# print(random.choice(my_list))

# print(random.random())

# import urllib.request модуль для открытия Url адресов


# a = urllib.request.urlopen("https://www.itbootcamp.com/#/")
# print(a.read()) счит
# print(a.getcode()) код доступа 200 что значит сайт подходит для получения информации

# import csv 
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Duration"])
#     writer.writerow([1, 'Aktan', 'Python'])
#     writer.writerow([2, 'Dima', 'JS'])
#     writer.writerow([3, 'Amal', 'Flutter'])

