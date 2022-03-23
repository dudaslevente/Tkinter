from tkinter import *
foablak=Tk()
import math

def terfogat():
    a=float(mezo1.get())
    b=float(mezo2.get())
    c=3.14*a*a*b
    mezo3.delete(0, END)
    mezo3.insert(0, ''+str(c))

def vashenger():
    a=float(mezo1.get())
    b=float(mezo2.get())
    c=a*b*7.8
    mezo4.delete(0, END)
    mezo4.insert(0, ''+str(c))

def fahenger():
    a=float(mezo1.get())
    b=float(mezo2.get())
    c=a*b*0.70
    mezo5.delete(0, END)
    mezo5.insert(0, ''+str(c))


gomb1=Button(foablak, text='Sugár (cm):')
gomb1.grid(row=1, column=1)
gomb2=Button(foablak, text='Magasság (cm):')
gomb2.grid(row=2, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=2)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=2)
gomb3=Button(foablak, text='Kiszámít')
gomb3.grid(row=3, column=3)
gomb3=Button(foablak, text='Térfogat (cm3):', command=terfogat)
gomb3.grid(row=4, column=1)
gomb3=Button(foablak, text='Vashenger (g):', command=vashenger)
gomb3.grid(row=5, column=1)
gomb3=Button(foablak, text='Fahenger (g):', command=fahenger)
gomb3.grid(row=6, column=1)
mezo3=Entry(foablak)
mezo3.grid(row=4, column=2)
mezo4=Entry(foablak)
mezo4.grid(row=5, column=2)
mezo5=Entry(foablak)
mezo5.grid(row=6, column=2)






foablak.mainloop()