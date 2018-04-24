'''
Random forests help to mitigate overfitting in decision trees.

Training data is spread across decision trees. The subsets are created by taking random samples with replacement.
This means that a given data point can be used in several subsets. (This is different from the subsets used in cross validation where each data point belongs to one subset).

Individual trees are trained with different subsets of features. So in our current problem,
one tree might be trained using eccentricity and another using concentration and the 4th adaptive moment.
By using different combinations of input features you create expert trees that are can better identify classes by a given feature.

The sklearn random forest only uses the first form of sampling.
'''

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from support_functions import generate_features_targets, plot_confusion_matrix, calculate_accuracy


# complete this function to get predictions from a random forest classifier
def rf_predict_actual(data, n_estimators):
    # generate the features and targets
    features, targets = generate_features_targets(data)

    # instantiate a random forest classifier
    rfc = RandomForestClassifier(n_estimators=n_estimators)

    # get predictions using 10-fold cross validation with cross_val_predict
    predicted = cross_val_predict(rfc, features, targets, cv=10)

    # return the predictions and their actual classes
    return predicted, targets


if __name__ == "__main__":
    data = np.load('galaxy_catalogue.npy')

    # get the predicted and actual classes
    number_estimators = 50  # Number of trees
    predicted, actual = rf_predict_actual(data, number_estimators)

    # calculate the model score using your function
    accuracy = calculate_accuracy(predicted, actual)
    print("Accuracy score:", accuracy)

    # calculate the models confusion matrix using sklearns confusion_matrix function
    class_labels = list(set(actual))
    model_cm = confusion_matrix(y_true=actual, y_pred=predicted, labels=class_labels)

    # plot the confusion matrix using the provided functions.
    plt.figure()
    plot_confusion_matrix(model_cm, classes=class_labels, normalize=False)
    plt.show()