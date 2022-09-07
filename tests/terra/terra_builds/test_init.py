"""
This file tests get functions for the supported builds and models.
"""
from unittest import main, TestCase

from camel.terra.terra_builds import get_all_builds, get_all_models


class TerraBuildsTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_all_builds(self):
        outcome = get_all_builds()
        self.assertEqual(["eu_west_1", "oasis_platform"], outcome)

    def test_get_all_models(self):
        outcome = get_all_models()
        self.assertEqual(["BGEQ", "pariswindstorm", "Impactforecasting_euws"], outcome)


if __name__ == "__main__":
    main()
