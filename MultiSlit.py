import numpy as np
np.set_printoptions(suppress=True,linewidth=1000,threshold=100)

def MultiSlit(slits, targets, prob):
    states = np.identity(slits + targets + 1)
    states[0, 0] = 0
    slitChance = 1 / slits
    for i in range(slits):
        states[i + 1, 0] = slitChance
        states[i + 1, i + 1] = 0
        for j in range(targets):
            states[slits + j + 1, i + 1] = prob[i, j]
    return states.dot(states)[slits + 1:, 0]


slits = 3
targets = 5
# prob must have [slits] rows and [targets] columns
prob = np.asarray([[0.5, 0.5, 0, 0, 0], [0, 0.2, 0.4, 0.2, 0], [0, 0, 0, 0.5, 0.5]])
states = MultiSlit(slits, targets, prob)
print(states)