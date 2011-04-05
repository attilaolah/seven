# Search for any global configuration:
try:
    from sevenconfig import log
except ImportError:
    try:  # PyFlakes
        log
    except NameError:
        log = True
try:
    from sevenconfig import speedup
except ImportError:
    try:  # PyFlakes
        speedup
    except NameError:
        speedup = True

# Then, only then, come the rest of the imports:
import seven.hook


__all__ = 'start', 'stop'

globalhook = None


def start(modules=None):
    global globalhook
    if globalhook is None:
        globalhook = seven.hook.Hook()
    globalhook.start(modules)


def stop():
    global globalhook
    if globalhook is not None:
        globalhook.stop()
        globalhook = None
