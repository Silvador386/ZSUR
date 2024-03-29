import numpy as np
from utils import timeit
from plot import plot_1D


# @timeit
def agglomerate_clustering(data, dists_matrix, plot=False, a=2, b=3):
    a, b = 3, 4
    dists_matrix = dists_matrix.copy()

    dist_levels = []
    for _ in range(dists_matrix.shape[0]-1):
        mask = np.zeros_like(dists_matrix)
        np.fill_diagonal(mask, np.infty)
        min_row, min_col = np.unravel_index(np.argmin(dists_matrix + mask), dists_matrix.shape)

        dist_levels.append(dists_matrix[min_row][min_col])

        min_vector = np.minimum(dists_matrix[min_row, :], dists_matrix[min_col, :])

        dists_matrix[min_row, :] = min_vector
        dists_matrix[:, min_row] = min_vector.T

        dists_matrix = np.delete(dists_matrix, min_col, 0)
        dists_matrix = np.delete(dists_matrix, min_col, 1)

    return num_cls_dist(dist_levels, plot, a, b)


def num_cls_dist(levels, plot, a, b):
    num_cls = 1
    distances = np.array(levels)
    distances = np.sort(distances)

    dist_avg = np.average(distances)
    dist_std = np.std(distances)

    for dist in distances:
        if dist > a*dist_avg + b*dist_std:
            num_cls += 1

    if plot:
        kwargs = {"title": "Agglomerative clustering - distances"}
        plot_1D(distances, **kwargs)

    return num_cls
