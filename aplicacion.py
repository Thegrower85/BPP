import tkinter as tk
import back
import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
"""
En este módulo definimos la clase Aplicacion.
En ella se definen todos lo elementos de la GUI
necesarios para poder manejar los datos de la aplicacion
"""


"""
Definimos la clase Aplicacion
Atributos:
master = Frame
frame_principal = Frame
frame_inferior = Frame
frame_grafico = Frame
muestra = Entry
resultados = lista de diccionarios
"""
class Aplicacion(tk.Frame):


    """
    Método constructor, como la clase hereda de tk.Frame, el constructor
    lo hacemos heredando del constructor de la clase 'padre'.
    Se generan todos los atributos necesarios para que el usuario
    pueda interactuar con la aplicación. También se generan los resultados
    llamando a los métodos del módulo back. quedan cargados en memoria para
    manipularlos desde la GUI.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill ='both')
        self.frame_principal = self.crear_frame_principal()
        self.frame_inferior = self.crear_frame_inferior()
        self.frame_botones = self.crear_frame_botones()
        self.frame_grafico = self.crear_frame_grafico()
        self.muestra = self.crear_muestra()
        MEDIA = back.cargar_archivo()
        df = back.generar_dataframe(MEDIA)
        self.resultados = back.resultados(df)



    """
    Método para cerra la aplicación completamente,
    se asocia al boton salir definido en el frame inferior.
    """
    def cerrar_aplicacion(self):
        self.master.destroy()



    """
    Método para crear el frame principal, en él se anidarán el
    resto de elementos GUI de la aplicacion.
    """
    def crear_frame_principal(self):
        frame_principal = tk.Frame(self, height = 465, width=1200, relief = "sunken", bd=2)
        frame_principal.place(x=0,y=0)
        return frame_principal


    """
    Método para crear el frame inferior, en él se anidará el
    botón de salida de la aplicación, sería un buen lugar
    para colocar un botón de ayuda, por ejemplo.
    """
    def crear_frame_inferior(self):
        frame_inferior = tk.Frame(self,  height = 35, width=1200, relief= "raised", bd=2)
        frame_inferior.place(x=0,y=465)
        boton_salir = tk.Button(frame_inferior, text = "Salir", width = 7, heigh = 1, command=self.cerrar_aplicacion)
        boton_salir.place(x=1115,y=3)
        return frame_inferior


    """
    Método para crear el frame botones, en él se anidarán los
    botones que ofrecen los resultados que puede pedirle el usuario
    a la aplicación.
    """
    def crear_frame_botones(self):
        frame_botones = tk.Frame(self.frame_principal, height = 465, width=175, relief = "raised", bd=2)
        frame_botones.place(x=0,y=0)
        boton_mayor_gasto = tk.Button(frame_botones, text = "Mayor Gasto", width = 14, heigh = 1, command=self.mayor_gasto)
        boton_mayor_gasto.place(x=25,y=20)
        boton_mayor_ahorro = tk.Button(frame_botones, text = "Mayor Ahorro", width = 14, heigh = 1, command=self.mayor_ahorro)
        boton_mayor_ahorro.place(x=25,y=60)
        boton_media_gasto = tk.Button(frame_botones, text = "Media de Gasto", width = 14, heigh = 1, command=self.media_gasto)
        boton_media_gasto.place(x=25,y=100)
        boton_gasto_total = tk.Button(frame_botones, text = "Gasto Total", width = 14, heigh = 1, command=self.gasto_total)
        boton_gasto_total.place(x=25,y=140)
        boton_ingresos_totales = tk.Button(frame_botones, text = "Ingresos Totales", width = 14, heigh = 1, command=self.ingresos_totales)
        boton_ingresos_totales.place(x=25,y=180)
        boton_grafico_ahorros = tk.Button(frame_botones, text = "Gráfico Ahorros", width = 14, heigh = 1, command=self.grafico_ahorros)
        boton_grafico_ahorros.place(x=25,y=300)
        boton_grafico_ingresos = tk.Button(frame_botones, text = "Gráfico Ingresos", width = 14, heigh = 1, command=self.grafico_ingresos)
        boton_grafico_ingresos.place(x=25,y=350)
        boton_grafico_gastos = tk.Button(frame_botones, text = "Gráfico Gastos", width = 14, heigh = 1, command=self.grafico_gastos)
        boton_grafico_gastos.place(x=25,y=400)
        return frame_botones


    """
    Método para crear el cuadro de resultados, es una simple entrada de
    texto donde el usuario verá el resultado de lo que le pide a la aplicación.
    """
    def crear_muestra(self):
        muestra = tk.Entry(self.frame_botones, width = 14, bd=2, state='readonly')
        muestra.place(x=33,y=240)
        return muestra


    """
    Método para crear el frame de gráficos, en él se imprimirán los distintos
    gráficos que pueda solicitar el usuario a la aplicación.
    """
    def crear_frame_grafico(self):
        frame_grafico = tk.Frame(self.frame_principal, height = 465, width=1025, relief = "sunken", bd=2, bg="white")
        frame_grafico.place(x=175,y=0)
        return frame_grafico


    """
    Método para expresar el mes en el que se ha hecho el mayor gasto.
    Recurre al método mayor definido en back.
    Utiliza la lista de resultados cargada en el constructor.
    Dará el resultado en la muestra.
    Asociado al boton_mayor_gasto
    """
    def mayor_gasto(self):
        gastos=self.resultados[2]
        mayor_gasto=back.mayor(gastos)
        back.cambiar_texto(self.muestra, mayor_gasto)


    """
    Método para expresar el mes en el que se ha hecho el mayor ahorro.
    Recurre al método mayor definido en back.
    Utiliza la lista de resultados cargada en el constructor.
    Dará el resultado en la muestra.
    Asociado al boton_mayor_ahorro.
    """
    def mayor_ahorro(self):
        ahorro=self.resultados[0]
        mayor_ahorro=back.mayor(ahorro)
        back.cambiar_texto(self.muestra, mayor_ahorro)


    """
    Método para expresar la media de gastos durante el año.
    Recurre al método media definido en back.
    Utiliza la lista de resultados cargada en el constructor.
    Dará el resultado en la muestra.
    Asociado al boton_media_gasto.
    """
    def media_gasto(self):
        gastos=self.resultados[2]
        media_gastos=back.media(gastos)
        back.cambiar_texto(self.muestra, round(media_gastos,2))


    """
    Método para expresar el gasto total durante el año.
    Recurre al método toal definido en back.
    Utiliza la lista de resultados cargada en el constructor.
    Dará el resultado en la muestra.
    Asociado al boton_gasto_total.
    """
    def gasto_total(self):
        gastos=self.resultados[2]
        gasto_total=back.total(gastos)
        back.cambiar_texto(self.muestra, gasto_total)


    """
    Método para expresar los ingresos totales durante el año.
    Recurre al método toal definido en back.
    Utiliza la lista de resultados cargada en el constructor.
    Dará el resultado en la muestra.
    Asociado al boton_ingresos_totales.
    """
    def ingresos_totales(self):
        ingresos=self.resultados[1]
        ingresos_totales=back.total(ingresos)
        back.cambiar_texto(self.muestra, ingresos_totales)

    """
    Método para generar los gráficos en el frame_grafico.
    Destruye y vuelve a construir el frame, para eliminar la imagen,
    de esta manera no se quedarán cargadas en memoria todas las que se vayan solicitando.
    Es un método genérico, se usará en otros métodos dándole como parámetros
    el gráfico que debe expresar y el texto que debe poner en el eje y
    """
    def grafico(self,resultado, eje_y):
        self.frame_grafico.destroy()
        self.frame_grafico = self.crear_frame_grafico()
        valores = resultado.values()
        meses = resultado.keys()
        fig = Figure(figsize=(10.5, 4.6), dpi=100)
        ax0 = fig.add_axes( (0.1, .15, .87, .8),frameon=False)
        ax0.set_xlabel( 'Meses' )
        ax0.set_ylabel( str(eje_y) )
        ax0.plot(meses,valores,marker="o")
        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()



    def grafico_ahorros(self):
        """
        Método para generar el gráfico de los ahorros.
        Utiliza el método gráfico definido anteriormente.
        Utiliza la lista de resultados cargada en el constructor.
        Asociado al boton_grafico_ahorros.
        """
        self.grafico(self.resultados[0], "Ahorros")


    
    ##Método para generar el gráfico de los ingresos.
    #Utiliza el método gráfico definido anteriormente.
    #Utiliza la lista de resultados cargada en el constructor.
    #Asociado al boton_grafico_ingresos.
    def grafico_ingresos(self):
        self.grafico(self.resultados[1],"Ingresos")


    """
    Método para generar el gráfico de los gastos.
    Utiliza el método gráfico definido anteriormente.
    Utiliza la lista de resultados cargada en el constructor.
    Asociado al boton_grafico_gastos.
    """
    def grafico_gastos(self):
        self.grafico(self.resultados[2],"Gastos")
