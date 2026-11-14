"""
Branch Coverage Test Suite for tennis_scoring.py
Achieves 100% Branch Coverage and 100% Statement/Line Coverage.
Thoroughly tests every decision path, conditional edge, and compound boolean branch.
"""
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ============================================================================
# 1. game_score Test Cases (Full Branch Coverage)
# ============================================================================

def test_game_negative_points_player_a():
    """Branch: a < 0 evaluates to True (first condition of 'or')."""
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)


def test_game_negative_points_player_b():
    """Branch: a >= 0 and b < 0 (second condition of 'or' evaluated)."""
    with pytest.raises(ValueError, match="negative points"):
        game_score(0, -1)


def test_game_negative_points_both():
    """Branch: both a < 0 and b < 0."""
    with pytest.raises(ValueError, match="negative points"):
        game_score(-2, -3)


def test_game_regular_points():
    """Branch: a < 4 and b < 4, not reaching deuce threshold (return POINTS[a]-POINTS[b])."""
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 0) == "15-0"
    assert game_score(0, 1) == "0-15"
    assert game_score(1, 2) == "15-30"
    assert game_score(2, 1) == "30-15"
    assert game_score(2, 3) == "30-40"
    assert game_score(3, 2) == "40-30"
    assert game_score(3, 1) == "40-15"


def test_game_deuce():
    """Branch: a >= 3 and b >= 3 with a == b (returns 'deuce')."""
    assert game_score(3, 3) == "deuce"
    assert game_score(4, 4) == "deuce"
    assert game_score(5, 5) == "deuce"


def test_game_advantage_a():
    """Branch: a >= 3 and b >= 3 with a - b == 1 (returns 'advantage A')."""
    assert game_score(4, 3) == "advantage A"
    assert game_score(5, 4) == "advantage A"


def test_game_advantage_b():
    """Branch: a >= 3 and b >= 3 with b - a == 1 (returns 'advantage B')."""
    assert game_score(3, 4) == "advantage B"
    assert game_score(4, 5) == "advantage B"


def test_game_win_after_deuce_a():
    """Branch: a >= 3 and b >= 3 with a - b >= 2 (returns 'game A')."""
    assert game_score(5, 3) == "game A"
    assert game_score(6, 4) == "game A"


def test_game_win_after_deuce_b():
    """Branch: a >= 3 and b >= 3 with b - a >= 2 (returns 'game B')."""
    assert game_score(3, 5) == "game B"
    assert game_score(4, 6) == "game B"


def test_game_win_without_deuce_a():
    """Branch: a >= 4 while b < 3 (returns 'game A' without deuce)."""
    assert game_score(4, 0) == "game A"
    assert game_score(4, 1) == "game A"
    assert game_score(4, 2) == "game A"


def test_game_win_without_deuce_b():
    """Branch: b >= 4 while a < 3 (returns 'game B' without deuce)."""
    assert game_score(0, 4) == "game B"
    assert game_score(1, 4) == "game B"
    assert game_score(2, 4) == "game B"


# ============================================================================
# 2. set_winner Test Cases (Full Branch Coverage)
# ============================================================================

def test_set_winner_regular_a():
    """Branch: a >= 6 and a - b >= 2 (returns 'A')."""
    assert set_winner(6, 0) == "A"
    assert set_winner(6, 1) == "A"
    assert set_winner(6, 2) == "A"
    assert set_winner(6, 3) == "A"
    assert set_winner(6, 4) == "A"


def test_set_winner_regular_b():
    """Branch: b >= 6 and b - a >= 2 (returns 'B')."""
    assert set_winner(0, 6) == "B"
    assert set_winner(1, 6) == "B"
    assert set_winner(2, 6) == "B"
    assert set_winner(3, 6) == "B"
    assert set_winner(4, 6) == "B"


def test_set_winner_extended_two_game_margin():
    """Branch: extended sets with a - b >= 2 or b - a >= 2 past 6 games."""
    assert set_winner(7, 5) == "A"
    assert set_winner(5, 7) == "B"
    assert set_winner(8, 6) == "A"
    assert set_winner(6, 8) == "B"


def test_set_winner_tiebreak_a():
    """Branch: a == 7 and b == 6 (tiebreak win for A, returns 'A')."""
    assert set_winner(7, 6) == "A"


def test_set_winner_tiebreak_b():
    """Branch: b == 7 and a == 6 (tiebreak win for B, returns 'B')."""
    assert set_winner(6, 7) == "B"


def test_set_winner_undecided():
    """Branch: all conditional checks evaluate to False (returns None)."""
    assert set_winner(0, 0) is None
    assert set_winner(3, 2) is None
    assert set_winner(5, 5) is None
    assert set_winner(6, 5) is None
    assert set_winner(5, 6) is None
    assert set_winner(6, 6) is None
    assert set_winner(7, 7) is None


# ============================================================================
# 3. match_status Test Cases (Full Branch Coverage)
# ============================================================================

def test_match_status_a_wins():
    """Branch: sets_a == needed (Player A wins match)."""
    assert match_status(2, 0, 3) == "A wins"
    assert match_status(2, 1, 3) == "A wins"
    assert match_status(3, 0, 5) == "A wins"
    assert match_status(3, 1, 5) == "A wins"
    assert match_status(3, 2, 5) == "A wins"


def test_match_status_b_wins():
    """Branch: sets_b == needed (Player B wins match)."""
    assert match_status(0, 2, 3) == "B wins"
    assert match_status(1, 2, 3) == "B wins"
    assert match_status(0, 3, 5) == "B wins"
    assert match_status(1, 3, 5) == "B wins"
    assert match_status(2, 3, 5) == "B wins"


def test_match_status_decider():
    """Branch: sets_a == needed - 1 and sets_b == needed - 1 (deciding set)."""
    assert match_status(1, 1, 3) == "decider"
    assert match_status(2, 2, 5) == "decider"


def test_match_status_in_progress():
    """Branch: all previous conditions False (match in progress)."""
    assert match_status(0, 0, 3) == "in progress"
    assert match_status(1, 0, 3) == "in progress"
    assert match_status(0, 1, 3) == "in progress"
    assert match_status(0, 0, 5) == "in progress"
    assert match_status(1, 0, 5) == "in progress"
    assert match_status(2, 0, 5) == "in progress"
    assert match_status(2, 1, 5) == "in progress"
    assert match_status(0, 2, 5) == "in progress"
    assert match_status(1, 2, 5) == "in progress"
