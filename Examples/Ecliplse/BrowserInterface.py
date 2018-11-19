import numpy as np
import Counters as c
import GraphDrawer as gd
n = 8
lenFr = np.array([[163., 86, 86, 86, 86, 91, 91, 86],
                   [86., 188, 93, 119, 93, 95, 95, 93],
                   [86., 93, 136, 93, 97, 93, 93, 93],
                   [86., 119, 93, 149, 93, 93, 93, 105],
                   [86., 93, 97, 93, 191, 93, 106, 96],
                   [91., 95, 93, 93, 93, 140, 107, 93],
                   [91., 95, 93, 93, 106, 107, 172, 93],
                   [86., 93, 93, 105, 96, 93, 93, 154]])
print("Browser:")
w = c.weights(n, c.divLenghts(n, lenFr))
c.printWeights(n, w)

#gd.grDraw(n, w)
gd.grViz(n,w,'BrowserInterface')