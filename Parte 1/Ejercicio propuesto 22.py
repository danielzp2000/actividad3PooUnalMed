class CalculoNomina:
    def __init__(self, horas_trabajadas, valor_hora, nombre):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.nombre = nombre

    def calcular_nomina(self):
        salario = self.horas_trabajadas * self.valor_hora
        if salario < 450000:
            return f"{self.nombre}"
        else:
            return f"{self.nombre}\n{salario:.2f}"

#INTERFAZ GRÁFICA:

import tkinter as tk
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Nómina")

        # Campos de entrada
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Horas Trabajadas:").grid(row=1, column=0, padx=10, pady=5)
        self.txt_horas_mes = tk.Entry(self)
        self.txt_horas_mes.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Valor por Hora:").grid(row=2, column=0, padx=10, pady=5)
        self.txt_valor_hora = tk.Entry(self)
        self.txt_valor_hora.grid(row=2, column=1, padx=10, pady=5)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text="Borrar", command=self.borrar).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Campo de salida
        tk.Label(self, text="Respuesta:").grid(row=5, column=0, padx=10, pady=5)
        self.txt_respuesta = tk.Entry(self, state="readonly")
        self.txt_respuesta.grid(row=5, column=1, padx=10, pady=5)

    def calcular(self):
        try:
            nombre = self.txt_nombre.get()
            horas_trabajadas = float(self.txt_horas_mes.get())
            valor_hora = float(self.txt_valor_hora.get())

            nomina = CalculoNomina(horas_trabajadas, valor_hora, nombre)
            respuesta = nomina.calcular_nomina()

            # Mostrar respuesta en el campo de texto
            self.txt_respuesta.config(state="normal")
            self.txt_respuesta.delete(0, tk.END)
            self.txt_respuesta.insert(0, respuesta)
            self.txt_respuesta.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos para las horas trabajadas y el valor por hora.")

    def borrar(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_horas_mes.delete(0, tk.END)
        self.txt_valor_hora.delete(0, tk.END)

        self.txt_respuesta.config(state="normal")
        self.txt_respuesta.delete(0, tk.END)
        self.txt_respuesta.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
