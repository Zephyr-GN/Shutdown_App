from tkinter import *
import os

root = Tk()
root.title("Shutdown App")
root.geometry("400x580")

def restarttime():
    os.system("shutdown /r /t 30")
def restart():
    os.system("shutdown /r /t 1")
def shutdown():
    os.system("shutdown /s /t 1")
def logout():
    os.system("shutdown -1")

#Primer boton
restart_time_button=PhotoImage(file="restart time.png")

first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2", command=restarttime)
first_button.place(x=10,y=10)

#Segundo boton
close_button=PhotoImage(file="close.png")

second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2", command=root.destroy)
second_button.place(x=200,y=10)

#Tercer boton
restart_button=PhotoImage(file="restart.png")

thrid_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2", command=restart)
thrid_button.place(x=10,y=200)

#Cuarto boton
shutdown_button=PhotoImage(file="shutdown.png")

fouth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2", command=shutdown)
fouth_button.place(x=200,y=200)

#Quinto boton
logout_button=PhotoImage(file="log out.png")

five_button=Button(root,image=logout_button,borderwidth=0,cursor="hand2", command=logout)
five_button.place(x=10,y=400)

root.mainloop()