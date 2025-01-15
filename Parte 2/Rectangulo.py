class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

# InTERFAZ GRÁFICA

import tkinter as tk
from tkinter import messagebox

class InterfazRectangulo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Rectángulo")

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

        # Campos de salida para área y perímetro
        tk.Label(self, text="Área:").grid(row=4, column=0, padx=10, pady=10)
        self.txt_area = tk.Entry(self, state="readonly")
        self.txt_area.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self, text="Perímetro:").grid(row=5, column=0, padx=10, pady=10)
        self.txt_perimetro = tk.Entry(self, state="readonly")
        self.txt_perimetro.grid(row=5, column=1, padx=10, pady=10)

    def calcular(self):
        try:
            base = float(self.txt_base.get())
            altura = float(self.txt_altura.get())

            if base < 0 or altura < 0:
                messagebox.showerror("Error", "La base y la altura deben ser valores positivos.")
                return

            rectangulo = Rectangulo(base, altura)
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()

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
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos para la base y la altura.")

    def limpiar(self):
        self.txt_base.delete(0, tk.END)
        self.txt_altura.delete(0, tk.END)

        self.txt_area.config(state="normal")
        self.txt_area.delete(0, tk.END)
        self.txt_area.config(state="readonly")

        self.txt_perimetro.config(state="normal")
        self.txt_perimetro.delete(0, tk.END)
        self.txt_perimetro.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = InterfazRectangulo()
    app.mainloop()
