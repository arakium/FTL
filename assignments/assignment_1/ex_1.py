# Create climate information for at least 5 cities using a list of dictionaries. 
# Each city should contain: 
# • City name 
# • Temperature 
# • Humidity 
# • Rainfall 
# Your programme must: 
# 1. Loop through all cities and display their information. 
# 2. Include one city with a missing temperature value. 
# 3. Use continue to skip the city with missing temperature data. 
# 4. Classify temperatures as: 
# o Extreme Heat: ≥ 40°C 
# o High Heat: ≥ 35°C 
# o Moderate Heat: ≥ 30°C 
# o Normal: < 30°C 
# 5. Calculate: 
# o Number of valid observations 
# o Average temperature 
# o Highest temperature 
# o Lowest temperature 
# 6. Store the final classification results in a dictionary. 
# You may use built-in functions such as: len() • sum() • min() • max() • round() 

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


def classify_temperature(temperature: int) -> str:
    if temperature >= 40:
        return "Extreme Heat"
    elif temperature >= 35:
        return "High Heat"
    elif temperature >= 30:
        return "Moderate Heat"
    else:
        return "Normal" 

expected_data = ["City", "Temperature", "Humidity", "Rainfall"]

def calculate_data(climate_data: list[dict]) -> dict:
    classification = {
    "valid_observations": 0,
    "average_temperature": None,
    "highest_temperature": None,
    "lowest_temperature": None
    }

    temperatures_sum = 0

    for city in climate_data:

        if not all(key in city for key in expected_data):
            continue

        temp = city["Temperature"]

        if not isinstance(temp, (int, float)):
            continue

        if classification["highest_temperature"] is None or temp > classification["highest_temperature"]:
            classification["highest_temperature"] = temp

        if classification["lowest_temperature"] is None or temp < classification["lowest_temperature"]:
            classification["lowest_temperature"] = temp

        classification["valid_observations"] += 1
        temperatures_sum += temp


    classification["average_temperature"] = round(temperatures_sum / classification["valid_observations"], 2)

    return classification

def display(climate_data: list[dict]) -> None:
    final_results = calculate_data(climate_data)
    for city in climate_data:
        if not all(key in city for key in expected_data):
            continue
        print("#"*5)
        for key, value in city.items():
            print(f"{key}: {value}{'°C' if key == 'Temperature' else ''}")
            if key == "Temperature":
                classification = classify_temperature(value)
        print(f"Classification: {classification}")
        
    print("#" * 10)
    print(f"final results dictionary:\n{final_results}")

if __name__ == "__main__":
    display(climate_data)