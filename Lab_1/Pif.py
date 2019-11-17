class ProgramInternalForm:
    def __init__(self):
        self._pif = []

    def add(self, code, index):
        self._pif.append((code, index))

    def __str__(self):
        s = 'Program Internal Form :\n'
        for i in range(len(self._pif)):
            s += str(self._pif[i][0]) + ' ' + str(self._pif[i][1]) + '\n'
        return s
