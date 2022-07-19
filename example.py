import numpy as np
import src.polyomino as polyomino
import src.table as table
import src.solver as solver


def run(fname):
    f = open(fname)

    tableWidth, tableHeight = map(int, f.readline().split())
    tabl = table.Table(tableWidth, tableHeight)

    polyominoes = []

    nRectPolyominoes = int(f.readline())
    for _ in range(nRectPolyominoes):
        width, height, count = map(int, f.readline().split())
        for _ in range(count):
            polyominoes.append(polyomino.RectanglePolyomino(width, height))

    nLPolyominoes = int(f.readline())
    for _ in range(nLPolyominoes):
        width, height, count = map(int, f.readline().split())
        for _ in range(count):
            polyominoes.append(polyomino.LPolyomino(height, width))

    print(fname, solver.solve(tabl, polyominoes), sep=': ')


run('input_true.txt')
run('input_false.txt')
