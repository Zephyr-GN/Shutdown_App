from tkinter import *
import os

root = Tk()
root.title("Shutdown App")
root.geometry("400x580")

#Primer boton
restart_time_button=PhotoImage(file="restart time.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2")
first_button.place(x=10,y=10)

#Segundo boton
close_button=PhotoImage(file="close.png")

second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2")
second_button.place(x=200,y=10)

#Tercer boton
restart_button=PhotoImage(file="restar.png")

thrid_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2")
thrid_button.place(x=10,y=200)

#Cuarto boton
shutdown_button=PhotoImage(file="shutdown.png")

fouth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2")
fouth_button.place(x=200,y=200)

