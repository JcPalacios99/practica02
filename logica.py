# logica.py
def mostrar_estado(palabra, letras_adivinadas):
    estado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    return estado

def jugar_ahorcado(palabra):
    print("=== JUEGO DEL AHORCADO ===")
    print("Tienes 6 intentos para adivinar la palabra.")
    print("¡Buena suerte!\n")

    letras_adivinadas = set()
    intentos_restantes = 6
    letras_usadas = set()

    while intentos_restantes > 0:
        print("\n" + mostrar_estado(palabra, letras_adivinadas))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Letras correctas: {len(letras_adivinadas)}")

        letra = input("Ingresa una letra: ").upper()
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, ingresa una sola letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue

        letras_usadas.add(letra)

        if letra in palabra:
            letras_adivinadas.add(letra)
            if all(letra in letras_adivinadas for letra in palabra):
                print(f"\n¡Ganaste! La palabra era: {palabra}")
                return True
        else:
            intentos_restantes -= 1
            print("Letra incorrecta.")

        if intentos_restantes == 0:
            print(f"\nPerdiste. La palabra era: {palabra}")
            return False