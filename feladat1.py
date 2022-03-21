from tkinter import *
foablak=Tk()
kep='H:\\IKT projektmunka\\Python\\Képek\\'
gomb1=Button(foablak, text='Első mező:')
gomb1.grid(row=1, column=1)
gomb2=Button(foablak, text='Második mező:')
gomb2.grid(row=2, column=1)
gomb3=Button(foablak, text='Harmadik mező:')
gomb3.grid(row=3, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=2)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=2)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=2)




can1=Canvas(foablak, width=160, height=160, bg='white')
photo=PhotoImage(file=kep+'images.png')
item=can1.create_image(80, 80, image=photo)
can1.grid(row=2, column=3)






foablak.mainloop()