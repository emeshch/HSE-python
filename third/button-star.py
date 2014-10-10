from tkinter import *

canvas_width = 500
canvas_height = 500
root = Tk()
w = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

def Pressed():                         
        print ('buttons are cool')
        
        x = 100
        points = [x, x+20, x+5, x+5, x+20, x, x+5, x-5, x, x-20, x-5, x-5, x-20, x, x-5, x+5]
        w.create_polygon(points, outline="#476042", fill='yellow', width=1)
                             
button = Button(root, text = 'Press', command = Pressed)
button.pack(pady=20, padx = 20)
#Pressed()

root.mainloop()
