import math
from tkinter import *

canvas_width = 500
canvas_height = 500
root = Tk()
w = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

#def Pressed():                         
#        print ('buttons are cool')        
y = canvas_height*3/4
#points = [0,y,canvas_width,y]
w.create_line([0,y,canvas_width,y], width=1)
x = 50
l = 20
ang = math.pi/3
w.create_rectangle(x, y-20, x+40, y, fill='white')
w.create_line(x+20, y-20, x+20+l*math.cos(ang), y-20-l*math.sin(ang), width=4)

                          
#button = Button(root, text = 'Draw', command = Pressed)
#button.pack(pady=20, padx = 20)
#Pressed()

root.mainloop()
