from random import randint
import time
"""
TODO:
Создать две переменные igrok1 и igrok2,
которым будет присвоен ввод с клавиатуры имён двух игроков соответственно.
"""

"""
TODO: 
Вывести текст Кубик бросает 'имя первого игрока'. 
"""


time.sleep(3)

n1 = randint(1, 6)

print("Выпало число", n1)
time.sleep(1)

"""
TODO: 
Вывести текст Кубик бросает 'имя второго игрока'. 
"""


time.sleep(3)

n2 = randint(1, 6)

print("Выпало число", n2)

if (n1 > n2):
	print("Выиграл", igrok1)
elif (n1 < n2):
	print("Выиграл", igrok2)
else:
	print("Ничья")


