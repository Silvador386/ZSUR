import numpy as np
import random
from utils import L2_distance_matrix, find_cls_data_centers
from plot import plot_2D


def run(data, num_cls, plot=False):
    data = data.copy()
    error_cls = [0]
    classed_data = [data]

    while True:
        cls_max_err = int(np.argmax(error_cls))

        div_data, div_cls_idxs, div_error_cls = cluster_err(classed_data[cls_max_err], num_cls=2)
        classed_data.pop(cls_max_err)
        classed_data += div_data
        error_cls.pop(cls_max_err)
        error_cls += div_error_cls

        if len(classed_data) == num_cls:
            break

    center_data = find_cls_data_centers(classed_data)

    if plot:
        data2plot_named = {f"Center: {center[0]:.2f}, {center[1]:.2f}": data for data, center in
                           zip(classed_data, center_data)}
        data2plot_named["title"] = "Non - Binary Division"
        plot_2D(**data2plot_named)

    return classed_data, center_data, sum(error_cls)


def cluster_err(cls_center_data, num_cls=2):
    data = cls_center_data.copy()
    data_idxs_lists_to_centers = [[value] for value in random.sample(range(max(data.shape[0], num_cls)), num_cls)]
    center_data = data[[idx for data_idxs_of_center in data_idxs_lists_to_centers for idx in data_idxs_of_center]]

    dists_matrix = L2_distance_matrix(data, center_data)

    error_cls = [0 for i, _ in enumerate(data_idxs_lists_to_centers)]

    for idx, row in enumerate(dists_matrix):
        min_row_idx = np.argmin(row)
        if idx not in data_idxs_lists_to_centers[min_row_idx]:
            error_cls[min_row_idx] += row[min_row_idx]
            data_idxs_lists_to_centers[min_row_idx].append(idx)

    new_data = []
    for center_idxs in data_idxs_lists_to_centers:
        new_data.append(data[center_idxs])

    return new_data, data_idxs_lists_to_centers, error_cls
