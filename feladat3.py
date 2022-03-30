from tkinter import * 
foablak = Tk() 
def terfogat(): 
    r = int(elsomezo.get()) 
    m = int(masodik.get()) 
    c = 3.14*r*r*m 
    negyedik.delete(0, END) 
    negyedik.insert(0, ''+str(c)+'cm2') 

def liter(): 
    a=int(elsomezo.get()) 
    b=(Hordo) 
    c=b-a 
    


elso=Label(foablak, text='Hány liter?', ) 
elso.grid(row=1, column=1) 
elsomezo=Entry(foablak) 
elsomezo.grid(row=1, column=2) 
masodikmezo=Label(foablak, text='Milyen hosszú a sugara? (cm)') 
masodikmezo.grid(row=2, column=1) 
masodik=Entry(foablak) 
masodik.grid(row=2, column=2)
harmadikmezo=Label(foablak, text='Milyen magas a hordó? (cm)') 
harmadikmezo.grid(row=3, column=1) 
harmadik=Entry(foablak) 
harmadik.grid(row=3, column=2) 
gomb=Button(foablak, text='Kiszámít', command=terfogat) 
gomb.grid(row=4, column=2) 
eredmeny=Label(foablak, text='Térfogat') 
eredmeny.grid(row=5, column=1) 
eredmenymezo=Entry(foablak) 
eredmenymezo.grid(row=5, column=2) 
negyedik=Entry(foablak)
negyedik.grid(row=6, column=2) 
gomb2=Label(foablak, text='Liter') 
gomb2.grid(row=6, column=1) 
Hordo=50 
otodik.delete(0, END) 
otodik.insert(0, 'Ennyi fér még bele: '+str(c)) 
otodik=Entry(foablak) 
otodik.grid(row=4, column=1)

gomb3=Button(foablak, text='Kivonás', command=liter) 
gomb3.grid(row=8, column=2) 
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