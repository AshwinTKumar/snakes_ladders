import unittest
from game import roll_dice


class TestingClass(unittest.TestCase):

    def test_a_dice_response_type(self):
        self.addTypeEqualityFunc(int,roll_dice(dice_type="C"))


if __name__ == '__main__':
    unittest.main()
