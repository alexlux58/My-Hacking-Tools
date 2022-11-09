from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learning TKinter")
root.iconbitmap('python_icon.ico')


frame = LabelFrame(root, text="This is my frame", padx=5, pady=5)
frame.pack(padx=10,pady=10)



image = ImageTk.PhotoImage(Image.open("python_icon.png"))
image_label = Label(image=image)
image_label.pack()

# Label widget

label2 = Label(frame, text="hello again")
label2.pack()

r = IntVar()
# r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
]

pizza = StringVar()
pizza.set("Pepperoni")

def clicked(value):
    myLabel = Label(frame, text=value)
    myLabel.pack()

Radiobutton(frame, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(frame, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()


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

exit = Button(root, text="Exit", command=root.quit)
exit.pack()

def popup():
    # showinfo(), showwarning(), showerror, askquestion, askokcancel, askyesno
    messagebox.showinfo("This is my popup", "hello")
    
Button(root, text="Popup", command=popup).pack()

# TODO 
# back() forward() buttons
# Button(root, text="", command=Lambda: forward/back())


root.mainloop()