from contadorPalabras.util.util import contar_palabras


def programa_contador_palabras():
    texto: str = input("Ingrese una frase: ")
    cantidad: int = contar_palabras(texto)
    print(f"La frase {texto} tiene {cantidad} palabras")