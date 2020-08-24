import unittest
from game import SnakesLadders


class TestingClass(unittest.TestCase):


    def test_a_dice_response_type(self):
        self.addTypeEqualityFunc(int,SnakesLadders(dice_type="C").roll_dice())

    def test_b_even_dice_response(self):
        self.assertEqual(SnakesLadders(dice_type="C").roll_dice() % 2, 0)

    def test_c_check_dice_step(self):
        self.assertEqual(SnakesLadders(dice_type="N").calculate_board_steps(dice_value=11,board_step=90)[0],90)

    def test_d_check_dice_step(self):
        self.assertEqual(SnakesLadders(dice_type="N").calculate_board_steps(dice_value=11,board_step=80)[0],91)

    def test_e_check_snakes_step(self):
        self.assertEqual(SnakesLadders(dice_type="N").calculate_board_steps(dice_value=11,board_step=43)[0],25)

    def test_g_check_ladders_step(self):
        self.assertEqual(SnakesLadders(dice_type="N").calculate_board_steps(dice_value=2, board_step=11)[0], 98)

if __name__ == '__main__':
    unittest.main()
