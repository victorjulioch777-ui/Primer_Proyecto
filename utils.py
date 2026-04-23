import time
import re

def escribir_lento(texto, delay=0.03):
    """Muestra un texto en consola carácter por carácter.
    
    Recorre cada letra de la cadena proporcionada e imprime su contenido
    de forma progresiva.

    Args:
        texto (_type_): El texto que mostrata en consola
        delay (float, optional): Tiempo de espera entra cada carácter.Defaults to 0.03.
        
    Returns:
        None
    """
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()  # salto de línea al final

# colores.py

# RESET
RESET = "\033[0m"

# TEXTO
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# FONDOS
FONDO_ROJO = "\033[41m"
FONDO_VERDE = "\033[42m"
FONDO_AMARILLO = "\033[43m"
FONDO_AZUL = "\033[44m"
FONDO_MAGENTA = "\033[45m"
FONDO_CYAN = "\033[46m"
FONDO_BLANCO = "\033[47m"

# ESTILOS
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"

# BRILLANTES
ROJO_BRIGHT = "\033[91m"
VERDE_BRIGHT = "\033[92m"
AMARILLO_BRIGHT = "\033[93m"
AZUL_BRIGHT = "\033[94m"
MAGENTA_BRIGHT = "\033[95m"
CYAN_BRIGHT = "\033[96m"
BLANCO_BRIGHT = "\033[97m"

def pintar(texto, color="", fondo="", estilo=""):
    """Devuelve un texto formateado con códigos ANSI para color, fondo y estilo.

    Args:
        texto (_type_): Texto que se desea formatear
        color (str, optional): Código ANSI para el color del texto. Defaults to "".
        fondo (str, optional): Código ANSI para el color de fondo. Defaults to "".
        estilo (str, optional): Código ANSI para aplicar el estilo al texto. Defaults to "".

    Returns:
        _type_: Texto formateado
    """
    return f"{estilo}{color}{fondo}{texto}{RESET}" 

        
keywords = [
    "is", "in", "not", "and", "or",
    "del", "yield",
    "with", "as",
    "match", "case",
    "finally",
    "except",
    "raise",
    "assert",
    "lambda",
    "global",
    "nonlocal",
    "pass",
    "break",
    "continue",
    "print", "input", "len", "range",
    "int", "float", "str", "bool",
    "list", "tuple", "set", "dict",
    "open", "read", "write",
    "append", "remove", "pop",
    "sort", "reverse",
    "format", "split", "join",
    "True", "False", "None",         "def", "for", "if", "while", "import",
    "=", ":", "elif", "else", "break", "continue", "pass",
    "return", "lambda",
    "True", "False", "None",
    "and", "or", "not", "in", "is",
    "try", "except", "finally", "raise", "assert",
    "class", "self", "super",
    "from", "as",
    "async", "await", "with",
    "global", "nonlocal", "if", "elif", "else", "for", "while", "break", "continue", "pass",
    "def","return","lambda",
    "True","False","None",
    "and","or","not","in","is",
    "try","except","finally","raise","assert",
    "class","self","super",
    "import","from","as",
    "async","await","with",
    "global","nonlocal"
]

def es_codigo(texto):
    pistas = [
        "def", "for", "if", "while", "import",
        "=", ":", "elif", "else", "break", "continue", "pass",
        "return", "lambda",
        "True", "False", "None",
        "and", "or", "not", "in", "is",
        "try", "except", "finally", "raise", "assert",
        "class", "self", "super",
        "from", "as",
        "async", "await", "with",
        "global", "nonlocal"
    ]

    contador = 0  # <-- esto te faltaba

    texto = texto.split() 

    for palabra in texto:
        limpia = palabra.strip("():,.;\"'\n\t")

        if limpia in pistas:
            contador += 1

        if contador >= 2:
            return True

    return False


def colorear_codigo(texto:list):
    """Resalta palabras reservadas dentro de un texto que contiene código.

    Args:
        texto (_type_): Texto o fragmento de código a procesar.

    Returns:
        _type_: Texto resaltado a color.
    """

    """for i, palabra in enumerate(palabras):
        limpia = palabra.strip("():,")
        if limpia in keywords:
            palabras[i] = pintar(MAGENTA_BRIGHT) + palabra

    return " ".join(palabras)"""

    tokens = re.split(r'(\W+)', texto)

    for i, palabra in enumerate(tokens):
        if palabra in keywords:
            tokens[i] = pintar(palabra, MAGENTA_BRIGHT, "")

    return "".join(tokens)
