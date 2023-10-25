import os

import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc

from comprag.chapter24.metrics import get_stats, specificity, sensitivity
from comprag.chapter24.preprocessing import build_marathon_examples, divide80_20


def apply_model(model, test_set, label, prob=0.5):
    test_feature_vecs = [e.get_features() for e in test_set]
    probs = model.predict_proba(test_feature_vecs)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if test_set[i].get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if test_set[i].get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def build_roc(model, test_set, label, title, plot=True):
    x_vals, y_vals = [], []
    p = 0.0
    while p <= 1.0:
        true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, label, p)
        x_vals.append(1.0 - specificity(true_neg, false_pos))
        y_vals.append(sensitivity(true_pos, false_neg))
        p += 0.01

    auroc = auc(x_vals, y_vals)

    if plot:
        plt.plot(x_vals, y_vals)
        plt.plot([0, 1], [0, 1, ], '--')
        plt.title(title + ' (AUROC = ' + str(round(auroc, 3)) + ')')
        plt.xlabel('1 - Specificity')
        plt.ylabel('Sensitivity')

    return auroc


if __name__ == "__main__":

    """
        Data: Boston Marathon 2019 results
    """
    data_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(data_dir, "Dataset-Boston-2019.csv")

    # Build examples
    examples = build_marathon_examples(data_path)
    training, test = divide80_20(examples)

    featureVecs, labels = [], []
    for e in training:
        featureVecs.append([e.get_age(), e.get_time()])
        labels.append(e.get_label())

    model = LogisticRegression().fit(featureVecs, labels)

    # #ROC AUC
    auroc = build_roc(model, test, 'M', 'ROC for Predicting Gender')
    print("auroc: ", auroc)
    # plt.show()

    # print('Feature weights for label M:', 'age =', str(round(model.coef_[0][0], 3)) + ',', 'time =',
    # round(model.coef_[0][1], 3))

    truePos, falsePos, trueNeg, falseNeg = apply_model(model, test, 'M', 0.7)
    get_stats(truePos, falsePos, trueNeg, falseNeg)
