"""Temporal split, baseline rule and evaluation helpers, shared by all modelling notebooks.

Functions to write once the proposal is approved. Declare any AI help in LOG_OUTILS.md.
"""


def temporal_split(table):
    """Split by season (train on earlier seasons, validate and test on later ones), never at random."""
    raise NotImplementedError


def baseline_rule(table):
    """Simple rule of thumb, e.g. 'young player whose playing time is increasing'."""
    raise NotImplementedError


def evaluate(y_true, y_pred):
    """Metrics suited to rare positives (see the course: confusion matrix, precision, recall, F1)."""
    raise NotImplementedError
