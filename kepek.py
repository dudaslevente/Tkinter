from tkinter import *
def klikk():
    print('Klikkeltem!')
ablak1=Tk()
ablak1.geometry('450x450')
ablak1.title('IKT!')
gyoker='H:\\IKT projektmunka\\Python\\Képek\\'
icon=PhotoImage(file=gyoker+'Hello.png')
ablak1.iconphoto(True, icon)
ablak1.config(bg='black')
elsokep=PhotoImage(file=gyoker+'Png.png')
gombkep=PhotoImage(file=gyoker+'Png.png')
cimke=Label(ablak1,
            text='Üdvözlet!',
            fg='red',
            bg='pink',
            font=('Arial', 45, 'bold'),
            bd=10,
            relief=RAISED,
            padx=25,
            pady=30,
            compound='bottom').pack()
            
gomb=Button(ablak1,
            text='Kattints!',
            fg='red',
            font=('Comic Sans', 35, 'bold'),
            bg='yellow',
            relief=SUNKEN,
            bd=10,
            command=klikk,
            padx=12,
            pady=12,
            image=gombkep,
            compound='bottom',
            activebackground='blue',
            activeforeground='yellow',
            state=ACTIVE).pack()

ablak1.mainloop()