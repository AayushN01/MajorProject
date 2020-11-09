import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import cv2

root = tk.Tk()
root.title('Fake Currency Detection')
#root.iconbitmap('class.ico')
#root.resizable(False, False)
tit = tk.Label(root, text="Fake Currency Detection", padx=25, pady=6, font=("", 12)).pack()
canvas = tk.Canvas(root, height=500, width=500, bg='grey')
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 150 # Processing image for dysplaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()

chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10,
                        fg="black", bg="grey", command=load_img)
chose_image.pack(side=tk.LEFT)
# class_image = tk.Button(root, text='Classify Image',
#                         padx=35, pady=10,
#                         fg="white", bg="grey", command=classify)
# class_image.pack(side=tk.RIGHT)


button_quit = tk.Button(root, text="Exit",
                        padx=35, pady=10,
                        bg='grey', fg='black', command=root.quit)
button_quit.pack(side=tk.LEFT)
root.mainloop()