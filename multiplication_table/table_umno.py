from tkinter import *

win = Tk()
win.geometry("550x400")
win.title("Table")

def clear():
    input_number.delete(0, END)
    input_number.focus()
    out_put.delete(0, END)

def view_times():
    num = input_number.get()
    for i in range(13):
        row = f"{i} x {num} = {int(i)*int(num)}"
        out_put.insert(END, row)
    input_number.delete(0, END)
    input_number.focus()


lbl_enter_number = Label(text="Enter a number: ")
lbl_enter_number.place(x=40, y=30)

input_number = Entry()
input_number.place(x=150, y=30,width = 185, height = 30)
input_number.focus()

out_put = Listbox()
out_put.place(x=150,y=70)

btn_view = Button(text="View Times Table", command=view_times)
btn_view.place(x=350, y=30, width = 150, height = 30)

btn_clear = Button(text="Clear", command=clear)
btn_clear.place(x=350, y=70, width = 150, height = 30)
win.mainloop()
