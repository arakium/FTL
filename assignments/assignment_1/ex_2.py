# Create the following function: 
# calculate_risk(temperature, rainfall) 
# The function must return: 
# 1 
# • EXTREME – temperature ≥ 40°C 
# • HIGH – temperature ≥ 35°C or rainfall < 5 mm 
# • MODERATE – temperature ≥ 30°C or rainfall < 15 mm 
# • LOW – otherwise 
# Then: 
# 1. Call the function for every valid city. 
# 2. Display the city, temperature and calculated risk. 
# 3. Create another function that returns a tuple containing: (average, minimum, maximum) 
# 4. Display only cities classified as HIGH or EXTREME. 
# 5. Sort the cities from the highest to the lowest temperature using sorted() and, where 
# appropriate, lambda. 

climate_data = [
    {
        "City": "New York",
        "Temperature": 22,   # °C
        "Humidity": 65,      # %
        "Rainfall": 120      # mm/month
    },
    {
        "City": "Tokyo",
        "Temperature": 27,
        "Humidity": 70,
        "Rainfall": 150
    },
    {
        "City": "Cairo",
        # Missing temperature value
        "Humidity": 30,
        "Rainfall": 5
    },
    {
        "City": "London",
        "Temperature": 18,
        "Humidity": 75,
        "Rainfall": 80
    },
    {
        "City": "Sydney",
        "Temperature": 25,
        "Humidity": 60,
        "Rainfall": 100
    },
    {
        "City": "Dubai",
        "Temperature": 41,
        "Humidity": 20,
        "Rainfall": 2
    },
    {
        "City": "Rio de Janeiro",
        "Temperature": 33,
        "Humidity": 85,
        "Rainfall": 200
    }
]
expected_data = ["City", "Temperature", "Humidity", "Rainfall"]


def calculate_risk(temperature: int, rainfall: int) -> str:
    if temperature >= 40:
        return "EXTREME"
    elif temperature >= 35 or rainfall < 5:
        return "HIGH"
    elif temperature >= 30 or rainfall < 15:
        return "MODERATE"
    else:
        return "LOW"


def get_valid_cities(climate_data: list[dict]) -> list[dict]:
    valid = []
    for city in climate_data:
        if not all(key in city for key in expected_data):
            continue
        if not isinstance(city["Temperature"], (int, float)) or not isinstance(city["Rainfall"], (int, float)):
            continue
        valid.append(city)
    return valid


def display(climate_data: list[dict]) -> None:
    for city in climate_data:
        risk = calculate_risk(city["Temperature"], city["Rainfall"])
        print("#" * 10)
        print(f"City: {city['City']}\nTemperature: {city['Temperature']}\nRisk: {risk}")


def temperature_stats(climate_data: list[dict]) -> tuple[float, float, float]:
    temperatures = [city["Temperature"] for city in climate_data]
    average = sum(temperatures) / len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    return average, minimum, maximum


def display_high_risk(climate_data: list[dict]) -> None:
    for city in climate_data:
        risk = calculate_risk(city["Temperature"], city["Rainfall"])
        if risk in ("HIGH", "EXTREME"):
            print(f"City: {city['City']} | Temperature: {city['Temperature']} | Risk: {risk}")


valid_cities = get_valid_cities(climate_data)

display(valid_cities)

avg_temp, min_temp, max_temp = temperature_stats(valid_cities)
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Minimum Temperature: {min_temp}°C")
print(f"Maximum Temperature: {max_temp}°C")

display_high_risk(valid_cities)

sorted_cities = sorted(valid_cities, key=lambda city: city["Temperature"], reverse=True)
for city in sorted_cities:
    print(f"{city['City']}: {city['Temperature']}°C")