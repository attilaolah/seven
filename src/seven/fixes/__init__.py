from ..lib2to3 import fixer_base

from .. import exceptions


class FixFutureFeature(fixer_base.BaseFix):
    """Adds `from __future__ import <feature>`."""

    PATTERN = 'file_input'

    feature = NotImplemented  # subclasses must define this

    def transform(self, node, results):
        """Raise an exception to be caught later."""
        raise exceptions.FutureImportNeeded(self.feature)
