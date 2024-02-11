import tkinter as tk
from tkinter import ttk

class Particle:
    def __init__(self, charge, mass):
        self.charge = charge  # Carga da partícula em unidades de carga elementar
        self.mass = mass  # Massa da partícula em unidades de massa de elétron

class ElectricField:
    def __init__(self):
        self.strength = 1.0  # Força do campo elétrico

    def force_on_particle(self, particle):
        return particle.charge * self.strength

def calcular_forcas():
    # Criar partículas
    electron = Particle(charge=-1, mass=1)
    proton = Particle(charge=1, mass=1836)  # Massa do próton em unidades de massa do elétron

    # Criar campo elétrico
    electric_field = ElectricField()

    # Calcular força sobre as partículas
    force_on_electron = electric_field.force_on_particle(electron)
    force_on_proton = electric_field.force_on_particle(proton)

    # Atualizar os rótulos
    label_electron.config(text="Força no elétron: {:.2f}".format(force_on_electron))
    label_proton.config(text="Força no próton: {:.2f}".format(force_on_proton))

# Criar a janela principal
root = tk.Tk()
root.title("Força Elétrica")

# Criar rótulos para exibir as informações
label_electron = ttk.Label(root, text="")
label_electron.pack(pady=5)
label_proton = ttk.Label(root, text="")
label_proton.pack(pady=5)

# Botão para calcular as forças
calculate_button = ttk.Button(root, text="Calcular Forças", command=calcular_forcas)
calculate_button.pack(pady=10)

# Rodar o loop da interface gráfica
root.mainloop()