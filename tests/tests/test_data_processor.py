import unittest
from data_processor import kelvin_to_celsius, kelvin_to_fahrenheit, process_weather_data

class TestDataProcessor(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85, places=2)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(kelvin_to_fahrenheit(300), 80.33, places=2)

    def test_process_weather_data(self):
        mock_data = {
            "name": "Delhi",
            "main": {"temp": 300, "feels_like": 298},
            "weather": [{"main": "Clear"}],
            "dt": 1609459200
        }

        processed_data = process_weather_data(mock_data, unit="Celsius")
        self.assertEqual(processed_data["city"], "Delhi")
        self.assertEqual(processed_data["temperature"], 26.85)
        self.assertEqual(processed_data["feels_like"], 24.85)
        self.assertEqual(processed_data["main_condition"], "Clear")
        self.assertEqual(processed_data["timestamp"], 1609459200)

if __name__ == '__main__':
    unittest.main()
