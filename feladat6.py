from tkinter import *
import  math

def nevjegy():
    abl2=Toplevel(foablak)
    uz2=Message(abl2, text='Készítette: Dudás Levente\nDusnok\n2005.12.09', width=400)
    gomb2=Button(abl2, text='Kilép', command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

def felszin():

    def szamit():
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        c=eval(mezo3.get())
        felszin=2*(a*b+a*c+b*c) if a!=0 and b!=0 and c!=0 else 'Hiba, az egyik adat 0!'
        mezo4.delete(0,END)
        mezo4.insert(0,str(felszin))
    
    abl3=Toplevel(foablak)
    abl3.title('A téglatest felszíne')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='c:')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    mezo4=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=3, column=2, sticky=W)
    mezo4.grid(row=5, column=2, sticky=W)
    gomb2=Button(abl3, text='Kilép', command=abl3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    abl3.mainloop()

def terfogat():

    def szamit():
        a=eval(mezo1.get()) 
        b=eval(mezo2.get())
        c=eval(mezo3.get())
        terfogat=a*b*c if a!=0 and b!=0 and c!=0 else 'Hiba, az egyik adat 0!'
        mezo4.delete(0,END)
        mezo4.insert(0,str(terfogat))

    abl3=Toplevel(foablak)
    abl3.title('A téglatest térfogata')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='c:')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    mezo4=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=3, column=2, sticky=W)
    mezo4.grid(row=5, column=2, sticky=W)
    gomb2=Button(abl3, text='Kilép', command=abl3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    abl3.mainloop()

def hfelszin():
    
    def szamit():
        r=eval(mezo1.get())
        m=eval(mezo2.get())
        hfelszin=2*r*r*math.pi+2*r*math.pi*m if r and m !=0 else 'Hiba, az egyik adat 0!'
        mezo3.delete(0,END)
        mezo3.insert(0, str(hfelszin))
    
    abl3=Toplevel(foablak)
    abl3.title('A henger felszíne')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='Sugár:')
    szoveg2=Label(abl3, text='Magasság:')
    szoveg3=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=5, column=2, sticky=W)
    gomb2=Button(abl3, text='Kilép', command=abl3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    abl3.mainloop()

def hterfogat():
    
    def szamit():
        r=eval(mezo1.get()) 
        m=eval(mezo2.get())
        hterfogat=r*r*math.pi*m if r and m !=0 else 'Hiba, az egyik adat 0!'
        mezo3.delete(0,END)
        mezo3.insert(0,str(hterfogat))

    abl3=Toplevel(foablak)
    abl3.title('A henger térfogata')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='Sugár:')
    szoveg2=Label(abl3, text='Magasság:')
    szoveg3=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=5, column=2, sticky=W)
    gomb2=Button(abl3, text='Kilép', command=abl3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    abl3.mainloop()

foablak=Tk()
foablak.title('A téglatest és a henger adatai')
foablak.minsize(width=300, height=100)

menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text='Fájl', underline=0)
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label="Névjegy", command=nevjegy, underline=0)
fajl.add_command(label="Kilépés", command=foablak.destroy, underline=0)
menu1.config(menu=fajl)

menu2=Menubutton(menusor, text='Téglatest', underline=0)
menu2.pack(side=LEFT)
teglatest=Menu(menu2)
teglatest.add_command(label='Felszín', command=felszin, underline=0)
teglatest.add_command(label='Térfogat', command=terfogat, underline=0)
menu2.config(menu=teglatest)

menu3=Menubutton(menusor, text='Henger', underline=0)
menu3.pack(side=LEFT)
henger=Menu(menu3)
henger.add_command(label='Felszín', command=hfelszin, underline=0)
henger.add_command(label='Térfogat', command=hterfogat, underline=0)
menu3.config(menu=henger)

foablak.mainloop()