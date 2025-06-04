from tkinter import *
import os

root = Tk()
root.title("Shutdown App")
root.geometry("400x580")

#Primer boton
restart_time_button=PhotoImage(file="restart time.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2")
first_button.place(x=10,y=10)