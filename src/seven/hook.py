import imp
import os
import sys

from . import refactor


# Initialize a refactoring tool
rtool = refactor.RefactoringTool()


class Hook(dict):
    """Import hook, see `PEP 302`_.

    .. _`PEP 302`: http://www.python.org/dev/peps/pep-0302/

    Usage::

        >>> from seven.hook import Hook
        >>> hook = Hook()
        >>> hook
        {}

        >>> hook.start()
        >>> # import Python 2.7 code

        >>> hook.stop()  # optional

    """

    def start(self, modules=None):
        """Insert the hook to `sys.meta_path`."""
        if self not in sys.meta_path:
            sys.meta_path.insert(0, self)
        self.modules = modules

    def stop(self):
        """Remove the hook from `sys.meta_path`."""
        sys.meta_path = [x for x in sys.meta_path if x is not self]

    def find_module(self, name, fullpath):
        """Return the module loader object, `self`."""
        if self.modules is not None:
            # We have a whitelist of modules, process only those in the list
            process = False
            for module in self.modules:
                if name == module or name.startswith('%s.' % module):
                    process = True
            if not process:
                return  # module not in the whitelist
        if name.rsplit('.')[-1] == '__future__':
            return  # don't do anything with __future__ imports
        if fullpath is not None:
            self[name] = fullpath
            return self
        try:
            self[name] = imp.find_module(name)
            return self
        except ImportError:
            pass  # gently step aside

    def load_module(self, fullname):
        """Find the module, and pass it to `create_module()`."""
        if isinstance(self[fullname], tuple):
            # The module is already found
            return self.create_module(fullname, *self[fullname])

        # Otherwise, we need to find the module in a list of paths
        mod = imp.find_module(fullname.rsplit('.')[-1], self[fullname])
        return self.create_module(fullname, *mod)

    def create_module(self, fullname, file, pathname, description):
        """Alter and execute the module source code, and return a module."""
        suffix, mode, type = description
        if type not in (imp.PY_SOURCE, imp.PKG_DIRECTORY):
            # Do nothing, not a Python source file
            return imp.load_module(fullname, file, pathname, description)
        elif type == imp.PKG_DIRECTORY:
            file = open(os.path.join(pathname, '__init__.py'), 'rb')

        # Create our own module object
        mod = imp.new_module(fullname)
        sys.modules.setdefault(fullname, mod)

        # The module lives in a regular file
        mod.__file__ = pathname
        exec rtool(file.read(), fullname) in mod.__dict__

        return mod
