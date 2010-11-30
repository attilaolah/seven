import doctest
import unittest

from pprint import pprint


optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE
options = {'optionflags': optionflags, 'globs': {'pprint': pprint}}


TESTFILES = [
    'hook.txt',
    'refactor.txt',
]
TESTMODS = [
    'seven.hook',
]


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(file,
            **options) for file in TESTFILES
    ] + [
        doctest.DocTestSuite(mod,
            **options) for mod in TESTMODS],
    )
