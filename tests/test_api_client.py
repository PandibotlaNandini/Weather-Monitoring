import unittest
from unittest.mock import patch
from api_client import get_weather_data

class TestApiClient(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_get_weather_data_success(self, mock_get):
        mock_response = {
            "name": "Delhi",
            "main": {"temp": 300, "feels_like": 298},
            "weather": [{"main": "Clear"}],
            "dt": 1609459200
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        data = get_weather_data("Delhi")
        self.assertIsNotNone(data)
        self.assertEqual(data["name"], "Delhi")
        self.assertEqual(data["main"]["temp"], 300)

    @patch('api_client.requests.get')
    def test_get_weather_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        data = get_weather_data("InvalidCity")
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
