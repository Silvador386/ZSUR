import random
import numpy as np
from utils import L2_distance_matrix, find_cls_data_centers
from plot import plot_2D


def k_means_div(data, num_cls, plot=False):
    data = data.copy()
    data_idxs_lists_to_centers = [[value] for value in random.sample(range(max(data.shape[0], num_cls)), num_cls)]
    center_data = data[[idx for data_idxs_of_center in data_idxs_lists_to_centers for idx in data_idxs_of_center]]

    while True:
        dists_matrix = L2_distance_matrix(data, center_data)

        error_cls = [0 for i, _ in enumerate(data_idxs_lists_to_centers)]

        for idx, row in enumerate(dists_matrix):
            min_row_idx = np.argmin(row)
            if idx not in data_idxs_lists_to_centers[min_row_idx]:
                error_cls[min_row_idx] += row[min_row_idx]
                data_idxs_lists_to_centers[min_row_idx].append(idx)

        classed_data = []
        for center_idxs in data_idxs_lists_to_centers:
            classed_data.append(data[center_idxs])

        new_center_data = find_cls_data_centers(classed_data)

        new_center_data = np.array(new_center_data)

        if (new_center_data == center_data).all():
            break

        data_idxs_lists_to_centers = [[] for _ in range(num_cls)]
        center_data = new_center_data


    if plot:
        data2plot_named = {f"Center: {center[0]:.2f}, {center[1]:.2f}": data
                           for data, center in zip(classed_data, new_center_data)}
        data2plot_named["title"] = "K - Means"
        plot_2D(**data2plot_named)

    return classed_data, new_center_data, sum(error_cls)



