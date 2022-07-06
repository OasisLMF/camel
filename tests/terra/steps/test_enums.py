from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.enums import StepNameEnum

class TestEnums(TestCase):

    def test___init__(self):
        test = StepNameEnum("run_script")

        self.assertEqual(StepNameEnum.RUN_SCRIPT, test)
        self.assertEqual("run_script", test.value)
        self.assertEqual("RUN_SCRIPT", test.name)

    def test_throw_error(self):
        with self.assertRaises(ValueError) as error:
            StepNameEnum("test")
        self.assertEqual("'test' is not a valid StepNameEnum", str(error.exception))


if __name__ == "__main__":
    main()
