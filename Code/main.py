import load
import clustering
import data_division
import classification
from nn import neural_network
from utils import timeit


DATA_PATH = "../data/data.txt"
PLOT = True


@timeit
def main():
    # Load data
    data = load.load_data(data_path=DATA_PATH)

    # Clustering - Predict the number of classes.
    num_cls = clustering.run_clustering(data, plot=PLOT)
    print(f"Final number of classes:     {num_cls}")

    # Division - Divide data point to classes.
    classed_data, center_data, total_error = data_division.run_division(data, num_cls, plot=PLOT)

    # Classification - Run classifiers on the divided (classed) data.
    classification.run_classifiers(classed_data, center_data, plot=PLOT)

    # Neural network - Run 2-layer net on the classed data.
    neural_network.run(classed_data, num_cls)


if __name__ == "__main__":
    main()
