import turtle

def draw_square():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)

	for time in range(0, 4):
		brad.forward(100)
		brad.right(90)
	

def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)


def draw_triangle():
	tri = turtle.Turtle()
	tri.shape("triangle")
	tri.color("pink")

	tri.forward(100)
	for time in range(0, 2):
		tri.left(120)
		tri.forward(100)


def main():
	window = turtle.Screen()
	window.bgcolor("red")
	draw_square()
	draw_circle()
	draw_triangle()
	window.exitonclick()

main()