import numpy as np
from bayes import bayes
from vector_quantization import vector_quantization
from k_nearest_neighbour import knn_classifier
from rosenblatt import rosenblatt
from constant_increase_classifier import constant_increase
from utils import timeit


@timeit
def run_classifiers(classed_data, center_data, plot=False):
    bayes(classed_data, center_data, plot)
    vector_quantization(classed_data, center_data, plot)
    knn_classifier(classed_data)
    num_iter = rosenblatt(classed_data)
    print(f"Rosenblatt - number of iterations:        {num_iter}")
    num_iter = constant_increase(classed_data)
    print(f"Constant increase - number of iterations: {num_iter}")

