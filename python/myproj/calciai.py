from tkinter import *

win = Tk()
win.title("Python Calculator")
win.geometry('300x350')
win.resizable(0, 0)

def on_click(num):
    global expression
    expression = expression + str(num)
    input_txt.set(expression)

def on_clear():
    global expression
    expression = ""
    input_txt.set("")

def on_equal():
    global expression
    result = str(eval(expression))
    input_txt.set(result)
    expression = ""

def on_percentage():
    global expression
    try:
        parts = expression.split("+")
        if len(parts) == 2:
            num = float(parts[0])
            percent = float(parts[1].rstrip("%"))
            result = num + (num * percent / 100)
            expression = str(result)
            input_txt.set(expression)
        parts = expression.split("-")
        if len(parts) == 2:
            num = float(parts[0])
            percent = float(parts[1].rstrip("%"))
            result1 = num - (num * percent / 100)
            expression = str(result1)
            input_txt.set(expression)
    except ZeroDivisionError:
        input_txt.set("Error")


expression = ""
input_txt = StringVar()

input_frame = Frame(win, height=80, width=300, background="#F8F0E3")
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=("Microsoft Sans Serif", 18, "bold"), width=16, justify=RIGHT, textvariable=input_txt)
input_field.grid(row=0, column=0, padx=10, pady=10)
input_field.pack(pady=10)

btn_frame = Frame(height=320, width=300)
btn_frame.pack()

clear = Button(btn_frame, text="Clear", width=16, height=2, command=lambda: on_clear())
clear.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

one = Button(btn_frame, text="1", width=7, height=2, command=lambda: on_click(1))
one.grid(row=1, column=0, padx=5, pady=5)
two = Button(btn_frame, text="2", width=7, height=2, command=lambda: on_click(2))
two.grid(row=1, column=1, padx=5, pady=5)
three = Button(btn_frame, text="3", width=7, height=2, command=lambda: on_click(3))
three.grid(row=1, column=2, padx=5, pady=5)

four = Button(btn_frame, text="4", width=7, height=2, command=lambda: on_click(4))
four.grid(row=2, column=0, padx=5, pady=5)
five = Button(btn_frame, text="5", width=7, height=2, command=lambda: on_click(5))
five.grid(row=2, column=1, padx=5, pady=5)
six = Button(btn_frame, text="6", width=7, height=2, command=lambda: on_click(6))
six.grid(row=2, column=2, padx=5, pady=5)

seven = Button(btn_frame, text="7", width=7, height=2, command=lambda: on_click(7))
seven.grid(row=3, column=0, padx=5, pady=5)
eight = Button(btn_frame, text="8", width=7, height=2, command=lambda: on_click(8))
eight.grid(row=3, column=1, padx=5, pady=5)
nine = Button(btn_frame, text="9", width=7, height=2, command=lambda: on_click(9))
nine.grid(row=3, column=2, padx=5, pady=5)

zero = Button(btn_frame, text="0", width=7, height=2, command=lambda: on_click(0))
zero.grid(row=4, column=0, padx=5, pady=5)
dot = Button(btn_frame, text=".", width=7, height=2, command=lambda: on_click("."))
dot.grid(row=4, column=1, padx=5, pady=5)

divide = Button(btn_frame, text="/", width=7, height=2, command=lambda: on_click("/"))
divide.grid(row=0, column=3, padx=5, pady=5)
multiply = Button(btn_frame, text="x", width=7, height=2, command=lambda: on_click("*"))
multiply.grid(row=1, column=3, padx=5, pady=5)
minus = Button(btn_frame, text="-", width=7, height=2, command=lambda: on_click("-"))
minus.grid(row=2, column=3, padx=5, pady=5)
plus = Button(btn_frame, text="+", width=7, height=2, command=lambda: on_click("+"))
plus.grid(row=3, column=3, padx=5, pady=5)
equal = Button(btn_frame, text="=", width=7, height=2, command=lambda: on_equal())
equal.grid(row=4, column=3, padx=5, pady=5)

percentage = Button(btn_frame, text="%", width=7, height=2, command=lambda: on_percentage())
percentage.grid(row=4, column=2, padx=5, pady=5)

win.mainloop()
