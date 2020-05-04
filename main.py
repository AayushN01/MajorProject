import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry('1600x1200')
root.title('FAKE CURRENCY DETECTION')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
frame.config(background='blue')
label = Label(frame, text="Fake Currency Detection", bg='blue', font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="abc.png")
background_label = Label(frame, image=filename)
background_label.pack(side=LEFT)


def hel():
    help(cv2)

def Contri():
    tkinter.messagebox.showinfo("Contributors", "\n1. Aayush Niraula\n2. Anjita Kandel\n3. Kopila Chaudhary Tharu\n4. Manish Ojha \n")

def anotherWin():
    tkinter.messagebox.showinfo("About",'Fake Currency Detection \n Made using\n-OpenCv\n-Numpy\n-Tkinter\n-Tensorflow\n In Python 3.8.0')

menu = Menu(root)
root.config(menu=menu)

subm1= Menu(menu)
menu.add_cascade(label="Tools", menu=subm1)
subm1.add_command(label="Open CV Docs", command=hel)
subm1.add_command(label="Tkinter Docs", command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="Info", command=anotherWin)
subm2.add_command(label="Contributors", command=Contri)

def exitt():
    exit()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/currency", title="Select an image", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

button1 = Button(frame, text="Input Image",padx=100, pady= 20, bg='white', fg='black', relief=GROOVE, command=open)
button1.pack()

def convert():
    img= cv2.imread("100.jpg")
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image",gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
button2 = Button(frame, text="Gray Conversion",padx=89, pady= 20, bg='white', fg='black', relief=GROOVE, command=convert)
button2.pack()

def resize():
    img = cv2.imread("100.jpg",0)
    cv2.imshow("Gray Image", img)
    cv2.waitKey(0)
    resize = cv2.resize(img,(int(img.shape[1]*1.5), int(img.shape[0]*1.5)))
    cv2.imshow("Resized Image", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

button3 = Button(frame, text="Resized Image",padx=95, pady= 20, bg='white', fg='black', relief=GROOVE, command=resize)
button3.pack()

button_quit = Button(frame, text="Exit",padx=123, pady=20,bg='white', fg='black', relief=GROOVE, command=root.quit)
button_quit.pack()

root.mainloop()