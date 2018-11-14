import numpy as np

def divLenghts(n, lenFr):
    eps = 3
    divLen = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            divLen[i][j] = round(lenFr[i][j] / lenFr[i][i], eps)
    return divLen


def weights(n, divLen):
    wts = np.zeros((n, n))
    for j in range(n):
        for k in range(j + 1, n):
            wt = min(divLen[j][k], divLen[k][j])
            if (wt >= 0.5):
                wts[j][k] = wt
    return wts


def printWeights(n, weights):
    for j in range(n):
        for k in range(j, n):
            if (weights[j][k] != 0):
                print(j + 1, "-", k + 1, ":", weights[j][k])
def coms(str):
    out = "["
    num = 0
    for i in range(len(str)):
        if (str[i] == " "):
            if(num == 0):
                out += "."
            out += ","
            num += 1
        out += str[i]
        i += 1
    out += "]"
    print(out)
    # print(num)

def adjMatrix(n, weights):
    mtx = np.zeros((n, n))
    for j in range(n):
        for k in range(j, n):
            if (weights[j][k] != 0):
                mtx[j][k] = 1
                mtx[k][j] = 1
    return mtx
