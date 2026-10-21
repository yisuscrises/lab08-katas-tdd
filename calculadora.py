def sumar(cadena: str) -> int:
    if not cadena:
        return 0
    numeros = cadena.split(",")
    return sum(int(n) for n in numeros)