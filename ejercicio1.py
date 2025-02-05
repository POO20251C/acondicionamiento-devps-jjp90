def suma_digitos(n):
    return sum(int(d) for d in str(abs(n)))

# Entrada, numero
numero = int(input("Escribe el número: "))

# Salida, suma de los digitos
print(f"Suma de sus dígitos: {suma_digitos(numero)}")