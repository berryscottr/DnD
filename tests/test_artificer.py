import unittest
from DnD.src.roll import roll

valid_rolls = [
    "1",
    "2",
    "1d20",
    "2d20",
    "1d20m2",
    "2d20m2",
    "1d20m2a",
    "2d20m2a",
    "1d20m-1",
    "2d20m-1",
    "1d20m-1d",
    "2d20m-1d",
]


class TestCases(unittest.TestCase):
    def test_valid_roll(self):
        for valid_roll in valid_rolls:
            for _ in range(0, 1000):
                self.assertTrue(type(roll.roll(valid_roll)[0]) == int, True)
                self.assertTrue(type(roll.roll(valid_roll)[1]) == bool, True)


if __name__ == '__main__':
    unittest.main()
