class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
tem1 = TemperatureConverter()
print(tem1.celsius_to_fahrenheit(25)) # 77.0