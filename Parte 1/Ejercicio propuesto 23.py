import math

class CalculoEcuacion:
    def __init__(self, a, b, c):
        self.valor_a = a
        self.valor_b = b
        self.valor_c = c

    def calcular_solucion_ecuacion(self):
        discriminante = self.calcular_discriminante()
        if discriminante > 0:
            x1 = (-self.valor_b + math.sqrt(discriminante)) / (2 * self.valor_a)
            x2 = (-self.valor_b - math.sqrt(discriminante)) / (2 * self.valor_a)
            return f"Las soluciones son: {x1:.2f} y {x2:.2f}"
        elif discriminante == 0:
            x = -self.valor_b / (2 * self.valor_a)
            return f"La solución es: {x:.2f}"
        else:
            return "No tiene soluciones reales"

    def calcular_discriminante(self):
        return (self.valor_b ** 2) - (4 * self.valor_a * self.valor_c)


#INTERFAZ GRÁFICA:

import tkinter as tk
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Ecuación Cuadrática")

        # Campos de entrada para los valores A, B y C
        tk.Label(self, text="Valor A:").grid(row=0, column=0, padx=10, pady=5)
        self.txt_a = tk.Entry(self)
        self.txt_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Valor B:").grid(row=1, column=0, padx=10, pady=5)
        self.txt_b = tk.Entry(self)
        self.txt_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Valor C:").grid(row=2, column=0, padx=10, pady=5)
        self.txt_c = tk.Entry(self)
        self.txt_c.grid(row=2, column=1, padx=10, pady=5)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text="Borrar", command=self.borrar).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Campo de salida para mostrar el resultado
        tk.Label(self, text="Resultado:").grid(row=5, column=0, padx=10, pady=5)
        self.txt_resultado = tk.Entry(self, state="readonly", width=50)  # Se agrega width=50
        self.txt_resultado.grid(row=5, column=1, padx=10, pady=5)

    def calcular(self):
        try:
            a = float(self.txt_a.get())
            b = float(self.txt_b.get())
            c = float(self.txt_c.get())

            if a == 0:
                messagebox.showerror("Error", "El valor de 'A' no puede ser cero en una ecuación cuadrática.")
                return

            ecuacion = CalculoEcuacion(a, b, c)
            resultado = ecuacion.calcular_solucion_ecuacion()

            # Mostrar el resultado
            self.txt_resultado.config(state="normal")
            self.txt_resultado.delete(0, tk.END)
            self.txt_resultado.insert(0, resultado)
            self.txt_resultado.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    def borrar(self):
        self.txt_a.delete(0, tk.END)
        self.txt_b.delete(0, tk.END)
        self.txt_c.delete(0, tk.END)

        self.txt_resultado.config(state="normal")
        self.txt_resultado.delete(0, tk.END)
        self.txt_resultado.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
