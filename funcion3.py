# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena 
# de caracteres como parámetro  y su responsabilidad es ordenar los caracteres de
#  manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

##def ordenarCaracteres(cadena): es una funcion que recibe una cadena tipo string y se encarga
## de organizar de manera ascendente la cadena y retorna la cadena organizada de manera ascendente

def ordenarCaracteres(cadena):
    caracteres = list(cadena)
    longitud = len(caracteres)
    for i in range(longitud - 1):
        for j in range(longitud - i - 1):
            if caracteres[j] > caracteres[j + 1]:
                caracteres[j], caracteres[j + 1] = caracteres[j + 1], caracteres[j]
    nueva_cadena = ''.join(caracteres)
    return nueva_cadena


cadena = input("Ingrese una cadena de caracteres: ")
cadena_ordenada = ordenarCaracteres(cadena)
print("Cadena ordenada:", cadena_ordenada)
