import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Primera Aplicación")

# Definir una función que se ejecuta al hacer clic en el botón
def mostrar_mensaje():
    messagebox.showwarning("Hola", "¡Hola, mundo!")

# Crear un botón y agregarlo a la ventana
boton = tk.Button(root, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack(pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()