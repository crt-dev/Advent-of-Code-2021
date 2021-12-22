from collections import Counter, defaultdict
from pprint import pprint

winning_score = 1000
dice = [n for n in range(1, 100 + 1)]
d = 0
roll_count = 0

def roll_dice():
    global d
    global roll_count
    if d == 100:
        d = 0
    value = dice[d]
    d += 1
    roll_count += 1
    return value

class Player:
    def __init__(self, starting_pos):
        self.pos = starting_pos
        self.score = 0

    def move(self):
        dice_roll = [roll_dice() for _ in range(3)]
        move = sum(dice_roll)
        while self.pos + move > 10:
            move -= 10
        self.pos += move # new_pos
        self.score += self.pos
        self.test[self.pos] += 1

    def __repr__(self):
        return "position: {} total score: {}".format(self.pos, self.score)

def solution_p1():
    global d
    global dice
    global roll_count

    p1 = Player(7) #
    p2 = Player(8)
    # p1 = Player(4) #
    # p2 = Player(8)

    while p2.score < winning_score:
        p1.move()
        if p1.score >= winning_score:
            break
        p2.move()

    print("player1: ", p1)
    print("player2: ", p2)
    print("dice rolls = ", roll_count)
    print("ans = ", p2.score * roll_count)

solution_p1()