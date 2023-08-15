import random as rand

seguir = True
while seguir:
    opcion = int(input("Bienvenido al programa, escoja un juego:\n 1. Adivina el número\n 2. Piedra, papel o tijeras\n 3. Ahorcado\n 4. Salir del programa \n Elección: "))
    
    if opcion == 1:
        numero = rand.randint(1, 40)
        intentos = 0
        while True:
            numAd = int(input("Ingresa el número a adivinar: "))
            intentos += 1
            if numAd == numero:
                print(f"Adivinaste el número en {intentos} intentos.")
                break
            elif numAd < numero:
                print("Intenta con un número más alto")
            else:
                print("Intenta con un número más bajo")
                
    elif opcion == 2:
        print("Bienvenido al juego de piedra, papel o tijera a continuación: ")
        elecciones = ["piedra", "papel", "tijera"]
        seguirJugando = True
        while seguirJugando:
            jugadorEleccion = input("Elige piedra, papel o tijera: ").lower()
            ptEleccion = rand.choice(elecciones)
            print("Tu adversario eligió", ptEleccion)
            if jugadorEleccion == ptEleccion:
                print("Empate")
                seguirJ = input("Empataron, quieres intentar nuevamente (Si / No): ")
                if seguirJ == "No":
                    seguirJugando = False
            elif (jugadorEleccion == "piedra" and ptEleccion == "tijera") or (jugadorEleccion == "papel" and ptEleccion == "piedra") or (jugadorEleccion == "tijera" and ptEleccion == "papel"):
                print("Felicidades, ganaste")
                seguirJugando = False
            else:
                print("Inténtalo otra vez, perdiste")
                seguirJugando = False
                
    elif opcion == 3:
        print("Bienvenido al juego de ahorcado")
        palabras = ["raton", "pato", "perro"]
        palabraEscogida = rand.choice(palabras)
        vidasUsuario = 5
        esp = ["_"] * len(palabraEscogida)
        seguirJu = False
        while not seguirJu and vidasUsuario > 0:
            letraE = input("Escoge una letra: ").lower()
            encontrada = False
            for pos in range(len(palabraEscogida)):
                letraA = palabraEscogida[pos]
                if letraA == letraE:
                    esp[pos] = letraA
                    encontrada = True
            if not encontrada:
                vidasUsuario -= 1
                print("Te quedan", vidasUsuario, "vidas")
                if vidasUsuario == 0:
                    seguirJu = True
                    print("Perdiste")
            print(esp)
            if "_" not in esp:
                seguirJu = True
                print("Ganaste")
                
    elif opcion == 4:
        seguir = False
    else:
        print("Por favor elige una opción válida (1-4).")
