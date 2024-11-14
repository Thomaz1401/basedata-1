def calcular_sensacion_termica(temperatura, velocidad):
    """Calcula la sensación térmica (wind chill) en Fahrenheit."""
    return 35.74 + (0.6215 * temperatura) - (35.75 * (velocidad ** 0.16)) + (0.4275 * temperatura * (velocidad ** 0.16))

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * (9/5)) + 32


temperatura = float(input("What is the temperature? "))
unidad = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

if unidad == 'C':
    temperatura = celsius_a_fahrenheit(temperatura)

for velocidad in range(5, 65, 5):
    sensacion_termica = calcular_sensacion_termica(temperatura, velocidad)
    print(f"At temperature {temperatura:.1f}F, and wind speed {velocidad} mph, the windchill is: {sensacion_termica:.2f}F")