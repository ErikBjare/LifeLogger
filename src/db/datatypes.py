class Datatype():
    def __init__(self, name, data):
        self.name = name
        self.data = None
        self._load(data)
        if self.data is None:
            raise ValueError("Data was not assigned")

        #raise DeprecationWarning("Not to be used")

    def _load(self, data):
        raise NotImplementedError

    def __str__(self):
        return str(self.data)


class String(Datatype):
    def __init__(self, data):
        Datatype.__init__(self, "string", data)

    def _load(self, data):
        self.data = data


class Number(Datatype):
    def __init__(self, data):
        Datatype.__init__(self, "string", data)

    def _load(self, data):
        self.data = float(data)

    def __str__(self):
        return str(self.data)