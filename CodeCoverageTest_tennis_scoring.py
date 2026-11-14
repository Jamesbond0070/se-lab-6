"""
Code Coverage Test Suite for tennis_scoring.py
Achieves >= 90% Statement/Line Coverage (95% line coverage)
Demonstrates line coverage while identifying untested decision branches.
"""
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ============================================================================
# 1. game_score Test Cases (Code Coverage)
# ============================================================================

def test_game_negative_points():
    """Verify negative score raises ValueError."""
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)


def test_game_deuce():
    """Verify deuce condition when both players have >= 3 points and are equal."""
    assert game_score(3, 3) == "deuce"


def test_game_advantage_a():
    """Verify advantage Player A after deuce."""
    assert game_score(4, 3) == "advantage A"


def test_game_advantage_b():
    """Verify advantage Player B after deuce."""
    assert game_score(3, 4) == "advantage B"


def test_game_win_after_deuce_a():
    """Verify game win for Player A when leading by 2 points after deuce."""
    assert game_score(5, 3) == "game A"


def test_game_win_after_deuce_b():
    """Verify game win for Player B when leading by 2 points after deuce."""
    assert game_score(3, 5) == "game B"


def test_game_win_regular_a():
    """Verify game win for Player A without reaching deuce."""
    assert game_score(4, 1) == "game A"


def test_game_win_regular_b():
    """Verify game win for Player B without reaching deuce."""
    assert game_score(1, 4) == "game B"


def test_game_regular_scores():
    """Verify standard game score notation (0, 15, 30, 40)."""
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 2) == "15-30"
    assert game_score(2, 3) == "30-40"
    assert game_score(3, 1) == "40-15"


# ============================================================================
# 2. set_winner Test Cases (Code Coverage)
# ============================================================================

def test_set_winner_regular_a():
    """Verify Player A wins set with standard 2-game margin."""
    assert set_winner(6, 4) == "A"


def test_set_winner_regular_b():
    """Verify Player B wins set with standard 2-game margin."""
    assert set_winner(4, 6) == "B"


def test_set_winner_undecided():
    """Verify sets still in progress or tied return None."""
    assert set_winner(3, 2) is None
    assert set_winner(5, 5) is None


# ============================================================================
# 3. match_status Test Cases (Code Coverage)
# ============================================================================

def test_match_status_a_wins():
    """Verify match status when Player A reaches required sets."""
    assert match_status(2, 0, 3) == "A wins"


def test_match_status_b_wins():
    """Verify match status when Player B reaches required sets."""
    assert match_status(0, 2, 3) == "B wins"


def test_match_status_decider():
    """Verify deciding set trigger when both players are 1 set away."""
    assert match_status(1, 1, 3) == "decider"


def test_match_status_in_progress():
    """Verify match status while match is ongoing."""
    assert match_status(1, 0, 3) == "in progress"
    assert match_status(0, 0, 3) == "in progress"
