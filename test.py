import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict_endpoint(self):
        input_data = {
            'total_acidity': 7.8,
            'sugar_content': 0.88,
            'mineral_content': 0.96,
            'acidity_of_base': 0.02,
            'element_X': 1.8,
            'phenol_compound': 86.0,
            'compound_Y': 3.45,
            'phenolic_derivative': 1.25,
            'color_agent': 0.5,
            'intensity_modifier': 5.5,
            'hue_value': 1.1,
            'dilution_ratio': 3.0,
            'protein_level': 1050.0
        }

        response = self.client.post('/predict', json=input_data)
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/predict', json=input_data)
        data = response.get_json()

        print("Response status code:", response.status_code)
        print("Response data:", data)

        self.assertIn('prediction', data)
        self.assertTrue(data['prediction'] in [
                        'Class 0', 'Class 1', 'Class 2'])


if __name__ == '__main__':
    unittest.main()