import itertools
from collections import Counter, defaultdict
from pprint import pprint
from itertools import permutations

winning_score = 21
dice = [n for n in range(1, 100 + 1)]
d = 0
roll_count = 0

die_values = [1, 2, 3]
permutations = [p for p in itertools.product(die_values, repeat=6)]

def roll_dice():
    global d
    global roll_count
    if d == 100:
        d = 0
    value = dice[d]
    d += 1
    roll_count += 1
    return value

def roll_dice_n(n):
    return [roll_dice() for _ in range(n)]


class Player:
    def __init__(self, starting_pos, score=None):
        self.pos = starting_pos
        if score is None:
            self.score = 0
        else:
            self.score = score

    def move(self, move_value):
        while self.pos + move_value > 10:
            move_value -= 10
        self.pos += move_value # new_pos
        self.score += self.pos

    def has_won(self):
        return self.score >= winning_score

    def __repr__(self):
        return "position: {} total score: {}".format(self.pos, self.score)

class Game:
    def __init__(self, p1_pos, p1_score, p2_pos, p2_score):
        self.p1 = Player(p1_pos, p1_score)
        self.p2 = Player(p2_pos, p2_score)
        self.winner = None

    def execute_turn(self, p1_move_value, p2_move_value):
        self.p1.move(p1_move_value)
        if self.p1.has_won():
            self.winner = "p1"
            return
        self.p2.move(p2_move_value)
        if self.p2.has_won():
            self.winner = "p2"

    def __repr__(self):
        # p1 = "{} score = {}".format("winner" if self.winner == "p1" else "loser", self.score)
        # p2 = "{} score = {}".format("winner" if self.winner == "p2" else "loser", self.score)
        return "[p1={} p2={}]".format(self.p1.score, self.p2.score)

    def get_loser(self):
        return self.p2 if self.winner == "p1" else self.p1

class GameManager:
    def __init__(self, game):
        self.p1_wins = 0
        self.p2_wins = 0
        self.games = [game]
        self.finished_games = []
        self.games2 = defaultdict(int)

    def __repr__(self):
        return "[ongoing: {} p1 wins: {} p2 wins: {}]".format(len(self.games2), self.p1_wins, self.p2_wins)
        #return "[ongoing: {} p1 wins: {} p2 wins: {}]".format(len(self.games), self.p1_wins, self.p2_wins)

    def move(self, p1_move_value, p2_move_value):
        if len(self.games) == 0:
            return False
        for game in self.games:
            game.execute_turn(p1_move_value, p2_move_value)
            if game.winner == "p1":
                self.p1_wins += 1
            elif game.winner == "p2":
                self.p2_wins += 1
            if game.winner is not None:
                self.finished_games.append(game)
                self.games.remove(game)
                return False
        return True

    def run_games(self):
        if len(self.games) == 0:
            return False
        new_games = []
        for game in self.games:
            for p in permutations:
                new_game = Game(game.p1.pos, game.p1.score, game.p2.pos, game.p2.score)
                p1_throw = sum([p[0], p[1], p[2]])
                p2_throw = sum([p[3], p[4], p[5]])
                new_game.execute_turn(p1_throw, p2_throw)
                if new_game.winner is not None:
                    if new_game.winner == "p1":
                        self.p1_wins += 1
                    else:
                        self.p2_wins += 1
                else:
                    new_games.append(new_game)
        self.games = new_games
        return True

    def run_games2(self):
        for key, values in self.games2.items():
            p1pos, p1score, p2pos, p2score = key
            if p1score >= 21:
                self.p1_wins += self.games2[key]
                break
            if p2score >= 21:
                self.p1_wins += self.games2[key]

        if len(self.games2) == 0:
            return False
        new_games = defaultdict(int)
        for key, values in self.games2.items():
            p1pos, p1score, p2pos, p2score = key
            for p in permutations:
                p1_throw = sum([p[0], p[1], p[2]])
                p2_throw = sum([p[3], p[4], p[5]])

                while p1pos + p1_throw > 10:
                    p1_throw -= 10
                p1pos += p1_throw
                p1score += p1pos

                while p2pos + p2_throw > 10:
                    p2_throw -= 10
                p2pos += p2_throw
                p2score += p2pos

                num = self.games2[key]
                new_games[(p1pos, p1score, p2pos, p2score)] += num

        self.games2 = new_games
        return True








def solution_p1(p1_start, p2_start):
    global roll_count
    p1 = Player(p1_start)
    p2 = Player(p2_start)
    game = Game(p1, p2)
    gm = GameManager(game)

    in_progress = True
    while in_progress:
        p1_move_value = sum(roll_dice_n(3))
        p2_move_value = sum(roll_dice_n(3))
        in_progress = gm.move(p1_move_value, p2_move_value)
    loser = gm.finished_games[0].get_loser()
    return (roll_count - 3) * loser.score #subtract 3 because we're rolling after p1 has already won

def solution_p2(p1_start, p2_start):
    game = Game(p1_start, 0, p2_start, 0) #initial seeding game
    gm = GameManager(game)
    gm.games2[(p1_start, 0, p2_start, 0)] = 1

    while gm.run_games2():
        print(gm)

    print("all games complete")


#print(solution_p1(4, 8))  #739785
#print(solution_p1(7, 8))  #556206
solution_p2(4,8)