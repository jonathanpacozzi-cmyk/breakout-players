"""Building the player-season table and the target.

Rule to respect everywhere: a feature for the prediction at 1 July of year t may only use
information dated BEFORE that date (otherwise: data leakage).

Functions to write once the proposal is approved. Declare any AI help in LOG_OUTILS.md.
"""


def assign_season(date):
    """Map a match date to a season label (e.g. 2023-09-02 -> 2023, season 2023/24, starting 1 July)."""
    raise NotImplementedError


def build_player_season_table(appearances, valuations, players, competitions, clubs):
    """One row per player and season, with features known at 1 July and the target."""
    raise NotImplementedError


def add_target(table):
    """Add the breakout label using the thresholds in config.py."""
    raise NotImplementedError
