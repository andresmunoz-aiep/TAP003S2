def sumar(val1, decada):
    result = val1 + decada
    return result


# Variable / Constante
decada = int(10)

# Entrada

val1 = int(input("Ingrese su edad: "))

# Proceso
resultado = sumar(val1, decada)

# Salida
print("Usted tendrá", resultado, "años en una década más")
