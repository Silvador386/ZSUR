import numpy as np
from code.nn.two_layer_net import TwoLayerNet
from code.nn.solver import Solver
from code.plot import generate_mesh, plot_mesh


def run(classed_data):
    classed_data = np.copy(classed_data)
    cls_labels = np.array([i for i, single_data in enumerate(classed_data) for _ in single_data])
    merged_data = np.concatenate(classed_data)
    data = {
        'X_train': merged_data,
        'y_train': cls_labels,
        'X_val': merged_data,
        'y_val': cls_labels
    }

    input_size = 1 * 2
    hidden_size = 50
    num_classes = 3
    learning_rate = 0.5
    regularization_strength = 0
    number_epochs = 20

    print(f"Hs:{hidden_size}, lr: {learning_rate}, rg: {regularization_strength}, ne: {number_epochs}")
    model = TwoLayerNet(input_size,
                        hidden_size,
                        num_classes,
                        reg=regularization_strength)
    solver = Solver(model,
                    data,
                    optim_config={"learning_rate": learning_rate},
                    num_epochs=number_epochs,
                    verbose=True)
    solver.train()

    val_accuracy = solver.best_val_acc
    print(f"Accuracy: {val_accuracy}")

    mesh = generate_mesh(classed_data)
    labels_cls = solver.predict(mesh)

    kwargs = {"title": "Neural net"}
    plot_mesh(mesh, labels_cls, classed_data, **kwargs)



