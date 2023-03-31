from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
import time 
import pygame,sys
from pygame.locals import*
from tkinter import filedialog
pygame.init() 


root=Tk()
root.title("Ejercicio A")
root.geometry("450x600")
ventanaprincipal=Frame(root,width=1000,height=1000,bg="gray")
ventanaprincipal.grid()

def clock():
    HoraReloj=time.strftime("%H")
    MinutosReloj=time.strftime("%M")
    SegundosDeReloj=time.strftime("%S")
    Tiempo=time.strftime(HoraReloj+":"+MinutosReloj+":"+SegundosDeReloj)
    Labelreloj.config(text=Tiempo)
    Labelreloj.after(1000,clock)
    if(HoraReloj==entryhoras.get()):
        if(MinutosReloj==EntryMinutos.get()):
            if(SegundosDeReloj=="00"):
                pygame.mixer.music.play()
                respuesta=MessageBox.askquestion("AskQuestion","Desea pausar la alarma?")
                if(respuesta=="yes"):
                    pygame.mixer.music.stop()

def mostrarmusica():
    cancion=filedialog.askopenfilename()
    pygame.mixer.music.load(cancion)
                    
def alarmaaa():
    MessageBox.showwarning("ShowWarning","Alarma establecida")

def mostraralarma():
     MessageBox.showwarning("ShowWarning",entryhoras.get()+":"+EntryMinutos.get())



LabelTITULO=Label(ventanaprincipal,
            text="ALARMA",
             font=("Times",14,"bold"),
             background="gray",
             foreground="black", 
             width=8,
             height=2, 
             justify=CENTER)
LabelTITULO.place(x=180,y=1)

LabelHORA=Label(ventanaprincipal,
            text="Hora",
             font=("Times",14,"bold"),
             background="gray",
             foreground="black", 
             width=8,
             height=2, 
             justify=CENTER)
LabelHORA.place(x=20,y=100)

entryhoras=StringVar()
entradahoras=Entry(ventanaprincipal,font=("Times",12),textvariable=entryhoras).place(x=160,y=110)
Labelminutos=Label(ventanaprincipal,
            text="Minutos",
             font=("Times",14,"bold"),
             background="gray",
             foreground="black", 
             width=8,
             height=2, 
             justify=CENTER)
Labelminutos.place(x=20,y=200)

EntryMinutos=StringVar()
EntradaMinutos=Entry(ventanaprincipal,font=("Times",12),textvariable=EntryMinutos).place(x=160,y=210)
Labelreloj=Label(ventanaprincipal,
            
             font=("Times",14,"bold"),
             background="gray",
             foreground="black", 
             width=8,
             height=2, 
             justify=CENTER)
Labelreloj.place(x=170,y=50)
ButtonMP3=Button(ventanaprincipal,font=("Times",14,"bold"),text="Seleccionar Musica",command=mostrarmusica).place(x=140,y=350)
ButtonSetAlarma=Button(ventanaprincipal,font=("Times",14,"bold"),text="Confirmar Alarma",command=alarmaaa).place(x=140,y=400)
ButtonRegistrar=Button(ventanaprincipal,font=("Times",14,"bold"),text="Alarma Establecida",command=mostraralarma).place(x=140,y=450)

clock()
root.mainloop()