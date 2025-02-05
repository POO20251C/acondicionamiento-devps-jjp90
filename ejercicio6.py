def encontrar_max_min(numeros):
    elementos = numeros.split()
    
    # Verificar que todos los elementos sean números enteros (incluyendo negativos)
    if not all(elem.lstrip('-').isdigit() for elem in elementos):
        return "Error: Ingresa solo números enteros separados por espacios."

    numeros_int = list(map(int, elementos))  # Convertir a enteros
    return f"{max(numeros_int)} {min(numeros_int)}"

# Entrada del usuario con mensaje
entrada = input("Escribe una lista de números separados por espacios: ")

# Salida
print(encontrar_max_min(entrada))
