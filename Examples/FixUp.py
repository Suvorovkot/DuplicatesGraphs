import numpy as np
import Counters as c
import GraphDrawer as gd
n2 = 5
lenFr2 = np.array([[548., 437, 286, 305, 313],
                   [437., 1020, 286, 286, 578],
                   [286., 286, 300, 286, 260],
                   [305., 286, 286, 474, 262],
                   [313., 578, 260, 262, 785]])
print("Fixup:")
w2 = c.weights(n2, c.divLenghts(n2, lenFr2))
c.printWeights(n2, w2)

#gd.grDraw(n2, w2)
gd.grViz(n2,w2)