from . import FixFutureFeature


class FixAbsoluteImport(FixFutureFeature):
    """Adds `from __future__ import absolute_import`."""

    feature = 'absolute_import'
