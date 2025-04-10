# main.py
from palabras import obtener_palabra
from logica import jugar_ahorcado

def main():
    print("¡Bienvenido al juego del ahorcado!")
    palabra = obtener_palabra()
    jugar_ahorcado(palabra)

if __name__ == "__main__":
    main()