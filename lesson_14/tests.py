from unittest import TestCase, main
from tsk_city_weather import city_data


class TestWeather(TestCase):
    def test_city(self):
        self.assertTrue('UA' in city_data())  # Input all UA city


if __name__ == '__main__':
    main()
