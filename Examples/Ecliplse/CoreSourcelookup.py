import numpy as np
import Counters as c
import GraphDrawer as gd
n = 8
lenFr = np.array([[54., 0, 0, 0, 0, 0, 3, 3],
                   [0., 49, 44, 45, 20, 27, 20, 20],
                   [0., 44, 70, 70, 20, 20, 20, 20],
                   [0., 45, 70, 79, 20, 20, 20, 20],
                   [0., 20, 20, 20, 109, 37, 30, 50],
                   [0., 27, 20, 20, 37, 162, 46, 46],
                   [3., 20, 20, 20, 30, 46, 143, 143],
                   [3., 20, 20, 20, 50, 46, 143, 152]])
print("Sourcelookup:")
w = c.weights(n, c.divLenghts(n, lenFr))
c.printWeights(n, w)

#gd.grDraw(n, w)
gd.grViz(n,w,'CoreSourcelookup')