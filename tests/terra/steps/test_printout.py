"""
This file tests the step that printouts a statement.
"""
from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.printout import PrintoutStep


class PrintoutStepTest(TestCase):

    def setUp(self) -> None:
        self.string = "test string"
        self.test = PrintoutStep(string=self.string)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.string, self.test.string)

    @patch("camel.terra.steps.printout.print")
    def test_run(self, mock_print):
        self.test.run()
        mock_print.assert_called_once_with(self.string)


if __name__ == "__main__":
    main()
