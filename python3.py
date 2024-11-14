def aventura():
    print("¡Bienvenido a la Mazmorra Misteriosa!")
    print("Te despiertas en una oscura mazmorra, con solo una antorcha para iluminar el camino.")
    print("Hay tres caminos delante de ti.")
    
    # Primer nivel de decisiones
    decision1 = input("¿Cuál eliges? IZQUIERDA, DERECHA o FRENTE: ").strip().lower()
    
    if decision1 == "izquierda":
        print("\nTe diriges a la izquierda y escuchas el sonido del agua corriendo.")
        print("Llegas a un río subterráneo. Hay un bote viejo flotando cerca de la orilla.")
        
        # Segundo nivel de decisiones para "izquierda"
        decision2 = input("¿Te SUBES al bote o decides CRUZAR el río nadando?: ").strip().lower()
        
        if decision2 == "subes":
            print("\nTe subes al bote y comienzas a remar. El bote se mueve lentamente por el río.")
            print("De repente, ves una criatura gigante acercándose.")
            
            # Tercer nivel de decisiones para "subes"
            decision3 = input("¿Le LANZAS algo para distraerla o SALTAS al agua?: ").strip().lower()
            
            if decision3 == "lanzas":
                print("\nLe lanzas tu mochila y la criatura se distrae. Aprovechas el momento para escapar.")
                print("¡Has sobrevivido al peligro y encuentras la salida de la mazmorra!")
            elif decision3 == "saltas":
                print("\nSaltas al agua y tratas de nadar, pero la corriente te arrastra.")
                print("Te pierdes en la oscuridad del río. ¡Game Over!")
            else:
                print("\nOpción no válida. La criatura te atrapa. ¡Game Over!")
        
        elif decision2 == "cruzar":
            print("\nIntentas cruzar el río nadando, pero la corriente es demasiado fuerte.")
            print("Te lleva lejos de la orilla y no puedes regresar. ¡Game Over!")
        else:
            print("\nOpción no válida. Te quedas paralizado por la indecisión y el tiempo se agota. ¡Game Over!")
    
    elif decision1 == "derecha":
        print("\nTe diriges hacia la derecha y te encuentras con una puerta cerrada.")
        print("Junto a la puerta, ves una caja con tres llaves de diferentes colores.")
        
        # Segundo nivel de decisiones para "derecha"
        decision2 = input("¿Cuál llave eliges? ROJA, AZUL o VERDE: ").strip().lower()
        
        if decision2 == "roja":
            print("\nLa llave roja encaja perfectamente en la cerradura. La puerta se abre lentamente.")
            print("Al otro lado hay una habitación llena de tesoros.")
            
            # Tercer nivel de decisiones para "roja"
            decision3 = input("¿Tomas el TESORO o SIGUES adelante?: ").strip().lower()
            
            if decision3 == "tesoro":
                print("\nDecides tomar el tesoro, pero al hacerlo, una trampa se activa y la habitación se llena de gas venenoso.")
                print("¡Has caído en una trampa! ¡Game Over!")
            elif decision3 == "sigues":
                print("\nDecides dejar el tesoro y seguir adelante. Encuentras una escalera que te lleva a la libertad.")
                print("¡Has escapado de la mazmorra con vida!")
            else:
                print("\nOpción no válida. Mientras dudas, la puerta se cierra y quedas atrapado. ¡Game Over!")
        
        elif decision2 == "azul":
            print("\nLa llave azul no encaja. De repente, el suelo comienza a moverse bajo tus pies.")
            print("Caes en una trampa y te quedas atrapado. ¡Game Over!")
        
        elif decision2 == "verde":
            print("\nLa llave verde encaja, pero al abrir la puerta, una avalancha de rocas cae sobre ti.")
            print("No logras escapar. ¡Game Over!")
        
        else:
            print("\nOpción no válida. Mientras dudas, una trampa se activa y caes en un pozo. ¡Game Over!")
    
    elif decision1 == "frente":
        print("\nCaminas hacia adelante y te encuentras en una gran sala con un dragón durmiendo en el centro.")
        print("Tienes dos opciones: intentar pasarlo sigilosamente o enfrentarlo.")
        
        # Segundo nivel de decisiones para "frente"
        decision2 = input("¿Qué haces? SIGILOSAMENTE o ENFRENTAR: ").strip().lower()
        
        if decision2 == "sigilosamente":
            print("\nTratas de pasar sigilosamente junto al dragón, pero accidentalmente pateas una piedra.")
            print("El dragón se despierta y te mira directamente.")
            
            # Tercer nivel de decisiones para "sigilosamente"
            decision3 = input("¿CORRES o te OCULTAS detrás de una columna?: ").strip().lower()
            
            if decision3 == "corres":
                print("\nCorres lo más rápido que puedes, pero el dragón lanza una llamarada y te quema. ¡Game Over!")
            elif decision3 == "ocultas":
                print("\nTe escondes detrás de una columna y el dragón no te ve. Cuando vuelve a dormir, aprovechas para escapar.")
                print("¡Lograste salir de la mazmorra sin ser visto!")
            else:
                print("\nOpción no válida. El dragón te encuentra y te quema. ¡Game Over!")
        
        elif decision2 == "enfrentar":
            print("\nDecides enfrentarte al dragón. Sin embargo, no tienes ninguna arma y el dragón es demasiado poderoso.")
            print("Te lanza una llamarada y te derrota. ¡Game Over!")
        else:
            print("\nOpción no válida. El dragón te ve y te ataca. ¡Game Over!")
    
    else:
        print("\nOpción no válida. Mientras dudas, algo te ataca desde las sombras. ¡Game Over!")

aventura()
