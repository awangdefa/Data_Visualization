from random import randint


class Die():
    """表示一个骰子的类"""

    def __init__(self, numb_sides=6):
        """骰子默认为6面"""
        self.num_sides = numb_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
