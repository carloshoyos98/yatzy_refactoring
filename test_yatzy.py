from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance_scores_sum_of_all_dice():
    assert Yatzy.chance(2, 3, 4, 5, 1) == 15
    assert Yatzy.chance(3, 3, 4, 5, 1) == 16


def test_yatzy_scores_50():
    assert Yatzy.yatzy(4, 4, 4, 4, 4) == 50
    assert Yatzy.yatzy(6, 6, 6, 6, 6) == 50
    assert Yatzy.yatzy(6, 6, 6, 6, 3) == 0


def test_sum_of_ones():
    assert Yatzy.sum_of_ones(1, 2, 3, 4, 5) == 1
    assert Yatzy.sum_of_ones(1, 2, 1, 4, 5) == 2
    assert Yatzy.sum_of_ones(6, 2, 2, 4, 5) == 0
    assert Yatzy.sum_of_ones(1, 2, 1, 1, 1) == 4


def test_sum_of_twos():
    assert Yatzy.sum_of_twos(1, 2, 3, 2, 6) == 4
    assert Yatzy.sum_of_twos(2, 2, 2, 2, 2) == 10


def test_sum_of_threes():
    assert Yatzy.sum_of_threes(1, 2, 3, 2, 3) == 6
    assert Yatzy.sum_of_threes(2, 3, 3, 3, 3) == 12


def test_sum_of_fours():
    assert Yatzy.sum_of_fours(4, 3, 4, 4, 4) == 16
    assert Yatzy.sum_of_fours(4, 4, 4, 5, 5) == 12
    assert Yatzy.sum_of_fours(4, 4, 5, 5, 5) == 8
    assert Yatzy.sum_of_fours(4, 5, 5, 5, 5) == 4


def test_sum_of_fives():
    assert 10 == Yatzy.sum_of_fives(4, 4, 4, 5, 5)
    assert 15 == Yatzy.sum_of_fives(4, 4, 5, 5, 5)
    assert 20 == Yatzy.sum_of_fives(4, 5, 5, 5, 5)


def test_sum_of_sixes():
    assert 0 == Yatzy.sum_of_sixes(4, 4, 4, 5, 5)
    assert 6 == Yatzy.sum_of_sixes(4, 4, 6, 5, 5)
    assert 18 == Yatzy.sum_of_sixes(6, 5, 6, 6, 5)


def test_one_pair():
    assert 6 == Yatzy.one_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy.one_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy.one_pair(5, 3, 6, 6, 5)


def test_two_pairs():
    assert 16 == Yatzy.two_pairs(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pairs(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pairs(3, 3, 6, 5, 4)


def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)


def test_four_of_a_knd():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.small_straight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.small_straight(1, 2, 2, 4, 5)


def test_large_straight():
    assert 20 == Yatzy.large_straight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.full_house(6, 2, 2, 2, 6)
    assert 0 == Yatzy.full_house(2, 3, 4, 5, 6)
