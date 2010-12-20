from .lib2to3 import refactor
from . import exceptions


class RefactoringTool(object):
    """Simple refactoring tool wrapper."""

    fixes = [  # overwrite fixers in a subclass to disable
        'seven.fixes.fix_with_statement',
        'seven.fixes.fix_absolute_import',
        'seven.fixes.fix_division',
        'seven.fixes.fix_class_decorators',
    ]

    def __init__(self):
        """Initialize separate refactoring tools for each fix."""
        self.children = [refactor.RefactoringTool([fix]) for fix in self.fixes]

    def __call__(self, code, name='<string>'):
        """Call each refactoring tool ang catch marker exceptions."""
        code = code if code.endswith('\n') else code + '\n'
        future_imports = []
        for child in self.children:
            try:
                code = unicode(child.refactor_string(code, name))
            except exceptions.FutureImportNeeded, exc:
                future_imports.append(exc.message)
        if future_imports:
            future_imports = ', '.join(future_imports)
            code = 'from __future__ import %s\n' % future_imports + code

        return code
