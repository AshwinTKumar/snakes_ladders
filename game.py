import random


class SnakesLadders:

    def __init__(self,dice_type):
        self.dice_type = dice_type
        self.snakes_ladders = {4: {"step": 28, "type": "ladder"}, 13: {"step": 98,"type": "ladder"},
                               23: {"step": 3, "type": "snake"}, 17: {"step": 7, "type": "snake"},
                                10: {"step": 4, "type": "snake"}, 54: {"step": 25, "type": "snake"}}

    def roll_dice(self):
        if self.dice_type == "C":
            return random.randrange(2, 13, 2)
        else:
            return random.randint(1, 6)

    def calculate_board_steps(self, dice_value, board_step):
        new_step = board_step + dice_value
        modified_step = self.snakes_ladders.get(new_step,None)
        if modified_step:
            step_message = "You got a %s at %s, You are now at %s" % (modified_step["type"],new_step,modified_step["step"])
            return modified_step["step"], step_message
        if new_step < 100:
            step_message = "You are now at %s" % new_step
            return new_step, step_message
        elif new_step == 100:
            print("Congrats you have won the game !!")
            exit()
        elif new_step > 100:
            required_steps = 100-board_step
            return board_step, "You cannot move ahead. You need exact %s on dice to win the game" % required_steps

    def play(self, board_step):
        dice_value = self.roll_dice()
        print("Your dice value is : %s" % dice_value)
        return self.calculate_board_steps(dice_value=dice_value, board_step=board_step)


if __name__ == "__main__":
    turn = 0
    allowed_turns = 10
    board_step = 0
    input = raw_input("Let's play Snakes and Ladders !!")
    print("You have %s turns" % allowed_turns)
    print("You have two dice options")
    print("Normal Dice: 1,2,3,4,5,6 dice values")
    print("Crooked Dice: 2,4,6,8,10,12 dice values")
    dice_type = raw_input("Select dice type: N for normal or C for crooked:")
    if dice_type != 'N' and dice_type != 'C':
        print("Invalid Dice Type entered")
    else:
        while turn < allowed_turns:
            input = raw_input("Throw the dice by pressing enter:")
            turn += 1
            board_step, message = SnakesLadders(dice_type).play(board_step=board_step)
            print(message)