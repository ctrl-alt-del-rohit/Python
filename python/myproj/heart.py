import turtle
import time

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(2)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    curve()
    pen.left(120)
    curve()
    pen.forward(224)
    pen.end_fill()

def txt():
    pen.up()
    # Calculate the center position based on screen size
    screen_width = turtle.Screen().window_width()
    text_width = 200  # Adjust the value based on the width of the text
    center_x = (screen_width - text_width) / 3
    pen.setpos(center_x, 20)
    pen.down()
    pen.color('lightgreen')
    pen.write("hi", align="right", font=("Verdana", 20, "bold"))

pen.up()
pen.sety(-150)  # Adjust the initial position to bring the heart to the center
pen.down()

heart()
txt()

pen.ht()

time.sleep(4)
turtle.mainloop()
