import numpy as np


class Table:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._configurations = []

    def put(self, polyomino):
        if not self._configurations:
            newConfiguration = polyomino.getPoints()
        else:
            newConfiguration = np.vstack([self._configurations[-1], polyomino.getPoints()])
        isSuc = self._checkPoints(newConfiguration)
        while (not isSuc and polyomino.next(self.width, self.height)):
            newConfiguration = np.vstack([self._configurations[-1], polyomino.getPoints()])
            isSuc = self._checkPoints(newConfiguration)
    
        if not isSuc:
            return False
        self._configurations.append(newConfiguration)
        return True
    
    def pop(self):
        self._configurations.pop()

    def _checkPoints(self, arr):
        l = np.all(arr >= 0)
        r = np.all(arr[:, 0] < self.width)
        t = np.all(arr[:, 1] < self.height)
        u = np.all(np.unique(arr, axis=0, return_counts=True)[1] == 1)
        return l and r and t and u

    def getLastConfiguration(self):
        if self._configurations:
            return self._configurations[-1]
