import turtle

#add colors of your choice
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()

#to chose background color
turtle.bgcolor('black')

#to chose direction and speed of turtle
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)
    
