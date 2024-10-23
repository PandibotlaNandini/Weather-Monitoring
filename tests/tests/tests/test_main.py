import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):

    @patch('main.get_weather_data')
    @patch('main.check_alert_conditions')
    @patch('time.sleep', return_value=None)  # Skip time.sleep for faster tests
    def test_main_loop(self, mock_sleep, mock_check_alert_conditions, mock_get_weather_data):
        mock_get_weather_data.return_value = {
            "name": "Delhi",
            "main": {"temp": 300, "feels_like": 298},
            "weather": [{"main": "Clear"}],
            "dt": 1609459200
        }

        # Run one iteration of the main loop
        with patch('builtins.input', side_effect=['exit']):  # Simulate exit input to break loop
            main()

        # Ensure weather data was retrieved and processed for each city
        self.assertTrue(mock_get_weather_data.called)
        self.assertTrue(mock_check_alert_conditions.called)

if __name__ == '__main__':
    unittest.main()
