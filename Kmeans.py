# 导入numpy库
from numpy import *


# K-均值聚类辅助函数

# 文本数据解析函数
from sklearn.cluster.k_means_ import KMeans


def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine)) #map all elements to float()
        # fltLine = list(map(float,curLine)) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))  # la.norm(vecA-vecB)


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))  # create centroid mat
    for j in range(n):  # create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:, j])
        print(minJ)
        # rangeJ = float(list(max(dataSet[:, j])) - list(minJ))
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    return centroids


def kkMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))  # create mat to assign data points
    # to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # for each data point assign it to the closest centroid
            minDist = inf;
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI;
                    minIndex = j
            if clusterAssment[i, 0] != minIndex: clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print
        centroids
        for cent in range(k):  # recalculate centroids
            print("//////////////////////////////")
            print(clusterAssment[0:, 1].A)
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            print(clusterAssment[:, 0].A)
            print(clusterAssment[:, 0].A.__class__)
            print(clusterAssment[:, 0].A == cent)
            print(nonzero(clusterAssment[:, 0].A == cent))
            print(nonzero(clusterAssment[:, 0].A == cent)[0])
            print("//////////////////////////////")
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]  # get all the point in this cluster
            centroids[cent, :] = mean(ptsInClust, axis=0)  # assign centroid to mean
    return centroids, clusterAssment

if __name__ == "__main__":
    print("K-means")
    # fileName = "testSet2.txt"
    fileName = "./testSet2.txt"
    dataMat = mat(loadDataSet(fileName))
    print(min(dataMat[:,0]))
    print(min(dataMat[:,1]))
    print(max(dataMat[:,1]))
    print(max(dataMat[:,0]))
    print("*********************")
    print(randCent(dataMat, 2))
    print("*******************")
    print(distEclud(dataMat[0], dataMat[1]))
    print("*******************")
    print(dataMat.__class__)
    m, c = kkMeans(dataMat, 4)
    print("---------------------")
    print(m)
    print("---------------------")
    print(c)