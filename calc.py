from tkinter import *
window=Tk()
window.geometry('500x300')
window.title('Calculator')
window.configure(bg='#F0F8FF')
expression=''
input_text=StringVar()
#fun for button click
def btn_click(item):
    global expression
    expression =expression + str(item)
    input_text.set(expression)
def clean():
    global expresson
    expression=""
    input_text.set("")
def equal():
    global expression
    result=eval(expression)
    input_text.set(result)
#Frame
calc_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
calc_frame.pack(side = TOP)
#Input Text
input_field = Entry(calc_frame,textvariable=input_text, font = ('arial', 18, 'bold'), width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)
#Button Frame
button_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
button_frame.pack()
clear = Button(button_frame,command=lambda: clean(), text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(button_frame, command=lambda: btn_click("/"), text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
seven = Button(button_frame,command=lambda: btn_click("7"), text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, command=lambda: btn_click("8"), text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(button_frame,command=lambda: btn_click("9"), text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, command=lambda: btn_click("*"), text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
four = Button(button_frame, command=lambda: btn_click("4"), text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
four.grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(button_frame,command=lambda: btn_click("5"), text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
five.grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(button_frame,command=lambda: btn_click("6"), text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
six.grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(button_frame,command=lambda: btn_click("-"), text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
one = Button(button_frame,command=lambda: btn_click("1"), text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
one.grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(button_frame,command=lambda: btn_click("2"), text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
two.grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(button_frame,command=lambda: btn_click("3"), text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
three.grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(button_frame,command=lambda: btn_click("+"), text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
zero = Button(button_frame,command=lambda: btn_click("0"), text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(button_frame,command=lambda: btn_click("."), text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
point.grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(button_frame,command=lambda: btn_click("="), text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
equals.grid(row = 4, column = 3, padx = 1, pady = 1)
window.mainloop()
