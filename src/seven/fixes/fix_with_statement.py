from . import FixFutureFeature


class FixWithStatement(FixFutureFeature):
    """Adds `from __future__ import with_statement`."""

    PATTERN = 'with_stmt'

    feature = 'with_statement'
