#!/usr/bin/python
import math
from re import A
from matplotlib import pylab
from pylab import *
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import random
import threading
import time
from time import sleep

from tkinter import *
from matplotlib import image
import matplotlib.image as mpimg
#from tkinter import messagebox as MessageBox
import random, os
from threading import Timer
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema.settings")
django.setup()

from libreria.models import Libro



def five_seconds():
    time.sleep(15)


class MyInfiniteTimer():
    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)
        
    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()
        
    def start(self):
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()
        
    def cancel(self):
        self.thread.cancel()

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

    from tkinter import messagebox
    messagebox.showinfo(message="Se ha detectado un libro sin aparente uso", title="Alerta-Entorno")

    libros = Libro.objects.all().values()
    libros = [servicio['titulo'] for servicio in libros]
    
    for i in range(1):
        #print("Se ha detectado el libro: " , random.choice(libros))
        print("Tiempo de lectura: ", random.randint(0.00, 10.00), "minutos")
        print("Etiqueta: " , random.randint(20000111111111111111, 20000999999999999999))
        print("Ubicacion: A804")
    #messagebox.showinfo(message="El libro esta ubicado en -> (%s,%s)" %(x, y), title="Found")
    messagebox.showinfo(message="Se ha detectado el libro: (%s)" %random.choice(libros), title="Libro posici??n fija")
    
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
    
    
    ran = ([path1, path2, path3, path4, path5, path6, path7, path8, path9, path10,path11])
    
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

def main():
    """funcion principal
    """
    
    try:
        ar = random.randint(1, 6)
        br = random.randint(1, 5)
        cr = random.randint(1, 6)
    except:
        print ("No seleccionaste las fuerzas de senal")
        return

    print ("El dispositivo capta una senal de: ")
    print ("Antena A %s" %ar)
    print ("Antena B %s" %br)
    print ("Antena C %s" %cr)
    localizacion(ar,br,cr)



main()

t = threading.Timer(3, main)
t.start()



