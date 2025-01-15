import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

#INTERFAZ GRÁFICA

import tkinter as tk
from tkinter import messagebox

class InterfazCirculo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Círculo")

        # Campo para ingresar el radio
        tk.Label(self, text="Radio:").grid(row=0, column=0, padx=10, pady=10)
        self.txt_radio = tk.Entry(self)
        self.txt_radio.grid(row=0, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=1, column=1, padx=10, pady=10)
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
            radio = float(self.txt_radio.get())
            if radio < 0:
                messagebox.showerror("Error", "El radio no puede ser negativo.")
                return

            circulo = Circulo(radio)
            area = circulo.calcular_area()
            perimetro = circulo.calcular_perimetro()

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
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido para el radio.")

    def limpiar(self):
        self.txt_radio.delete(0, tk.END)

        self.txt_area.config(state="normal")
        self.txt_area.delete(0, tk.END)
        self.txt_area.config(state="readonly")

        self.txt_perimetro.config(state="normal")
        self.txt_perimetro.delete(0, tk.END)
        self.txt_perimetro.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = InterfazCirculo()
    app.mainloop()
