import numpy as np
import Counters as c
import GraphDrawer as gd

n1 = 7
lenFr1 = np.array([[1062., 875, 650, 253, 421, 500, 250],
                   [875., 1027, 655, 235, 511, 499, 260],
                   [650., 655, 1039, 295, 570, 494, 256],
                   [253., 235, 295, 365, 254, 186, 115],
                   [421., 511, 570, 254, 814, 486, 222],
                   [500., 499, 494, 186, 486, 626, 221],
                   [250., 260, 256, 115, 222, 221, 452]])
print("Debug:")
w1 = c.weights(n1, c.divLenghts(n1, lenFr1))
c.printWeights(n1, w1)

#gd.grDraw(n1, w1)
gd.grViz(n1,w1,'DebugFunctions')