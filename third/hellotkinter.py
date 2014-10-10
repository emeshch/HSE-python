from tkinter import *
 
def Pressed():                         
        print ('buttons are cool')

root = Tk()                             
button = Button(root, text = 'Press', command = Pressed)
button.pack(pady=20, padx = 20)
Pressed()
root.mainloop() 
