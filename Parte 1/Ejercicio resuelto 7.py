import tkinter as tk
from tkinter import messagebox

# Clase que realiza la comparación entre dos números
class ComparacionValores:
    def __init__(self, numero_a, numero_b):
        self.numero_a = numero_a
        self.numero_b = numero_b

    def determinar_relacion(self):
        if self.numero_a > self.numero_b:
            return "A es mayor que B"
        elif self.numero_a < self.numero_b:
            return "A es menor que B"
        else:
            return "A es igual a B"

# Ventana principal con Tkinter
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Comparación de Valores")

        # Etiquetas y campos de entrada
        tk.Label(self, text="Número A:").grid(row=0, column=0, padx=10, pady=10)
        self.txt_numero_a = tk.Entry(self)
        self.txt_numero_a.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Número B:").grid(row=1, column=0, padx=10, pady=10)
        self.txt_numero_b = tk.Entry(self)
        self.txt_numero_b.grid(row=1, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self, text="Borrar", command=self.borrar).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Campo para mostrar el resultado
        self.txt_resultado = tk.Entry(self, state="readonly")
        self.txt_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Método para calcular la relación
    def calcular(self):
        try:
            numero_a = float(self.txt_numero_a.get())
            numero_b = float(self.txt_numero_b.get())
            comparacion = ComparacionValores(numero_a, numero_b)
            resultado = comparacion.determinar_relacion()
            self.txt_resultado.config(state="normal")
            self.txt_resultado.delete(0, tk.END)
            self.txt_resultado.insert(0, resultado)
            self.txt_resultado.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos.")

    # Método para borrar los campos de texto
    def borrar(self):
        self.txt_numero_a.delete(0, tk.END)
        self.txt_numero_b.delete(0, tk.END)
        self.txt_resultado.config(state="normal")
        self.txt_resultado.delete(0, tk.END)
        self.txt_resultado.config(state="readonly")

    # Método para salir de la aplicación
    def salir(self):
        self.destroy()

# Punto de entrada principal
if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
