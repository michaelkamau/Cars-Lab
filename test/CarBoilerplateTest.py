import unittest
from cars.car import Car

class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = Car('Honda')
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        honda = Car('Honda')
        self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        gm = Car()
        self.assertEqual('General', gm.name,
                         msg='The car should be called `General` if no name was passed as an argument')


if __name__ == '__main__':
    unittest.main()