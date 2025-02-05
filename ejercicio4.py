def invertir_lista(numeros):
    return " ".join(numeros.split()[::-1])  # Divide, invierte y une la lista

# Entrada del usuario con mensaje
entrada = input("Escribe una lista de números separados por espacios: ")

# Salida formateada
print(f"Lista invertida: {invertir_lista(entrada)}")
