import pandas as pd
import re
"""
En este módulo se definen todos los métodos y clases necesarios
para la manipulación de los datos de la aplicación, su fin es generar
los resultados que le pasamos a la GUI.
"""


"""
Definimos un tipo de error que nos puede dar al generar un archivo
"""
class DemasiadasColumnas(Exception):
    pass


"""
Definimos un tipo de error que nos puede dar al generar un archivo
"""
class InsuficientesColumnas(Exception):
    pass


"""
Método para comprobar que el archivo que tomamos es álido, en cuanto
al número de columnas que posee. Tienen que ser necesariamente 12,
coincidiendo con los meses del año. En él se usas los dos tipos de
error definidos.
"""
def archivo_valido(dataframe):
    bool = True
    try:
        total_cols=len(dataframe.axes[1])
        if (total_cols>12):
            raise DemasiadasColumnas
        elif (total_cols<12):
            raise InsuficientesColumnas
    except DemasiadasColumnas:
        print("El número de coumnas es mayor que 12, no se corresponde con los meses del año")
        bool = False
    except InsuficientesColumnas:
        print("El número de coumnas es menor que 12, no se corresponde con los meses del año")
        bool = False
    return bool


"""
Método que nos devuelve la ruta en la que está el archivo
que vamos a manejar
"""
def cargar_archivo():
    MEDIA = "C:/Users/prior/Desktop/Máster/Buenas prácticas/finanzas2020[1].csv"
    return MEDIA


"""
Método que nos devuelve un data frame generado a partir de una
ruta dada
"""
def generar_dataframe(ruta):
    df = pd.DataFrame()
    try:
        df =pd.read_csv(ruta,sep='\t')
    except:
        print("No se encuentra el archivo en la ruta especificada, pruebe a cambiar la ruta o incluir el archivo en ella")
    return df


"""
Método que sirve para hacer cambios en las entradas de texto.
Tranforma su estado a normal, borra lo que hay en su interior,
incorpora el nuevo texto (parámetro de la función), y vuelve a
dejar el estado en "read only"
"""
def cambiar_texto(cuadro, texto):
    cuadro.config(state='normal')
    cuadro.delete(0,15)
    cuadro.insert(0,texto)
    cuadro.config(state='readonly')


"""
Método que nos devuelve la clave que lleva asociado el
mayor valor de un diccionario. Se asume que la aplicación
solo usa este método con diccionarios:
clave = String; valor = int
"""
def mayor(diccionario):
    valor = 0
    mayor = ""
    for i in diccionario.keys():
        if diccionario[i] > valor:
            valor = diccionario[i]
            mayor = i
    return mayor


"""
Método que nos devuelve el total de la suma de los valores
de un diccionario. Se asume que la aplicación
solo usa este método con diccionarios:
clave = String; valor = int
"""
def total(diccionario):
    total = 0
    for i in diccionario.keys():
        total = total + diccionario[i]
    return total


"""
Método que nos devuelve la media de los valores
de un diccionario. Para ello utiliza el método
total definido anteriormente. Se asume que la aplicación
solo usa este método con diccionarios:
clave = String; valor = int
"""
def media(diccionario):
    suma = total(diccionario)
    numero = len(diccionario.keys())
    return suma/numero


"""
Método que nos devuelve una lista de los valores correspondientes
a la suma aritmética, a la suma de los positivos y a la suma de valores
negativos. En él se hace la limpieza de datos, omitiendo los valores erróneos
y limpiando los mal introducidos para transformarlos en variables numéricas.
"""
def sumar_columna(dataframe,columna):
    df2 = dataframe[columna]
    ahorro = 0
    ingresos = 0
    gastos = 0
    errores = []
    e = 0
    for i in range(0,len(dataframe[columna])):
        try:
            entero = int(df2[i])
            ahorro = ahorro+entero
            if entero > 0:
                ingresos = ingresos+entero
            else:
                gastos = gastos-entero
        except:
            e = e+1
            errores.append(df2[i])
            print("Existen ",e," datos mal introducidos en el mes de",columna)
            print(errores)
    e = 0
    total = len(errores)
    for i in range(0, total):
        error = errores[i]
        try:
            error = int(re.sub("[^0-9,-]", "",error))
            ahorro = ahorro+error
            if error > 0:
                ingresos = ingresos+error
            else:
                gastos = gastos-error
        except:
            e = e+1
            print("Existen ",e," datos que no contienen información de relevancia numérica en el mes de",columna)
    return [ahorro,ingresos,gastos]


"""
Método que nos devuelve una lista de diccionarios,
cada uno de ellos corresponde a los ahorros, ingresos y
gastos respectivamente. Utiliza el método sumar_columna definido
anteriormente. La lista que devuelve será la que use la GUI para
generar los resultados y cargarlos en memoria. Al ejecutar este método,
comprueba que el archivo introducido es válido según los parámetros definidos
en el método archivo_valido.
"""
def resultados(dataframe):
    ahorro_total = {}
    ingresos_total = {}
    gastos_total = {}
    if archivo_valido(dataframe):
        try:
            ahorro_total = {"Enero":sumar_columna(dataframe,"Enero")[0],
                            "Febrero":sumar_columna(dataframe,"Febrero")[0],
                            "Marzo":sumar_columna(dataframe,"Marzo")[0],
                            "Abril":sumar_columna(dataframe,"Abril")[0],
                            "Mayo":sumar_columna(dataframe,"Mayo")[0],
                            "Junio":sumar_columna(dataframe,"Junio")[0],
                            "Julio":sumar_columna(dataframe,"Julio")[0],
                            "Agosto":sumar_columna(dataframe,"Agosto")[0],
                            "Septiembre":sumar_columna(dataframe,"Septiembre")[0],
                            "Octubre":sumar_columna(dataframe,"Octubre")[0],
                            "Noviembre":sumar_columna(dataframe,"Noviembre")[0],
                            "Diciembre":sumar_columna(dataframe,"Diciembre")[0],}
        except:
            print("No se ha podido generar el ahorro total, revise los datos")
        try:
            ingresos_total = { "Enero":sumar_columna(dataframe,"Enero")[1],
                                "Febrero":sumar_columna(dataframe,"Febrero")[1],
                                "Marzo":sumar_columna(dataframe,"Marzo")[1],
                                "Abril":sumar_columna(dataframe,"Abril")[1],
                                "Mayo":sumar_columna(dataframe,"Mayo")[1],
                                "Junio":sumar_columna(dataframe,"Junio")[1],
                                "Julio":sumar_columna(dataframe,"Julio")[1],
                                "Agosto":sumar_columna(dataframe,"Agosto")[1],
                                "Septiembre":sumar_columna(dataframe,"Septiembre")[1],
                                "Octubre":sumar_columna(dataframe,"Octubre")[1],
                                "Noviembre":sumar_columna(dataframe,"Noviembre")[1],
                                "Diciembre":sumar_columna(dataframe,"Diciembre")[1],}
        except:
            print("No se ha podido generar los ingresos totales, revise los datos")
        try:
            gastos_total = { "Enero":sumar_columna(dataframe,"Enero")[2],
                             "Febrero":sumar_columna(dataframe,"Febrero")[2],
                             "Marzo":sumar_columna(dataframe,"Marzo")[2],
                             "Abril":sumar_columna(dataframe,"Abril")[2],
                             "Mayo":sumar_columna(dataframe,"Mayo")[2],
                             "Junio":sumar_columna(dataframe,"Junio")[2],
                             "Julio":sumar_columna(dataframe,"Julio")[2],
                             "Agosto":sumar_columna(dataframe,"Agosto")[2],
                             "Septiembre":sumar_columna(dataframe,"Septiembre")[2],
                             "Octubre":sumar_columna(dataframe,"Octubre")[2],
                             "Noviembre":sumar_columna(dataframe,"Noviembre")[2],
                             "Diciembre":sumar_columna(dataframe,"Diciembre")[2],}
        except:
            print("No se ha podido generar los gastos totales, revise los datos")
    else:
        pass
    return [ahorro_total,ingresos_total,gastos_total]
