from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Tkinter GUI w/ Database")
root.iconbitmap('python_icon.png')
root.geometry("600x600")


conn = sqlite3.connect('address_book.db')

cursr = conn.cursor()
cursr.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    zipcode integer
    )""")


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="ZIP")
zipcode_label.grid(row=5, column=0)

def submit():
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

submt_btn = Button(root, text="Add Record to Database", command=submit)
submt_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


conn.commit()
conn.close()

root.mainloop()