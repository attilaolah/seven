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
