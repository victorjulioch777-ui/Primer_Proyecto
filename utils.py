import time

def escribir_lento(texto, delay=0.03):
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
    return f"{estilo}{color}{fondo}{texto}{RESET}" 

        
keywords = [
    "if","elif","else","for","while","break","continue","pass",
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
    pistas = ["def", "for", "if", "while", "import", "print", "=", ":"]
    return any(p in texto for p in pistas)

def colorear_codigo(texto):
    palabras = texto.split()

    for i, palabra in enumerate(palabras):
        limpia = palabra.strip("():,")
        if limpia in keywords:
            palabras[i] = pintar(MAGENTA_BRIGHT) + palabra

    return " ".join(palabras)

