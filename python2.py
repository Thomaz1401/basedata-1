
def calcular_total_comida():
   
    precio_nino = float(input("Introduce el precio de la comida para niños: "))
    precio_adulto = float(input("Introduce el precio de la comida para adultos: "))
    cantidad_ninos = int(input("Introduce el número de niños: "))
    cantidad_adultos = int(input("Introduce el número de adultos: "))
    
   
    subtotal = (precio_nino * cantidad_ninos) + (precio_adulto * cantidad_adultos)
    print(f"\nSubtotal: ${subtotal:.2f}")
    
   
    tasa_impuesto = float(input("Introduce la tasa de impuesto sobre las ventas (en porcentaje, por ejemplo 6.5): "))
    
  
    impuesto = subtotal * (tasa_impuesto / 100)
    print(f"Impuesto sobre las ventas: ${impuesto:.2f}")
    
 
    total = subtotal + impuesto
    print(f"Total a pagar: ${total:.2f}")
    
 
    pago = float(input("\nIntroduce el monto del pago: "))
    

    cambio = pago - total
    if cambio >= 0:
        print(f"El cambio a devolver es: ${cambio:.2f}")
    else:
        print(f"Falta por pagar: ${abs(cambio):.2f}")

calcular_total_comida()
