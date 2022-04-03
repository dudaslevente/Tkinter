import math
from tkinter import *

from setuptools import Command 
foablak = Tk() 
def terfogat(): 
    r = float(elsomezo.get()) 
    m = float(masodikmezo.get()) 
    c = math.pi*r*r*m 
    negyedikmezo.delete(0, END) 
    negyedikmezo.insert(0, ''+str("%.0f" % c)) 
    

def liter(): 
    a=float(elsomezo.get()) 
    b=float(negyedikmezo.get()) 
    c=b-a 
    otodikmezo.delete(0, END) 
    otodikmezo.insert(0, ''+str("%.0f" % c))



elso=Label(foablak, text='Hány liter?', ) 
elso.grid(row=1, column=1) 
elsomezo=Entry(foablak) 
elsomezo.grid(row=1, column=2) 
masodik=Label(foablak, text='Milyen hosszú a sugara? (cm)') 
masodik.grid(row=2, column=1) 
masodikmezo=Entry(foablak) 
masodikmezo.grid(row=2, column=2)
harmadik=Label(foablak, text='Milyen magas a hordó? (cm)') 
harmadik.grid(row=3, column=1) 
harmadikmezo=Entry(foablak) 
harmadikmezo.grid(row=3, column=2) 
gomb=Button(foablak, text='Kiszámít', command=terfogat) 
gomb.grid(row=4, column=2) 
'''
eredmeny=Label(foablak, text='Térfogat') 
eredmeny.grid(row=5, column=1) 
eredmenymezo=Entry(foablak) 
eredmenymezo.grid(row=5, column=2) 
'''
negyedikmezo=Entry(foablak)
negyedikmezo.grid(row=5, column=2) 
negyedik=Label(foablak, text='Hordó (l)') 
negyedik.grid(row=5, column=1) 
#Hordo=50 
otodik=Label(foablak, text='Mennyi fér még bele? (l)') 
otodik.grid(row=6, column=1)
otodikmezo=Entry(foablak) 
otodikmezo.grid(row=6, column=2)

gomb3=Button(foablak, text='Kivonás', command=liter) 
gomb3.grid(row=9, column=2) 


foablak.mainloop()



'''
def terfogat():
    a=float(mezo1.get())
    b=float(mezo2.get())
    c=float(mezo3.get())
    d=math.pi*pow(a,2)*b
    mezo4.delete(0, END)
    mezo4.insert(0,+float("%.0f" % d))
'''