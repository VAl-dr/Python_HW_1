import turtle

t = turtle.Turtle()
t.speed(10000)
t.ht()

def hexagon(x, y):

	t.setposition(x, y)
	t.left(30)
	t.forward(a)
	t.left(120)
	
	for _ in range(6):
		t.pendown()
		t.forward(a)
		t.left(60)
		t.penup()
		
	t.left(60)
	t.forward(a)
	t.left(150)


n = int(input('Введите количество шестиугольников вдоль стороны большого шестиугольника: '))
a = int(input('Введите длинну сторны шестиугольника: '))
h = a * (3 ** (1/2)) / 2

t.penup()

for i in range(2 * n - 1):
	x = ((n - 1) - i) * (2 * h)
	y = 0
	hexagon(x, y)

for i in range(n - 1):
	for j in range((n - 1) * 2 - i):
		x = ((2 * (n - 1) - 1) - i) * h - (2 * h * j) 
		y = (3 / 2) * a * (i + 1)
		hexagon(x, y)
		hexagon(x, -y)

t.home()
input()