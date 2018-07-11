from tkinter import *
import parser

root = Tk()
root.title("Calculator")

#get the user input and plaace it into the input field
i = 0
def get_variables(num):
   global i
   display.insert(i,num)
   i+=1
#AC clear function
def clear_all():
    display.delete(0,END)

#deleting a single element
def undo():
    entire_string = display.get() #gets the string from the display field
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        #display.insert(0, "")

#calculate function
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile() #this is what does the math
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def factorial():
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number
    try:
        while counter > 0:
            fact = fact*counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")

#arithmetic operation
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length


#adding the input field
display = Entry(root)
display.grid(row=1,columnspan=6, sticky=W+E)


#adding buttons to the calculator
Button(root, text="1", bg="pink", command = lambda :get_variables(1)).grid(row=2, column=0)
Button(root, text="2", bg="pink", command = lambda :get_variables(2)).grid(row=2, column=1)
Button(root, text="3", bg="pink", command = lambda :get_variables(3)).grid(row=2, column=2)

Button(root, text="4", bg="pink", command = lambda :get_variables(4)).grid(row=3, column=0)
Button(root, text="5", bg="pink", command = lambda :get_variables(5)).grid(row=3, column=1)
Button(root, text="6", bg="pink", command = lambda :get_variables(6)).grid(row=3, column=2)

Button(root, text="7", bg="pink", command = lambda :get_variables(7)).grid(row=4, column=0)
Button(root, text="8", bg="pink", command = lambda :get_variables(8)).grid(row=4, column=1)
Button(root, text="9", bg="pink", command = lambda :get_variables(9)).grid(row=4, column=2)

#adding other buttons to the calculator
Button(root, text="AC", bg="pink", command = lambda :clear_all()).grid(row=5, column=0)
Button(root, text="0", bg="pink", command = lambda :get_variables(0)).grid(row=5, column=1)
Button(root, text="=", bg="pink", command = lambda :calculate()).grid(row=5, column=2)

#adding operation buttons
Button(root, text="+", bg="pink", command = lambda :get_operation("+")).grid(row=2, column=3)
Button(root, text="-", bg="pink", command = lambda :get_operation("-")).grid(row=3, column=3)
Button(root, text="*", bg="pink", command = lambda :get_operation("*")).grid(row=4, column=3)
Button(root, text="/", bg="pink", command = lambda :get_operation("/")).grid(row=5, column=3)

#adding new operations
Button(root, text="pi", bg="pink", command = lambda :get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="%", bg="pink", command = lambda :get_operation("%")).grid(row=3, column=4)
Button(root, text="(", bg="pink", command = lambda :get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", bg="pink", command = lambda :get_operation("**")).grid(row=5, column=4)

#adding other operations
Button(root, text="<-", bg="pink", command = lambda :undo()).grid(row=2, column=5)
Button(root, text="X!", bg="pink", command = factorial).grid(row=3, column=5)
Button(root, text=")", bg="pink", command = lambda :get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", bg="pink", command = lambda :get_operation("*2")).grid(row=5, column=5)


root.mainloop()