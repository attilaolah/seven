from . import FixFutureFeature


class FixDivision(FixFutureFeature):
    """Adds `from __future__ import division`."""

    feature = 'division'
