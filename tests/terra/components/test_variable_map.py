from unittest import main, TestCase

from camel.terra.components.variable_map import VariableMap, Singleton


class Test(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        test = VariableMap()

        self.assertEqual({}, test)
        self.assertEqual(None, test.ip_address)

        another_test = VariableMap()
        self.assertEqual(id(another_test), id(test))

    def test_load_data(self):
        test = VariableMap()

        data = {
            "one": 1,
            "two": 2,
            "three": 3
        }

        test.load_data(mapped_variables=data, ip_address="1234")

        self.assertEqual(data, test)
        self.assertEqual("1234", test.ip_address)


if __name__ == "__main__":
    main()
