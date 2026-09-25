climate_data_1 = [
    {"City": "New York", "Temperature": 22, "Humidity": 65, "Rainfall": 120},
    {"City": "Tokyo", "Temperature": 27, "Humidity": 70, "Rainfall": 150},
    {"City": "Cairo", "Humidity": 30, "Rainfall": 5},
    {"City": "London", "Temperature": 18, "Humidity": 75, "Rainfall": 80},
    {"City": "Sydney", "Temperature": 25, "Humidity": 60, "Rainfall": 100},
    {"City": "Dubai", "Temperature": 41, "Humidity": 20, "Rainfall": 2},
    {"City": "Rio de Janeiro", "Temperature": 33, "Humidity": 85, "Rainfall": 200}
]

expected_data_1 = ["City", "Temperature", "Humidity", "Rainfall"]


def classify_temperature_1(temperature: int) -> str:
    if temperature >= 40:
        return "Extreme Heat"
    elif 35 <= temperature < 40:
        return "High Heat"
    elif 30 <= temperature < 35:
        return "Moderate Heat"
    else:
        return "Normal"


def calculate_data_1(data: list[dict]) -> dict:
    classification = {
        "valid_observations": 0,
        "average_temperature": None,
        "highest_temperature": None,
        "lowest_temperature": None
    }

    temperatures_sum = 0

    for city in data:
        if not all(key in city for key in expected_data_1):
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


def display_1(data: list[dict]) -> None:
    final_results = calculate_data_1(data)
    for city in data:
        if not all(key in city for key in expected_data_1):
            continue
        print("#" * 5)
        for key, value in city.items():
            print(f"{key}: {value}{'°C' if key == 'Temperature' else ''}")
            if key == "Temperature":
                classification = classify_temperature_1(value)
        print(f"Classification: {classification}")

    print("#" * 10)
    print(f"final results dictionary:\n{final_results}")


def run_exercise_1() -> None:
    display_1(climate_data_1)


climate_data_2 = [
    {"City": "New York", "Temperature": 22, "Humidity": 65, "Rainfall": 120},
    {"City": "Tokyo", "Temperature": 27, "Humidity": 70, "Rainfall": 150},
    {"City": "Cairo", "Humidity": 30, "Rainfall": 5},
    {"City": "London", "Temperature": 18, "Humidity": 75, "Rainfall": 80},
    {"City": "Sydney", "Temperature": 25, "Humidity": 60, "Rainfall": 100},
    {"City": "Dubai", "Temperature": 41, "Humidity": 20, "Rainfall": 2},
    {"City": "Rio de Janeiro", "Temperature": 33, "Humidity": 85, "Rainfall": 200}
]

expected_data_2 = ["City", "Temperature", "Humidity", "Rainfall"]


def calculate_risk_2(temperature: int, rainfall: int) -> str:
    if temperature >= 40:
        return "EXTREME"
    elif temperature >= 35 or rainfall < 5:
        return "HIGH"
    elif temperature >= 30 or rainfall < 15:
        return "MODERATE"
    else:
        return "LOW"


def get_valid_cities_2(data: list[dict]) -> list[dict]:
    valid = []
    for city in data:
        if not all(key in city for key in expected_data_2):
            continue
        if not isinstance(city["Temperature"], (int, float)) or not isinstance(city["Rainfall"], (int, float)):
            continue
        valid.append(city)
    return valid


def display_2(data: list[dict]) -> None:
    for city in data:
        risk = calculate_risk_2(city["Temperature"], city["Rainfall"])
        print("#" * 10)
        print(f"City: {city['City']}\nTemperature: {city['Temperature']}\nRisk: {risk}")


def temperature_stats_2(data: list[dict]) -> tuple[float, float, float]:
    temperatures = [city["Temperature"] for city in data]
    average = sum(temperatures) / len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    return average, minimum, maximum


def display_high_risk_2(data: list[dict]) -> None:
    for city in data:
        risk = calculate_risk_2(city["Temperature"], city["Rainfall"])
        if risk in ("HIGH", "EXTREME"):
            print(f"City: {city['City']} | Temperature: {city['Temperature']} | Risk: {risk}")


def run_exercise_2() -> None:
    valid_cities = get_valid_cities_2(climate_data_2)

    display_2(valid_cities)

    avg_temp, min_temp, max_temp = temperature_stats_2(valid_cities)
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Minimum Temperature: {min_temp}°C")
    print(f"Maximum Temperature: {max_temp}°C")

    display_high_risk_2(valid_cities)

    sorted_cities = sorted(valid_cities, key=lambda city: city["Temperature"], reverse=True)
    for city in sorted_cities:
        print(f"{city['City']}: {city['Temperature']}°C")


class ClimateStation:
    def __init__(self, city: str, temperature: float, humidity: float, rainfall: float):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall = rainfall

    def display_summary(self) -> None:
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Humidity: {self.humidity}%")
        print(f"Rainfall: {self.rainfall}mm")

    def calculate_risk(self) -> str:
        if self.temperature >= 40:
            return "EXTREME"
        elif self.temperature >= 35 or self.rainfall < 5:
            return "HIGH"
        elif self.temperature >= 30 or self.rainfall < 15:
            return "MODERATE"
        else:
            return "LOW"

    def update_temperature(self, new_temperature: float) -> None:
        self.temperature = new_temperature

    def recommendation(self) -> str:
        risk = self.calculate_risk()
        if risk == "LOW":
            return "Normal monitoring"
        elif risk == "MODERATE":
            return "Continue monitoring"
        elif risk == "HIGH":
            return "Increased monitoring recommended"
        else:
            return "Immediate attention required"


class SmartClimateStation(ClimateStation):
    def __init__(self, city: str, temperature: float, humidity: float, rainfall: float, sensor_status: str):
        super().__init__(city, temperature, humidity, rainfall)
        self.sensor_status = sensor_status

    def check_sensor(self) -> str:
        return self.sensor_status


def run_exercise_3() -> None:
    stations = [
        ClimateStation("New York", 22, 65, 120),
        ClimateStation("Tokyo", 27, 70, 150),
        ClimateStation("London", 18, 75, 80),
        ClimateStation("Sydney", 25, 60, 100),
        ClimateStation("Dubai", 41, 20, 2),
        SmartClimateStation("Rio de Janeiro", 33, 85, 200, "Active")
    ]

    for station in stations:
        station.display_summary()
        print(f"Risk: {station.calculate_risk()}")
        print(f"Recommendation: {station.recommendation()}")
        if isinstance(station, SmartClimateStation):
            print(f"Sensor Status: {station.check_sensor()}")
        print("#" * 10)


if __name__ == "__main__":
    print("=" * 30, "EXERCISE 1", "=" * 30)
    run_exercise_1()

    print("\n" + "=" * 30, "EXERCISE 2", "=" * 30)
    run_exercise_2()

    print("\n" + "=" * 30, "EXERCISE 3", "=" * 30)
    run_exercise_3()