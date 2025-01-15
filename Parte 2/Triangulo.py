import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"


#Interfaz Gráfica:

import tkinter as tk
from tkinter import messagebox

class InterfazTriangulo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Triángulo Rectángulo")

        # Campos para ingresar la base y la altura
        tk.Label(self, text="Base:").grid(row=0, column=0, padx=10, pady=10)
        self.txt_base = tk.Entry(self)
        self.txt_base.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Altura:").grid(row=1, column=0, padx=10, pady=10)
        self.txt_altura = tk.Entry(self)
        self.txt_altura.grid(row=1, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Campos de salida para área, perímetro, hipotenusa y tipo de triángulo
        tk.Label(self, text="Área:").grid(row=4, column=0, padx=10, pady=10)
        self.txt_area = tk.Entry(self, state="readonly")
        self.txt_area.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self, text="Perímetro:").grid(row=5, column=0, padx=10, pady=10)
        self.txt_perimetro = tk.Entry(self, state="readonly")
        self.txt_perimetro.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self, text="Hipotenusa:").grid(row=6, column=0, padx=10, pady=10)
        self.txt_hipotenusa = tk.Entry(self, state="readonly")
        self.txt_hipotenusa.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(self, text="Tipo de Triángulo:").grid(row=7, column=0, padx=10, pady=10)
        self.txt_tipo_triangulo = tk.Entry(self, state="readonly")
        self.txt_tipo_triangulo.grid(row=7, column=1, padx=10, pady=10)

    def calcular(self):
        try:
            base = float(self.txt_base.get())
            altura = float(self.txt_altura.get())

            if base <= 0 or altura <= 0:
                messagebox.showerror("Error", "La base y la altura deben ser mayores que cero.")
                return

            triangulo = TrianguloRectangulo(base, altura)
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            hipotenusa = triangulo.calcular_hipotenusa()
            tipo_triangulo = triangulo.determinar_tipo_triangulo()

            # Mostrar resultados
            self.txt_area.config(state="normal")
            self.txt_area.delete(0, tk.END)
            self.txt_area.insert(0, f"{area:.2f}")
            self.txt_area.config(state="readonly")

            self.txt_perimetro.config(state="normal")
            self.txt_perimetro.delete(0, tk.END)
            self.txt_perimetro.insert(0, f"{perimetro:.2f}")
            self.txt_perimetro.config(state="readonly")

            self.txt_hipotenusa.config(state="normal")
            self.txt_hipotenusa.delete(0, tk.END)
            self.txt_hipotenusa.insert(0, f"{hipotenusa:.2f}")
            self.txt_hipotenusa.config(state="readonly")

            self.txt_tipo_triangulo.config(state="normal")
            self.txt_tipo_triangulo.delete(0, tk.END)
            self.txt_tipo_triangulo.insert(0, tipo_triangulo)
            self.txt_tipo_triangulo.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    def limpiar(self):
        self.txt_base.delete(0, tk.END)
        self.txt_altura.delete(0, tk.END)

        self.txt_area.config(state="normal")
        self.txt_area.delete(0, tk.END)
        self.txt_area.config(state="readonly")

        self.txt_perimetro.config(state="normal")
        self.txt_perimetro.delete(0, tk.END)
        self.txt_perimetro.config(state="readonly")

        self.txt_hipotenusa.config(state="normal")
        self.txt_hipotenusa.delete(0, tk.END)
        self.txt_hipotenusa.config(state="readonly")

        self.txt_tipo_triangulo.config(state="normal")
        self.txt_tipo_triangulo.delete(0, tk.END)
        self.txt_tipo_triangulo.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = InterfazTriangulo()
    app.mainloop()
