from tkinter import *

root=Tk()
root.title("My Calculator")

# Creating entry window
e=Entry(root,width=65, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


# The Methods
def click(number):
  current=e.get()
  e.delete(0,END)
  e.insert(0,str(current) + str(number))

def clear():
  e.delete(0, END)

def add():
  global symbol
  global n1
  n1=int(e.get())
  e.delete(0, END)
  symbol='+'

def subtract():
  global symbol
  global n1
  n1=int(e.get())
  e.delete(0,END)
  symbol='-'

def multiply():
  global symbol
  global n1
  n1=int(e.get())
  e.delete(0,END)
  symbol='*'

def divide():
  global symbol
  global n1
  n1=int(e.get())
  e.delete(0, END)
  symbol='/'

def eq():
  n2=int(e.get())
  e.delete(0, END)
  if symbol=='+':
    e.insert(0, str(n1+n2))
  if symbol=='-':
    e.insert(0, str(n1-n2))
  if symbol=='/':
    e.insert(0, str(int(n1/n2)))
  if symbol=='*':
    e.insert(0, str(n1*n2))


# Define the buttons
b1=Button(root, text="1", padx=40, pady=20,borderwidth=10, command=lambda:click(1))
b2=Button(root, text="2", padx=40, pady=20,borderwidth=10, command=lambda:click(2))
b3=Button(root, text="3", padx=40, pady=20,borderwidth=10, command=lambda:click(3))
b4=Button(root, text="4", padx=40, pady=20,borderwidth=10, command=lambda:click(4))
b5=Button(root, text="5", padx=40, pady=20,borderwidth=10, command=lambda:click(5))
b6=Button(root, text="6", padx=40, pady=20,borderwidth=10, command=lambda:click(6))
b7=Button(root, text="7", padx=40, pady=20,borderwidth=10, command=lambda:click(7))
b8=Button(root, text="8", padx=40, pady=20,borderwidth=10, command=lambda:click(8))
b9=Button(root, text="9", padx=40, pady=20,borderwidth=10, command=lambda:click(9))
b0=Button(root, text="0", padx=40, pady=20,borderwidth=10, command=lambda:click(0))

b_clear=Button(root, text="CLEAR",bg='red', padx=40, pady=20, command=clear)
b_equals=Button(root, text="=", padx=40,bg='green', pady=20, command=eq)

b_plus=Button(root, text="+", padx=50, pady=20,bg="yellow", command=add)
b_sub=Button(root, text="-", padx=50, pady=20,bg="yellow", command=subtract)
b_mul=Button(root, text="*", padx=50, pady=20,bg="yellow", command=multiply)
b_div=Button(root, text="/", padx=50, pady=20,bg="yellow", command=divide)

#b_quit=Button(root, text="Exit",padx=50, pady=20,bg="white",fg="red", command=root.quit)

# Gridding the buttons

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=1)

b_clear.grid(row=4,column=0)
b_equals.grid(row=4,column=2)

b_plus.grid(row=1,column=3)
b_sub.grid(row=2,column=3)
b_mul.grid(row=3,column=3)
b_div.grid(row=4,column=3)


#b_quit.grid(row=0,column=0)

root.mainloop()