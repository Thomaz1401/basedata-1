filename = "life-expectancy.csv"

min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_country = ""
max_country = ""
min_year = 0
max_year = 0


life_expectancy_by_year = {}

with open(filename, 'r') as file:
    header = file.readline() 
    for line in file:
        parts = line.strip().split(',')
        country = parts[0]
        year = int(parts[1])
        life_expectancy = float(parts[2])
        
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = country
            min_year = year
        
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = country
            max_year = year

        if year not in life_expectancy_by_year:
            life_expectancy_by_year[year] = []
        life_expectancy_by_year[year].append(life_expectancy)

print(f"The overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_year}")

year_of_interest = int(input("Enter the year of interest: "))

if year_of_interest in life_expectancy_by_year:
    average_life_expectancy = sum(life_expectancy_by_year[year_of_interest]) / len(life_expectancy_by_year[year_of_interest])
    max_life_expectancy_year = max(life_expectancy_by_year[year_of_interest])
    min_life_expectancy_year = min(life_expectancy_by_year[year_of_interest])

    max_country_year = [country for country, year, life in zip(countries, years, life_expectancy) if life == max_life_expectancy_year and year == year_of_interest][0]
    min_country_year = [country for country, year, life in zip(countries, years, life_expectancy) if life == min_life_expectancy_year and year == year_of_interest][0]

    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_country_year} with {max_life_expectancy_year:.2f}")
    print(f"The min life expectancy was in {min_country_year} with {min_life_expectancy_year:.3f}")
else:
    print(f"No data available for the year {year_of_interest}.")
