# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres
# como primer parámetro, un carácter como segundo y otro carácter  como tercero,  
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero 
# y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

##def reemplazarCaracteres(cadena, caracter_original, caracter_reemplazo): la funcion recibe 3 parametros tipo string
## el primero es una cadena de caracteres, el segundo un caracter y el tercero un caracter y la misma 
## retorna 2 valores con la nueva cadena y la cantidad de veces que se reemplazó ese caracter 

def reemplazarCaracteres(cadena, caracter_original, caracter_reemplazo):
    cantidad_reemplazos = 0
    nueva_cadena = ""
    for caracter in cadena:
        if caracter == caracter_original:
            nueva_cadena += caracter_reemplazo
            cantidad_reemplazos += 1
        else:
            nueva_cadena += caracter
    return nueva_cadena, cantidad_reemplazos


cadena = input("Ingrese una cadena de caracteres: ")
caracter_original = input("Ingrese el carácter a reemplazar: ")
caracter_reemplazo = input("Ingrese el carácter de reemplazo: ")

nueva_cadena, cantidad_reemplazos = reemplazarCaracteres(cadena, caracter_original, caracter_reemplazo)
print("Nueva cadena:", nueva_cadena)
print("Cantidad de reemplazos realizados:", cantidad_reemplazos)
