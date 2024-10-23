import unittest
from alert_manager import check_alert_conditions

class TestAlertManager(unittest.TestCase):

    @staticmethod
    def capture_alert_output(alert_func, data):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        alert_func(data)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_no_alert_below_threshold(self):
        mock_data = {"city": "Delhi", "temperature": 30}
        output = self.capture_alert_output(lambda data: check_alert_conditions(data, threshold=35), mock_data)
        self.assertEqual(output, "")

    def test_alert_above_threshold(self):
        mock_data = {"city": "Delhi", "temperature": 37}
        output = self.capture_alert_output(lambda data: check_alert_conditions(data, threshold=35), mock_data)
        self.assertIn("ALERT", output)
        self.assertIn("Delhi", output)

    def test_consecutive_alerts(self):
        # Simulate two consecutive breaches
        mock_data_1 = {"city": "Delhi", "temperature": 36}
        mock_data_2 = {"city": "Delhi", "temperature": 37}

        # Check the first data (no alert yet)
        output_1 = self.capture_alert_output(lambda data: check_alert_conditions(data, threshold=35, consecutive_alerts=2), mock_data_1)
        self.assertEqual(output_1, "")

        # Now check the second data (should trigger alert)
        output_2 = self.capture_alert_output(lambda data: check_alert_conditions(data, threshold=35, consecutive_alerts=2), mock_data_2)
        self.assertIn("ALERT", output_2)

if __name__ == '__main__':
    unittest.main()
