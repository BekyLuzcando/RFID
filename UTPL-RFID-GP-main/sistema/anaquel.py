#!/usr/bin/python
import math
from matplotlib import pylab
from pylab import *
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import random
from tkinter import messagebox, ttk

from tkinter import *
from matplotlib import image
import matplotlib.image as mpimg
#from tkinter import messagebox as MessageBox
import random, os

import threading
import time


import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema.settings")
django.setup()

from libreria.models import Libro


def five_seconds():
    time.sleep(15)


"""def show_selection(event):
    # Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
        title="Selección",
        message=selection
    )

import tkinter as tk
main_window = tk.Tk()
main_window.geometry('300x200')
main_window.title("Seleccion de sensores")
labelTop = tk.Label(main_window,
                    text = "Escoja el tipo de sensor con el que desea trabajar")
labelTop.grid(column=0, row=0)
combo = ttk.Combobox(
    main_window,
    values=["Monza 4", "Monza x-8k", "Higgs 4"],
    state="readonly"
)

combo.bind("<<ComboboxSelected>>", show_selection)

  

combo.place(x=50, y=50)
main_window.mainloop()"""

from tkinter import messagebox
messagebox.showinfo(message="Se ha detectado un libro faltante en el anaquel (%d)" %random.randint(1, 10), title="Alerta Anaquel / Piso (%d)" %random.randint(1, 3))


def localizacion(a,b,c):
    """se localiza el dispositivo por medio de las
   fuerzas de las senales captadas y de la ubicacion de
   las antenas
    """
    d = 3
    i = 2.5
    j = -4
    #se definen las coordenadas de la Antena A
    ax = 0
    ay = 0
    #se define la cobertura Antena A
    ar = a
    #se definen las coordenadas de la Antena B
    bx = d
    by = 0
    #se definen las coordenadas de la Antena C
    br = b
    cx = i
    cy = j
    #se define la cobertura de la Antena c
    cr = c
    #se localiza la ubicacion del receptor
    x = (ar**2 - br**2 + d**2)/float((2*d))
    y = ((ar**2 + cr**2 + i**2 + j**2)/(2*j))-((float(i/j))*x)
    #messagebox.showinfo(message="El libro 20000143258754125412 esta ubicdo en ", title="Alerta")

    #print ("El libro esta ubicado en -> (%s,%s)" %(x, y))

    libros = Libro.objects.all().values()
    libros = [servicio['titulo'] for servicio in libros]

    #libros=['Contabilidad general', 'Java, como programar', 'Estadistica', 'Matematicas Discretas']
    for i in range(1):
        #print("Se ha detectado el libro: " , random.choice(libros))
        print("Tiempo de lectura: ", random.randint(0.00, 10.00), "minutos")
        print("Etiqueta: " , random.randint(20000111111111111111, 20000999999999999999))
        print("Ubicacion: A804")
    messagebox.showinfo(message="El libro faltante es: (%s)" %random.choice(libros), title="InfoAnaquel")
    messagebox.showinfo(message="El libro esta ubicado en -> (%s,%s)" %(x, y), title="Respuesta Entorno-Anaquel")
    
    
    #grafica
    a = subplot(111, aspect='equal')
    e = Ellipse((ax,ay), ar*2, ar*2, 0)
    e.set_clip_box(a.bbox)
    e.set_color('green')
    e.set_alpha(0.1)
    a.add_patch(e)
    a.annotate("Antena A",
               xy=(ax, ay), xycoords='data',
               xytext=(ax-3, ay+3), textcoords='data',
               arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3"), 
               )
    a.plot(ax,ay, "g^", mew=2, ms=12)
    a.add_artist(e)
    e = Ellipse((bx,by), 2*br,2*br, 0)
    e.set_clip_box(a.bbox)
    e.set_color('red')
    e.set_alpha(0.1)
    a.add_patch(e)
    a.annotate("Antena B",
               xy=(bx, by), xycoords='data',
               xytext=(bx+3, by+3), textcoords='data',
               arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3"))
    a.plot(bx,by, "r^", mew=2, ms=12)
    a.add_artist(e)
    e = Ellipse((cx,cy), 2*cr, 2*cr, 0)
    e.set_clip_box(a.bbox)
    e.set_color('blue')
    e.set_alpha(0.1)
    a.add_patch(e)
    a.annotate("Antena C",
               xy=(cx, cy), xycoords='data',
               xytext=(bx+3.5, by-6), textcoords='data',
               arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3"))
    a.plot(cx,cy, "b^", mew=2, ms=12)
    a.add_artist(e)
    a.plot(x,y, 'k*', mew=3, ms=12)

    #fig = plt.figure()

    #a = fig.add_subplot(111)
    
    #a = plt.subplots()
    #plt.plot(200, 350, marker='v', color="white") 
    
    
    xlim(-20, 20)
    ylim(-20, 20)
    #imagen sola
    #img = plt.imread(r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\mapa3.png')
    
    #fig, a = plt.subplots()
    #a = plt.axes()

    #imagen Random
    path1 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\compus.png'
    path2 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\cubiculos1PA.png'
    path3 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\estudiantes1PA.png'
    path4 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\estudiantes2PA.png'
    path5 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\estudiantesPB.png'
    path6 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\grupos1PA.png'
    path7 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\grupos2PA.png'
    path8 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\hall.png'
    path9 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\hall1PA.png'
    path10 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\hall2PA.png'
    path11 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\ingles.png'
    #path12 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\procesosPB.png'
    #path13 = r'C:\Users\bekyl\OneDrive\Documentos\visual\imagenes\tesisPB.png'
    
    ran = ([path1, path2, path3, path4, path5, path6, path7, path8, path9, path10,path11])
    
    try:
        img = plt.imread(random.choice(ran))
    


    #plt.imshow(img)
    #plt.show()
    #coordenadas izq, der, up, down
        ext=[-20, 20, -20, 20]
        a.imshow(img, extent=ext)

        aspect=img.shape[0]/float(img.shape[1])*((ext[1]-ext[0])/(ext[3]-ext[2]))
    
    #print(img)
        print(a is plt.gca())
        show()  
    
    except:

        print('ss')

def main():
    """funcion principal
    """
    
    try:
        ar = random.randint(1, 10)
        br = random.randint(1, 10)
        cr = random.randint(1, 10)
    except:
        print ("No seleccionaste las fuerzas de senal")
        return

    print ("El dispositivo capta una senal de: ")
    print ("Antena A %s" %ar)
    print ("Antena B %s" %br)
    print ("Antena C %s" %cr)
    localizacion(ar,br,cr)

main()