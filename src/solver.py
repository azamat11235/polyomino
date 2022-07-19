import numpy as np

def solve(table, polyominoes):
    i = 0
    while 0 <= i < len(polyominoes):
        if (table.put(polyominoes[i])):
            i += 1
        elif i == 0:
            return False
        else:
            table.pop()
            polyominoes[i].restart()
            i -= 1
            while (i > 0 and not polyominoes[i].next(table.width, table.height)):
                table.pop()
                polyominoes[i].restart()
                i -= 1
            if i == 0 and not polyominoes[i].next(table.width, table.height):
                return False
    return True
