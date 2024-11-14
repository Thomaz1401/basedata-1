file_name = "life_expectancy_data.csv"

def load_data(file_name):
    data = []
    with open(file_name, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            country = parts[0]
            year = int(parts[1])
            life_expectancy = float(parts[2])
            data.append((country, year, life_expectancy))
    return data

def calculate_min_max(data):
    min_life_exp = min(data, key=lambda x: x[2])
    max_life_exp = max(data, key=lambda x: x[2])
    return min_life_exp, max_life_exp

def analyze_year(data, year):
    year_data = [x for x in data if x[1] == year]
    if not year_data:
        print(f"No hay datos para el año {year}.")
        return
    
    avg_life_exp = sum(x[2] for x in year_data) / len(year_data)
    min_country = min(year_data, key=lambda x: x[2])
    max_country = max(year_data, key=lambda x: x[2])
    
    print(f"\nPara el año {year}:")
    print(f"La esperanza de vida promedio en todos los países fue de {avg_life_exp:.2f}")
    print(f"La esperanza de vida máxima fue en {max_country[0]} con {max_country[2]}")
    print(f"La esperanza de vida mínima fue en {min_country[0]} con {min_country[2]}")

def analyze_country(data, country):
    country_data = [x for x in data if x[0].lower() == country.lower()]
    if not country_data:
        print(f"No se encontraron datos para el país '{country}'.")
        return
    
    avg_life_exp = sum(x[2] for x in country_data) / len(country_data)
    min_year = min(country_data, key=lambda x: x[2])
    max_year = max(country_data, key=lambda x: x[2])
    
    print(f"\nPara el país {country.capitalize()}:")
    print(f"La esperanza de vida promedio fue de {avg_life_exp:.2f}")
    print(f"La esperanza de vida máxima fue en el año {max_year[1]} con {max_year[2]}")
    print(f"La esperanza de vida mínima fue en el año {min_year[1]} con {min_year[2]}")

def calculate_largest_drop(data):
    largest_drop = None
    for country in set(x[0] for x in data):
        country_data = sorted([x for x in data if x[0] == country], key=lambda x: x[1])
        for i in range(1, len(country_data)):
            drop = country_data[i-1][2] - country_data[i][2]
            if largest_drop is None or drop > largest_drop[2]:
                largest_drop = (country, country_data[i-1][1], country_data[i][1], drop)
    
    print("\nMayor caída en la esperanza de vida de un año a otro:")
    print(f"El país con la mayor caída fue {largest_drop[0]}, desde {largest_drop[1]} hasta {largest_drop[2]}, con una disminución de {largest_drop[3]:.2f}")

def main():
    data = load_data(file_name)
    
    min_life_exp, max_life_exp = calculate_min_max(data)
    print(f"La esperanza de vida máxima general es: {max_life_exp[2]} en {max_life_exp[0]} en el año {max_life_exp[1]}")
    print(f"La esperanza de vida mínima general es: {min_life_exp[2]} en {min_life_exp[0]} en el año {min_life_exp[1]}")
    
    year = int(input("\nIngrese el año de interés: "))
    analyze_year(data, year)
    
    country = input("\nIngrese el nombre de un país para obtener estadísticas (o deje en blanco para omitir): ").strip()
    if country:
        analyze_country(data, country)
    
    calculate_largest_drop(data)

if __name__ == "__main__":
    main()
