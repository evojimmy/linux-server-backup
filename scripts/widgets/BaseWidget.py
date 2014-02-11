class BaseWidget(object):
    def __init__(self, path):
        self._path = path
    def expand(self):
        "Implement this in sub classes"
        raise Exception("Not implemented in Base class.")
