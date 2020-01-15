from turtle import *

a = int(input('Введите длину стороны квадрата: '))
n = int(input('Введите клоичество линий штриховки: '))

ht()

for _ in range(4):
	forward(a)
	left(90)

for i in range(n):
	if i % 2 == 0:
		forward(a / (n + 1))
		left(90)
		forward(a)
		right(90)
	else:
		forward(a / (n + 1))
		right(90)
		forward(a)
		left(90)
	

home()
input()