import random

# Comentario: Este programa implementa un juego de adivinar la palabra donde el usuario intenta adivinar una palabra secreta. Se proporcionan pistas sobre las letras y sus posiciones.

# Lista de palabras secretas
palabras_secretas = ['mosiah', 'temple', 'moroni', 'helaman', 'nephi']
# Selecciona una palabra secreta al azar
palabra_secreta = random.choice(palabras_secretas)
intentos = 0

# Genera la pista inicial con guiones bajos
pista = '_ ' * len(palabra_secreta)
print("Welcome to the word guessing game!")
print(f"Your hint is: {pista.strip()}")

while True:
    intento = input("What is your guess? ").lower()
    intentos += 1

    # Verifica si la longitud de la suposición es correcta
    if len(intento) != len(palabra_secreta):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    # Verifica si la suposición es correcta
    if intento == palabra_secreta:
        print(f"Congratulations! You guessed it!")
        print(f"It took you {intentos} guesses.")
        break

    # Genera la pista
    nueva_pista = []
    for i in range(len(palabra_secreta)):
        if intento[i] == palabra_secreta[i]:
            nueva_pista.append(intento[i].upper())  # Letra correcta en la posición correcta
        elif intento[i] in palabra_secreta:
            nueva_pista.append(intento[i])  # Letra correcta pero en la posición incorrecta
        else:
            nueva_pista.append('_')  # Letra incorrecta

    # Muestra la nueva pista
    print("Your hint is:", ' '.join(nueva_pista))
