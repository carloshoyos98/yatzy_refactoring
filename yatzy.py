class Yatzy:

    @staticmethod
    def chance(*dice):

        sum_dice = 0
        for die in dice:
            sum_dice += die
        return sum_dice

    @staticmethod
    def yatzy(*dice):
        for die in dice:
            if dice.count(die) == len(dice):
                return 50
            else:
                return 0

    @staticmethod
    def sum_of_ones(*dice):
        total_of_ones = 0
        for die in dice:
            if die == 1:
                total_of_ones += 1
            else:
                continue
        return total_of_ones

    @staticmethod
    def sum_of_twos(*dice):
        sum_twos = 0
        for die in dice:
            if die == 2:
                sum_twos += 2
            else:
                continue
        return sum_twos

    @staticmethod
    def sum_of_threes(*dice):
        sum_threes = 0
        for die in dice:
            if die == 3:
                sum_threes += 3
            else:
                continue
        return sum_threes

    @staticmethod
    def sum_of_fours(*dice):
        sum_fours = 0
        for die in dice:
            if die == 4:
                sum_fours += 4
            else:
                continue
        return sum_fours

    @staticmethod
    def sum_of_fives(*dice):
        sum_fives = 0
        for die in dice:
            if die == 5:
                sum_fives += 5
            else:
                continue
        return sum_fives

    @staticmethod
    def sum_of_sixes(*dice):
        sum_sixes = 0
        for die in dice:
            if die == 6:
                sum_sixes += 6
            else:
                continue
        return sum_sixes

    @staticmethod
    def one_pair(*dice):
        score = 0
        number = 6
        while number >= 1:
            if dice.count(number) >= 2:
                score += 2 * number
                break
            number -= 1
        return score

    @staticmethod
    def two_pairs(*dice):
        score = 0
        pairs = 0
        number = 6
        while number >= 1:
            if dice.count(number) >= 2:
                pairs += 1
                score += 2 * number
            number -= 1
        if pairs != 2:
            score = 0
        return score

    @staticmethod
    def three_of_a_kind(*dice):
        score = 0
        number = 6
        while number >= 1:
            if dice.count(number) >= 3:
                score += 3 * number
                break
            number -= 1
        return score

    @staticmethod
    def four_of_a_kind(*dice):
        score = 0
        number = 6
        while number >= 1:
            if dice.count(number) >= 4:
                score += 4 * number
                break
            number -= 1
        return score

    @staticmethod
    def small_straight(*dice):
        for number in range(1, 6):
            if dice.count(number) != 1:
                return 0
        return 15

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def full_house(*dice):
        score = 0
        pair = Yatzy.one_pair(*dice)
        three = Yatzy.three_of_a_kind(*dice)
        score += pair + three
        return score
