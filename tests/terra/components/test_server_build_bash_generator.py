from unittest import main, TestCase

from camel.terra.components.server_build_bash_generator import ServerBuildBashGenerator


class TestServerBuildBashGenerator(TestCase):

    def setUp(self) -> None:
        self.test = ServerBuildBashGenerator()

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual([], self.test)

    def test_write_line(self):
        self.test.write_line(line="this is the first line")
        self.test.write_line(line="this is the second line")

        expected_outcome = ['this is the first line\n', 'this is the second line\n']
        self.assertEqual(expected_outcome, self.test)

    def test_generate_script(self):
        self.test.generate_script()
        self.assertEqual("".join(self.test), str(self.test))


if __name__ == "__main__":
    main()
