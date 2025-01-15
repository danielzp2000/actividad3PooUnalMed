class SalarioEmpleado:
    def __init__(self, horas, tarifa, retencion):
        self.horas_trabajadas = horas
        self.tarifa_hora = tarifa
        self.porcentaje_retencion = retencion

    def calcular_salario_bruto(self):
        bruto = self.horas_trabajadas * self.tarifa_hora
        return bruto

    def calcular_salario_neto(self):
        bruto = self.calcular_salario_bruto()
        neto = bruto - (self.porcentaje_retencion * bruto)
        return neto
import tkinter as tk
from tkinter import messagebox
    
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Salarios")

        # Campos de entrada
        tk.Label(self, text="Código Empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.txt_codigo_empleado = tk.Entry(self)
        self.txt_codigo_empleado.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Horas Trabajadas:").grid(row=2, column=0, padx=10, pady=5)
        self.txt_horas_trabajadas = tk.Entry(self)
        self.txt_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Tarifa por Hora:").grid(row=3, column=0, padx=10, pady=5)
        self.txt_tarifa_hora = tk.Entry(self)
        self.txt_tarifa_hora.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Retención Fuente (%):").grid(row=4, column=0, padx=10, pady=5)
        self.txt_retencion_fuente = tk.Entry(self)
        self.txt_retencion_fuente.grid(row=4, column=1, padx=10, pady=5)

        # Botones
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self, text="Borrar", command=self.borrar).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self, text="Salir", command=self.salir).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Campos de salida
        tk.Label(self, text="Código:").grid(row=7, column=0, padx=10, pady=5)
        self.txt_codigo = tk.Entry(self, state="readonly")
        self.txt_codigo.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(self, text="Nombre:").grid(row=8, column=0, padx=10, pady=5)
        self.txt_nombre_dos = tk.Entry(self, state="readonly")
        self.txt_nombre_dos.grid(row=8, column=1, padx=10, pady=5)

        tk.Label(self, text="Salario Bruto:").grid(row=9, column=0, padx=10, pady=5)
        self.txt_salario_bruto = tk.Entry(self, state="readonly")
        self.txt_salario_bruto.grid(row=9, column=1, padx=10, pady=5)

        tk.Label(self, text="Salario Neto:").grid(row=10, column=0, padx=10, pady=5)
        self.txt_salario_neto = tk.Entry(self, state="readonly")
        self.txt_salario_neto.grid(row=10, column=1, padx=10, pady=5)

    # Método para calcular los salarios
    def calcular(self):
        try:
            codigo = self.txt_codigo_empleado.get()
            nombre = self.txt_nombre.get()
            horas = float(self.txt_horas_trabajadas.get())
            tarifa = float(self.txt_tarifa_hora.get())
            retencion = float(self.txt_retencion_fuente.get()) / 100

            empleado = SalarioEmpleado(horas, tarifa, retencion)
            salario_bruto = empleado.calcular_salario_bruto()
            salario_neto = empleado.calcular_salario_neto()

            # Mostrar resultados en los campos de salida
            self.txt_codigo.config(state="normal")
            self.txt_codigo.delete(0, tk.END)
            self.txt_codigo.insert(0, codigo)
            self.txt_codigo.config(state="readonly")

            self.txt_nombre_dos.config(state="normal")
            self.txt_nombre_dos.delete(0, tk.END)
            self.txt_nombre_dos.insert(0, nombre)
            self.txt_nombre_dos.config(state="readonly")

            self.txt_salario_bruto.config(state="normal")
            self.txt_salario_bruto.delete(0, tk.END)
            self.txt_salario_bruto.insert(0, f"{salario_bruto:.2f}")
            self.txt_salario_bruto.config(state="readonly")

            self.txt_salario_neto.config(state="normal")
            self.txt_salario_neto.delete(0, tk.END)
            self.txt_salario_neto.insert(0, f"{salario_neto:.2f}")
            self.txt_salario_neto.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos.")

    # Método para borrar los campos de entrada y salida
    def borrar(self):
        self.txt_codigo_empleado.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_horas_trabajadas.delete(0, tk.END)
        self.txt_tarifa_hora.delete(0, tk.END)
        self.txt_retencion_fuente.delete(0, tk.END)

        self.txt_codigo.config(state="normal")
        self.txt_codigo.delete(0, tk.END)
        self.txt_codigo.config(state="readonly")

        self.txt_nombre_dos.config(state="normal")
        self.txt_nombre_dos.delete(0, tk.END)
        self.txt_nombre_dos.config(state="readonly")

        self.txt_salario_bruto.config(state="normal")
        self.txt_salario_bruto.delete(0, tk.END)
        self.txt_salario_bruto.config(state="readonly")

        self.txt_salario_neto.config(state="normal")
        self.txt_salario_neto.delete(0, tk.END)
        self.txt_salario_neto.config(state="readonly")

    # Método para salir de la aplicación
    def salir(self):
        self.destroy()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
