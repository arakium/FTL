# Create a class called: 
# ClimateStation 
# The class must contain the following attributes: 
# • city 
# • temperature 
# • humidity 
# • rainfall 
# Create the following methods: 
# • display_summary() 
# • calculate_risk() 
# • update_temperature(new_temperature) 
# Create at least 5 ClimateStation objects, place them inside a list and use a loop to display 
# their information. 
# Then create a child class: 
# SmartClimateStation 
# It must inherit from ClimateStation and include: 
# • Additional attribute: sensor_status 
# 2 
# • Method: check_sensor() 
# The child class should continue to use the methods inherited from the parent class. 
# Bonus 
# Create an additional method: recommendation() 
# that returns an action depending on the climate risk, for example: 
# • LOW → Normal monitoring 
# • MODERATE → Continue monitoring 
# • HIGH → Increased monitoring recommended 
# • EXTREME → Immediate attention required

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
