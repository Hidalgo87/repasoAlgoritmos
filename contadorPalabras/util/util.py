def contar_palabras(frase: str) -> int:
    """Cuenta palabras"""
    palabras: list[str] = frase.split(" ")
    return len(palabras)
