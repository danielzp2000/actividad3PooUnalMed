import math

class Pitagoras:
    def __init__(self, longitud):
        self.longitud = longitud

    def calcular_ultimo_lado(self):
        medio_lado = self.longitud / 2
        lado = math.sqrt(self.longitud**2 - medio_lado**2)
        return lado

class Operaciones:
    def __init__(self, longitud):
        self.longitud = longitud

    def calcular_area(self):
        pitagoras = Pitagoras(self.longitud)
        altura = pitagoras.calcular_ultimo_lado()
        area = self.longitud * altura / 2
        return area

    def calcular_perimetro(self):
        perimetro = self.longitud * 3
        return perimetro



#INTERFAZ GRÁFICA:

import tkinter as tk
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Triángulo Equilátero")

        # Campo para ingresar la longitud
        tk.Label(self, text="Longitud del lado:").grid(row=0, column=0, padx=10, pady=10)
        self.txt_longitud = tk.Entry(self)
        self.txt_longitud.grid(row=0, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self, text="Borrar", command=self.borrar).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Campos de salida para área y perímetro
        tk.Label(self, text="Área:").grid(row=3, column=0, padx=10, pady=10)
        self.txt_area = tk.Entry(self, state="readonly")
        self.txt_area.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self, text="Perímetro:").grid(row=4, column=0, padx=10, pady=10)
        self.txt_perimetro = tk.Entry(self, state="readonly")
        self.txt_perimetro.grid(row=4, column=1, padx=10, pady=10)

    def calcular(self):
        try:
            longitud = float(self.txt_longitud.get())
            operacion = Operaciones(longitud)
            area = operacion.calcular_area()
            perimetro = operacion.calcular_perimetro()

            # Mostrar resultados
            self.txt_area.config(state="normal")
            self.txt_area.delete(0, tk.END)
            self.txt_area.insert(0, f"{area:.2f}")
            self.txt_area.config(state="readonly")

            self.txt_perimetro.config(state="normal")
            self.txt_perimetro.delete(0, tk.END)
            self.txt_perimetro.insert(0, f"{perimetro:.2f}")
            self.txt_perimetro.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

    def borrar(self):
        self.txt_longitud.delete(0, tk.END)
        self.txt_area.config(state="normal")
        self.txt_area.delete(0, tk.END)
        self.txt_area.config(state="readonly")

        self.txt_perimetro.config(state="normal")
        self.txt_perimetro.delete(0, tk.END)
        self.txt_perimetro.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
