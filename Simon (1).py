import tkinter as tk
import random
points = 0
mejor = 0
color = 0
clicks = []
r = random.randint(1,4)
secuencia = []

class Simon:
    def __init__(self):
        self.top = tk.Tk()
        self.top.title("Simon")
        self.top.configure(bg="#0b0c0e")
        self.top.minsize(550,550)
        self.top.resizable(True, True)
        

        tk.Grid.rowconfigure(self.top,0, weight=1)
        tk.Grid.rowconfigure(self.top,1, weight=1)
        tk.Grid.columnconfigure(self.top, 0, weight=1)
        tk.Grid.columnconfigure(self.top, 1, weight=1)

        self.init_buttons()
        self.top.mainloop()
    
    def init_buttons(self):
        # Creamos los botones
        self.azul = tk.Button(bg="#175FAD", activebackground="#337CA0", command = self.clickAzul) # Se crea el boton y se asigna
        self.azul.grid(row=0, column=0, sticky= tk.N + tk.S + tk.E + tk.W) # Posicionamos el boton

        self.rojo = tk.Button(bg= "#D1495B", activebackground= "#FF1D15", command = self.clickRojo)
        self.rojo.grid(row=1, column=0, sticky= tk.N + tk.S + tk.E + tk.W)

        self.amarillo = tk.Button(bg="#F7D117", activebackground="#FFCC1E",command = self.clickAmarillo)
        self.amarillo.grid(row=0, column=1, sticky= tk.N + tk.S + tk.E + tk.W)

        self.verde = tk.Button(bg="#8CC63F", activebackground="green", command = self.clickVerde)
        self.verde.grid(row=1, column=1, sticky= tk.N + tk.S + tk.E + tk.W)

        self.start = tk.Button(text="Iniciar", command=self.mostrarSecuencia)
        self.start.grid(row=3, column=1)

        self.puntos = tk.Label(bg="black", fg="white", text = "Puntos:  ")#preguntar como llamar a la funcion para que vaya sumando puntos
        self.puntos.grid(row=2, column=0)
        
        self.punteo = tk.Label(text = points)
        self.punteo.grid(row=3, column=0)

        self.best = tk.Label(bg="black", fg="white", text="Mejor:  ")
        self.best.grid(row=2, column=1)
       
       
        
        self.top.mainloop()

#Programamos el cambio de color en los botones al momento de hacer click 
#lambda sirve  para hacer una funcion pequeña en una sola linea 
    def clickAmarillo(self):
        self.amarillo.configure(activebackground="#F7D117")
        self.amarillo.after(500, lambda: self.amarillo.configure(activebackground="#FFCC1E"))
        color = 1
        clicks.append(color)
        self.chequearSecuencia()
    
    def clickAzul(self):
        self.azul.configure(activebackground="#175FAD")
        self.azul.after(500, lambda: self.azul.configure(activebackground="#337CA0"))
        color = 2
        clicks.append(color)
        self.chequearSecuencia()
    
    def clickRojo(self):
        self.rojo.configure(activebackground="#D1495B")
        self.rojo.after(500, lambda: self.rojo.configure(activebackground="#FF1D15"))
        color = 3
        clicks.append(color)
        self.chequearSecuencia()

    def clickVerde(self):
        self.verde.configure(activebackground="#8CC63F")
        self.verde.after(500, lambda: self.verde.configure(activebackground="green"))
        color = 4
        clicks.append(color)
        self.chequearSecuencia()

    def chequearSecuencia(self):
        if clicks == secuencia:
            points = points + 1
            self.punteo.configure(text = points)

    
    def mostrarSecuencia(self):
    
        if r == 1:
            self.amarillo.configure(bg="#F7D117")
            self.amarillo.after(1000, lambda: self.amarillo.configure(bg="#FFCC1E"))
            secuencia.append(r)
            self.top.after(3000, chequearSecuencia)
        
        elif r == 2:
            self.azul.configure(bg="#337CA0")
            self.azul.after(1000, lambda: self.azul.configure(bg="#175FAD"))
            secuencia.append(r)
            self.top.after(3000, chequearSecuencia)

        elif r == 3:
            self.rojo.configure(bg="#FF1D15")
            self.rojo.after(1000, lambda: self.rojo.configure(bg="#D1495B"))
            secuencia.append(r)
            self.top.after(3000, chequearSecuencia)
        
        elif r == 4:
            self.verde.configure(bg="green")
            self.verde.after(1000, lambda: self.verde.configure(bg="#8CC63F"))
            secuencia.append(r)
            self.top.after(3000, chequearSecuencia)
    
        self.top.after(2000, mostrarSecuencia)
        self.top.mainloop()

_ = Simon()