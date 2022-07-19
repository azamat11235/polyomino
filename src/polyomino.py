import numpy as np


class Polyomino:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._dx = 0
        self._dy = 0
        self._points = None # N_{points} x 2
    
    def rotate(self):
        g = np.array([0, 1, -1, 0]).reshape(2, 2) # Givens matrix
        self._points = self._points @ g
        xMin = self._points[:, 0].min()
        dx = abs(min(0, xMin))
        if dx != 0:
            dy = 0
            self._points += np.array([dx, dy])
        self.width, self.height = self.height, self.width

    def next(self, tableWidth, tableHeight):
        self._dx += 1
        if (self.width + self._dx <= tableWidth) and (self.height + self._dy <= tableHeight):
            return True
        self._dx = 0
        self._dy += 1
        if (self.width <= tableWidth) and (self.height + self._dy <= tableHeight):
            return True
        while self._turns > 0:
            self._turns -= 1
            self.rotate()
            self._dx = 0
            self._dy = 0
            if (self.width <= tableWidth) and (self.height <= tableHeight):
                return True
        return False
    
    def restart(self):
        self._dx = 0
        self._dy = 0
    
    def getPoints(self):
        return self._points + np.array([self._dx, self._dy])   


class RectanglePolyomino(Polyomino):
    def __init__(self, width, height):
        super().__init__(width, height)
        self._turns = (self.width != self.height)
        self._points = np.empty((height * width, 2), dtype=int)
        for xi in range(width):
            for yi in range(height):
                nPoint = xi * height + yi
                self._points[nPoint, 0] = xi
                self._points[nPoint, 1] = yi
    
    def restart(self):
        super().restart()
        self._turns = (self.width != self.height)


class LPolyomino(Polyomino):
    def __init__(self, height, width):
        super().__init__(width, height)
        self._turns = 4
        self._points = np.empty((height + width - 1, 2), dtype=int)
        for xi in range(width):
            self._points[xi, 0] = xi
            self._points[xi, 1] = 0
        for yi in range(1, height):
            nPoint = width + yi - 1
            self._points[nPoint, 0] = 0
            self._points[nPoint, 1] = yi
    
    def restart(self):
        super().restart()
        self._turns = 4
