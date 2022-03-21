from tkinter import *
import math
def osszeg():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a+b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg:'+str(c))

def szorzas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a*b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg:'+str(c))

def osztas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a/b if b!=0 else "Hiba!"
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg:'+str(c))

def kivonas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a-b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg:'+str(c))

def gyokvonas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=math.sqrt(a)
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg:'+str(c))

def negyzetre():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a*a
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg:'+str(c))


foablak=Tk()
cimke=Label(foablak, text="Üdvözlet!",fg="blue")
cimke.grid(row=0, column=1)
gomb1=Button(foablak, text='Első szám:')
gomb1.grid(row=1, column=1)
gomb2=Button(foablak, text='Második szám:')
gomb2.grid(row=2, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=4)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=4)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=4)
gomb4=Button(foablak, text='Összead', command=osszeg)
gomb4.grid(row=4, column=4)
gomb5=Button(foablak, text='Szorzás', command=szorzas)
gomb5.grid(row=5, column=4)
gomb6=Button(foablak, text='Osztás', command=osztas)
gomb6.grid(row=6, column=4)
gomb7=Button(foablak, text='Kivonás', command=kivonas)
gomb7.grid(row=7, column=4)
gomb3=Button(foablak, text='Kilépés', command=foablak.destroy)
gomb3.grid(row=12, column=5)



can1=Canvas(foablak, width=300, height=200, bg='white')
photo=PhotoImage(file='cica.gif')
item=can1.create_image(80, 80, image=photo)
can1.grid(row=8, column=1)


foablak.mainloop()








#gomb8=Button(foablak, text='Gyökvonás', command=gyokvonas)
#gomb8.pack()
#gomb9=Button(foablak, text='Négyzetre emelés', command=negyzetre)
#gomb9.pack()