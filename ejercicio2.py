def contar_vocales(cadena):
    vocales = "aeiou"
    return sum(1 for letra in cadena.lower() if letra in vocales)

# Entrada del usuario
texto = input("Escriba una cadena de texto: ")

# Cálculo y salida
print(f"Número de vocales en la cadena: {contar_vocales(texto)}")
