def es_palindromo(cadena):
    cadena_limpia = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    return "Si" if cadena_limpia == cadena_limpia[::-1] else "No"  # Comparar con su reverso

# Entrada del usuario con mensaje
texto = input("Escribe una cadena de texto: ")

# Salida formateada
print(es_palindromo(texto))
