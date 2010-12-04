from . import FixFutureFeature


class FixAbsoluteImport(FixFutureFeature):
    """Adds `from __future__ import absolute_import`."""


    PATTERN = """
    import_from< 'from' imp=any 'import' ['('] any [')'] >
    |
    import_name< 'import' imp=any >
    """

    #PATTERN = 'import_stmt< import_name | import_from >'

    feature = 'absolute_import'
