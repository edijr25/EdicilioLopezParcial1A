## Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y 
##devuelva el valor del producto con un aumento del 5%.
##realizar la llamada desde el main.

##def aplicarAumento(precio:float): -> float
##La funcion AplicarAumento recibe como parametro el precio de un producto y realiza un aumento del 5%
##retornando un valor tipo float
def aplicarAumento(precio):
    aumento = precio * 0.05
    precioConAumento = precio + aumento
    return precioConAumento


precioProducto = float(input("Ingrese el precio del producto: "))
precioConAumento = aplicarAumento(precioProducto)
print("El precio con aumento es:", precioConAumento)
