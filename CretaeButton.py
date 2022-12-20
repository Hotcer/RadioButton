import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tk.IntVar()

def seleccionar():

    if seleccionado.get() == 1:
        mostrarResultado.config(text='')

    elif seleccionado.get() == 2:
        mostrarResultado.config(text='')

    elif seleccionado.get() == 3:
        mostrarResultado.config(text='')

    elif seleccionado.get() == 4:
        mostrarResultado.config(text='')

def borrarOpcion():

    seleccionado.set(None)
    mostrarResultado.config(text='')

Button1 = ttk.Radiobutton(window, text='Ubuntu', variable=seleccionado, value=1, command=seleccionar)
Button2 = ttk.Radiobutton(window, text='Mint', variable=seleccionado, value=2, command=seleccionar)
Button3 = ttk.Radiobutton(window, text='Zorin', variable=seleccionado, value=3, command=seleccionar)
Button4 = ttk.Radiobutton(window, text='Manjaro', variable=seleccionado, value=4, command=seleccionar)

Button1.grid(column=0, row=1, padx=5, pady=5)
Button2.grid(column=0, row=2, padx=5, pady=5)
Button3.grid(column=0, row=3, padx=5, pady=5)
Button4.grid(column=0, row=4, padx=5, pady=5)

botonOk = ttk.Button(window, text="Reset", command=borrarOpcion)
botonOk.place(x=5, y=140)


mostrarResultado = tk.Label(window)
mostrarResultado.grid(column=0, row=7, sticky='s')

window.mainloop()
