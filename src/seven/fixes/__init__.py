from ..lib2to3 import fixer_base

from .. import exceptions


class FixFutureFeature(fixer_base.BaseFix):
    """Adds `from __future__ import <feature>`."""

    PATTERN = 'file_input'

    BM_compatible = True

    @property
    def feature(self):
        raise NotImplementedError('Subclasses must set the feature.')

    def start_tree(self, tree, name):
        """Do not add future feature if already imported."""
        super(FixFutureFeature, self).start_tree(tree, name)
        self.skip = self.feature in tree.future_features

    def transform(self, node, results):
        """Raise an exception to be caught later."""
        raise exceptions.FutureImportNeeded(self.feature)
