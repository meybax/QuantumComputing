import numpy as np

def MatrixMovement(mov, pos, times):
    for _ in range(times):
        pos = mov.dot(pos)
    return pos

pos = np.asarray([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
mov = np.asarray([[0.1, 0.7, 0.2,], [0.6, 0.2, 0.2], [0.3, 0.1, 0.6,]])
times = 15;
pos = MatrixMovement(mov, pos, times)
max = np.argmax(pos, 0)
print(pos)
print("pos 1 likely to go to " + str(max[0] + 1))
print("pos 2 likely to go to " + str(max[1] + 1))
print("pos 3 likely to go to " + str(max[2] + 1))




