# palabras.py
palabras = ["python", "programacion", "computadora", "algoritmo", "tecnologia"]
indice_actual = 0  # Variable para rastrear qué palabra toca usar

def obtener_palabra():
    global indice_actual
    palabra = palabras[indice_actual]  # Selecciona la palabra actual
    indice_actual = (indice_actual + 1) % len(palabras)  # Avanza al siguiente índice, reinicia si llega al final
    return palabra.upper()