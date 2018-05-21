import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import datasets
from sklearn import svm
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

x = [1, 2, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]



with open("seeds_dataset.txt", "r") as df:
    data = df.read()



#Main metode som printer ut datasettet.
if __name__ == '__main__':
    print("______________________________________________________________")
    print("Rad1 " + "   " + "Rad2 " + "   " + "Rad3 " + "   " + "Rad4 " + "   " + "Rad5 " + "   " + "Rad6 " + "   " + "Rad7 " + " " "Rad8 ")
    print(data)
    print("______________________________________________________________")
    plt.scatter(x, y)
    plt.savefig("test.png")






#https://mubaris.com/2017/10/01/kmeans-clustering-in-python/