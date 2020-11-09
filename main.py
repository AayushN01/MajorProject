import tkinter as tk
import numpy
import os
import time
import cv2
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title("Fake Currency Detection")
tit = tk.Label(root, text="FAKE CURRENCY DETECTION", padx=30, pady=15, font=("", 16)).pack()
canvas = tk.Canvas(root, height=500, width=500, bg="grey").pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def hel():
    help(cv2)

def Contri():
    tkinter.messagebox.showinfo("Contributors", "\n1. Aayush Niraula\n2. Anjita Kandel\n3. Kopila Chaudhary Tharu\n4. Manish Ojha \n")

def anotherWin():
    tkinter.messagebox.showinfo("About",'Fake Currency Detection \n Made using\n-OpenCv\n-Numpy\n-Tkinter\n-PyTorch\n In Python 3.8.0')

menu = Menu(root)
root.config(menu=menu)

subm1= Menu(menu)
menu.add_cascade(label="Tools", menu=subm1)
subm1.add_command(label="Open CV Docs", command=hel)
subm1.add_command(label="Tkinter Docs", command=hel)
subm1.add_command(label="Numpy Docs", command=hel)
subm1.add_command(label="PyTorch Docs", command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="Info", command=anotherWin)
subm2.add_command(label="Contributors", command=Contri)

def exitt():
    exit()

def select_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Select an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 250 # Processing image for dysplaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()

select_btn = tk.Button(root, text="Select Image",padx=35, pady= 10, bg='grey', fg='black',command=select_img)
select_btn.pack(side=tk.LEFT)

def select_roi():
    img= cv2.imread(image_data)
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image",gray_img)
    cv2.waitKey(0)
    blur_img =  cv2.GaussianBlur(gray_img,(3,3),cv2.BORDER_DEFAULT) #cv2.GaussianBlur(src_img,(kernel_size), border_type)==Applied to remove noise from gray image
    cv2.imshow("Blurred Image", blur_img)
    cv2.waitKey(0)
    canny = cv2.Canny(blur_img, 20, 150)
    cv2.imshow("Canny Edge Detection", canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
roi_btn = tk.Button(root, text="ROI Selection",padx=35, pady= 10, bg='grey', fg='black',command=select_roi)
roi_btn.pack(side=tk.LEFT)



button_quit = Button(root, text="Exit",padx=35, pady=10,bg='grey', fg='black', relief=GROOVE, command=root.quit)
button_quit.pack(side=tk.RIGHT)

root.mainloop()