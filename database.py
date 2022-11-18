from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Tkinter GUI w/ Database")
root.iconbitmap('python_icon.png')
root.geometry("600x600")


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
    conn = sqlite3.connect('address_book.db')
    cursr = conn.cursor()
    
    '''
    cursr.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
    '''
    
    cursr.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'state': state.get(),
                      'zipcode': zipcode.get()
                  }
                  )
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
    conn.commit()
    conn.close()
    
def query():
    conn = sqlite3.connect('address_book.db')
    cursr = conn.cursor()
    cursr.execute("SELECT *, oid FROM addresses")
    records = cursr.fetchall()
    # cursr.fetchone()
    # cursr.fetchmany(50)
    print(records)
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    conn.commit()
    conn.close()

submt_btn = Button(root, text="Add Record to Database", command=submit)
submt_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

def delete(name):
    conn = sqlite3.connect('address_book.db')
    cursr = conn.cursor()
    cursr.execute(f"DELETE FROM addresses WHERE first_name='{name}'")
    conn.commit()
    conn.close()
    
entry = Entry(root, width=50)
entry.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
    
delete_btn = Button(root, text="Delete", command=delete(entry.get()))
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()