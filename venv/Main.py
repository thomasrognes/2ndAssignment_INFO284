import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn.mixture import GaussianMixture
from sklearn.mixture import k_means


with open("seeds_dataset.txt", "r") as myFile:
    data = myFile.read()

#Main metode som printer ut datasettet.
if __name__ == '__main__':
    print("Rad1 " + "   " + "Rad2 " + "   " + "Rad3 " + "   " + "Rad4 " + "   " + "Rad5 " + "   " + "Rad6 " + "   " + "Rad7 " + "   " "Rad8 ")
    print(data)

