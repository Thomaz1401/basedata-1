
def generar_historia():
    adjetivo1 = input("Introduce un adjetivo: ")
    animal = input("Introduce un animal: ")
    verbo1 = input("Introduce un verbo: ")
    adjetivo2 = input("Introduce otro adjetivo: ")
    exclamacion = input("Introduce una exclamación: ").capitalize()  
    verbo2 = input("Introduce otro verbo: ")
    verbo3 = input("Introduce un último verbo: ")

 
    historia = (
        f"El otro día, me metí en serios problemas. Todo empezó cuando vi un "
        f"{adjetivo1} {animal} {verbo1} muy {adjetivo2} al final del pasillo. "
        f"\"{exclamacion}!\", grité. Pero lo único que se me ocurrió hacer fue "
        f"{verbo2} una y otra vez. Milagrosamente, eso hizo que se detuviera, "
        f"pero no antes de que intentara {verbo3} justo delante de mi familia."
    )

    print("\nAquí está tu historia personalizada:\n")
    print(historia)

generar_historia()
