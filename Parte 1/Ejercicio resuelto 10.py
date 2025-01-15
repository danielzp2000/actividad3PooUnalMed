class CalculoMatricula:
    def __init__(self, patrimonio, estrato):
        self.patrimonio = patrimonio
        self.estrato = estrato
        self.costo_matricula = 50000  # Costo base de la matrícula

    def calcular_pago_matricula(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            self.costo_matricula += 0.03 * self.patrimonio
        return self.costo_matricula
import tkinter as tk
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Matrícula")

        # Etiquetas y campos de entrada
        tk.Label(self, text="Número de Inscripción:").grid(row=0, column=0, padx=10, pady=10)
        self.txt_num_inscripcion = tk.Entry(self)
        self.txt_num_inscripcion.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Nombres:").grid(row=1, column=0, padx=10, pady=10)
        self.txt_nombres = tk.Entry(self)
        self.txt_nombres.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=10)
        self.txt_patrimonio = tk.Entry(self)
        self.txt_patrimonio.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Estrato:").grid(row=3, column=0, padx=10, pady=10)
        self.txt_estrato = tk.Entry(self)
        self.txt_estrato.grid(row=3, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self, text="Borrar", command=self.borrar).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Campos de salida
        tk.Label(self, text="Resultado:").grid(row=6, column=0, padx=10, pady=10)
        self.txt_resultado = tk.Entry(self, state="readonly")
        self.txt_resultado.grid(row=6, column=1, padx=10, pady=10)

    def calcular(self):
        try:
            num_inscripcion = self.txt_num_inscripcion.get()
            nombres = self.txt_nombres.get()
            patrimonio = float(self.txt_patrimonio.get())
            estrato = int(self.txt_estrato.get())

            matricula = CalculoMatricula(patrimonio, estrato)
            pago_matricula = matricula.calcular_pago_matricula()

            resultado = f"Número: {num_inscripcion}\nNombre: {nombres}\nPago Matrícula: ${pago_matricula:.2f}"
            self.txt_resultado.config(state="normal")
            self.txt_resultado.delete(0, tk.END)
            self.txt_resultado.insert(0, f"${pago_matricula:.2f}")
            self.txt_resultado.config(state="readonly")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos para patrimonio y estrato.")

    def borrar(self):
        self.txt_num_inscripcion.delete(0, tk.END)
        self.txt_nombres.delete(0, tk.END)
        self.txt_patrimonio.delete(0, tk.END)
        self.txt_estrato.delete(0, tk.END)
        self.txt_resultado.config(state="normal")
        self.txt_resultado.delete(0, tk.END)
        self.txt_resultado.config(state="readonly")

    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
