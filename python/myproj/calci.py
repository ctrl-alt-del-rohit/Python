from tkinter import *
win = Tk()                                     #To bring the main box
win.title("Python Calculator")                 #title of the box
win.geometry('400x280')                        #size of the box
win.resizable(0,0)                             #to choose if to make the box resizable or not.

#to display btn on click
def on_click(num):
    global expression
    expression= expression+str(num)
    input_txt.set(expression)
    
expression=""
input_txt= StringVar()

#to clear the input field
def on_clear():
    global expression
    expression=""
    input_txt.set("")
    
#to show result on equal
def on_equal():
    global expression
    result=str(eval(expression))
    input_txt.set(result)
    expression=""

def on_enter_press(event):
    if event.keycode == 13:
        on_equal()
        
input_frame=Frame(win, height=55,width=350, background="#F8F0E3")# to create a frame
input_frame.pack(side=TOP)
input_field=Entry(input_frame, font=("Microsoft Sans Serif",18,"bold"),width=24,justify=RIGHT, textvariable=input_txt)# to make a field to write in it
input_field.grid(row=0,column=0)
input_field.pack(pady=10) # to increase the height of the input field

btn_frame=Frame(height=265,width=500,)
btn_frame.pack()# frame for the button

clear=Button(btn_frame,text="Clear",width=35,height=2, command=lambda: on_clear()).grid(padx=1,pady=1,row=0,column=0,columnspan=3)#clear button

#numbers
one=Button(btn_frame, text="1", width=10, height=2, command=lambda: on_click(1)).grid(column=0,row=3,padx=1,pady=1)
two=Button(btn_frame,text="2",width=10,height=2, command=lambda: on_click(2)).grid(column=1,row=3,padx=1,pady=1)
three=Button(btn_frame,text="3",width=10,height=2, command=lambda: on_click(3)).grid(column=2,row=3,padx=1,pady=1)
four=Button(btn_frame,text="4",width=10,height=2, command=lambda: on_click(4)).grid(column=0,row=2,padx=1,pady=1)
five=Button(btn_frame,text="5",width=10,height=2, command=lambda: on_click(5)).grid(column=1,row=2,padx=1,pady=1)
six=Button(btn_frame,text="6",width=10,height=2, command=lambda: on_click(6)).grid(column=2,row=2,padx=1,pady=1)
seven=Button(btn_frame,text="7",width=10,height=2 ,command=lambda: on_click(7)).grid(column=0,row=1,padx=1,pady=1)
eight=Button(btn_frame,text="8",width=10,height=2, command=lambda: on_click(8)).grid(column=1,row=1,padx=1,pady=1)
nine=Button(btn_frame,text="9",width=10,height=2, command=lambda: on_click(9)).grid(column=2,row=1,padx=1,pady=1)
percent=Button(btn_frame,text="%",width=10,height=2, command=lambda: on_click("%")).grid(column=0,row=4,padx=1,pady=1)
zero=Button(btn_frame,text="0",width=10,height=2,command=lambda: on_click(0)).grid(column=1,row=4,padx=1,pady=1)
dot=Button(btn_frame,text=".",width=10,height=2, command=lambda: on_click(".")).grid(column=2,row=4,padx=1,pady=1)


#function buttons
divide=Button(btn_frame,text="/",width=10,height=2, command=lambda: on_click("/")).grid(column=4,row=0,padx=1,pady=1)
multiply=Button(btn_frame,text="x",width=10,height=2, command=lambda: on_click("*")).grid(column=4,row=1,padx=1,pady=1)
minus=Button(btn_frame,text="-",width=10,height=2, command=lambda: on_click("-")).grid(column=4,row=2,padx=1,pady=1)
plus=Button(btn_frame,text="+",width=10,height=2, command=lambda: on_click("+")).grid(column=4,row=3,padx=1,pady=1)
equal=Button(btn_frame,text="=",width=10,height=2, command=lambda: on_equal()).grid(column=4,row=4,padx=1,pady=1)

input_field.bind('<KeyRelease>', on_enter_press)

win.mainloop()                                 # to make the box stay on the screen

