from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learning TKinter")
root.iconbitmap('python_icon.ico')
root.geometry("800x800")

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
    response = messagebox.showinfo("This is my popup", "hello")
    Label(root, text=response).pack()
    
Button(root, text="Popup", command=popup).pack()

def open():
    top = Toplevel()
    lbl = Label(top, text="hello").pack()
    myImg = ImageTk.PhotoImage(Image.open("python_icon.png"))
    image_label2 = Label(top, image=myImg)
    image_label2.pack(padx=10,pady=10)
    close_btn = Button(top, text="Close", command=top.destroy)
    close_btn.pack()
    root.filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    lbl = Label(top, text=root.filename).pack()
    myImg = ImageTk.PhotoImage(Image.open(root.filename))
    img_lbl = Label(top, image=myImg)
    img_lbl.pack()

open_btn = Button(root, text="Open second window", command=open).pack()

# TODO 
# back() forward() buttons
# Button(root, text="", command=Lambda: forward/back())

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    my_label = Label(root, text=vertical.get()).pack()
    
my_btn = Button(root, text="slide value", command=slide).pack()

var = StringVar()
c_b = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c_b.deselect()
c_b.pack()

def show(v):
    myLabel = Label(root, text=v.get()).pack()
    
showbtn = Button(root, text="Show", command=show).pack()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
drop.pack()

root.mainloop()