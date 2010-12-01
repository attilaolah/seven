Usage
=====

To import `Python 2.6` or `Python 2.7` code to a `Python 2.5` interpreter, first do this::

    >>> import seven
    >>> seven.start()

    >>> # import Python 2.x code

    >>> seven.stop()  # optional

The above will install an import hook and preprocess all modules before
importing them using `lib2to3` from the `Python 2.7` `stdlib`. It is mainly
intended to be used on `Google App Engine`. Note that exceptions raised at
import time in wrapped modules may look cryptic. This might be improved in the
future.
