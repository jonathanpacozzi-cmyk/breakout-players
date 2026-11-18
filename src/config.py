"""Shared paths and constants. Every notebook imports from here, so a threshold is changed in one place only."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"
TABLES = ROOT / "tables"

# --- Definition of a "breakout" (PROVISIONAL: check how many breakouts each season gives before fixing) ---
REFERENCE_DATE = (7, 1)          # (month, day): last valuation known before 1 July each year
MIN_START_VALUE = 1_000_000      # EUR: ignore players valued below this at the start
GROWTH_FACTOR = 2.0              # value must at least double...
MIN_ABSOLUTE_GAIN = 5_000_000    # EUR: ...and gain at least this much

# --- Temporal split (PROVISIONAL: depends on the seasons available once the panel is built) ---
TRAIN_LAST_SEASON = None
VALIDATION_SEASONS = None
TEST_SEASON = None

RANDOM_STATE = 42
