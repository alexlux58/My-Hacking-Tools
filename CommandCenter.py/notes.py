from tkinter import *

root = Tk()
root.title("Learning TKinter")
root.iconbitmap('python_icon.ico')

# Label widget

label2 = Label(root, text="hello again")


# label.pack()
# label.grid(row=0, column=1)
# label2.grid(row=1, column=0)

def ButtonClick():
    label = Label(root, text=entry.get())
    label.pack()

entry = Entry(root, width=50)
entry.pack()
entry.insert(0, "Name: ")

# state=DISABLED (disables the button)
button = Button(root, text="Enter your name", padx=50, pady=50, command=ButtonClick, fg="black", bg="white")
button.pack()


root.mainloop()