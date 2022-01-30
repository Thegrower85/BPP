import tkinter as tk
from aplicacion import Aplicacion
"""
En este módulo ejecutamos los métodos para
el loop principal de la aplicación
"""


"""
Generamos el objeto Tk
"""
raiz=tk.Tk()


"""
Le damos un título a la aplicación
"""
raiz.title("Finanzas")


"""
Definimos el tamaño de la ventana
"""
raiz.geometry("1200x500")


"""
Bloqueamos la opción de cambiar el tamaño
de la ventana
"""
raiz.resizable(False,False)


"""
Generamos el objeto de la clase Aplicacion, definida en el
módulo aplicacion, donde se define la GUI.
"""
app = Aplicacion(raiz)


"""
Ejecutamos el loop principal de la aplicacion
"""
app.mainloop()
