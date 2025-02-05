def contar_palabras(cadena):
    palabras = cadena.split()  # Divide la cadena en palabras eliminando espacios extras
    return len(palabras)

# Entrada del usuario con mensaje
texto = input("Escribe una cadena de texto: ")

# Salida 
print(f"Número de palabras en la cadena: {contar_palabras(texto)}")
