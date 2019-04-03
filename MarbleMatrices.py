import numpy as np

def MarbleMatrices(arrows, marbles):
    A = np.zeros((marbles.shape[0],)*2)
    for arrow in arrows:
        A[arrow[1], arrow[0]] = 1
    return A * marbles

marbles = np.matrix('5; 2; 7; 10; 11; 24')
arrows = [[0, 2], [3, 5], [2, 4]]
marbles = MarbleMatrices(arrows, marbles)
print(marbles)