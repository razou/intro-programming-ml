import os

import numpy as np
from sklearn.linear_model import LogisticRegression

from comprag.chapter17.central_limit_theorem import stdDev
from comprag.chapter22.distance_and_similarity import minkowskiDist
from comprag.chapter24.data_loader import load_titanic_data
from comprag.chapter24.logistic_regression import build_roc, apply_model
from comprag.chapter24.metrics import get_stats
from comprag.chapter24.preprocessing import divide80_20, build_marathon_examples


class Passenger(object):
    features = ('C1', 'C2', 'C3', 'age', 'male gender')

    def __init__(self, p_class, age, gender, survived, name):
        self.name = name
        self.featureVec = [0, 0, 0, age, gender]
        self.featureVec = [float(x) for x in self.featureVec]
        self.featureVec[p_class - 1] = 1
        self.label = survived
        self.cabinClass = p_class

    def distance(self, other):
        return minkowskiDist(self.featureVec, other.featureVec, 2)

    def get_class(self):
        return self.cabinClass

    def get_age(self):
        return self.featureVec[3]

    def get_gender(self):
        return self.featureVec[4]

    def get_name(self):
        return self.name

    def get_features(self):
        return self.featureVec[:]

    def get_label(self):
        return self.label


def summarize_stats(stats):
    """assumes stats a list of 5 floats: accuracy, sensitivity, specificity, pos. pred. val, ROC"""

    def print_stat(X, name):
        mean = round(sum(X) / len(X), 3)
        std = stdDev(X)
        print(' Mean', name, '=', str(mean) + ',', '95% confidence interval =', round(1.96 * std, 3))

    accs, sens, specs, ppvs, aurocs = [], [], [], [], []
    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        aurocs.append(stat[4])

    print_stat(accs, 'accuracy')
    print_stat(sens, 'sensitivity')
    print_stat(accs, 'specificity')
    print_stat(sens, 'pos. pred. val.')
    print_stat(aurocs, 'AUROC')


def test_models(examples, num_trials, print_stats, print_weights):
    survived = 1  # value of label indicating survived
    stats, weights = [], [[], [], [], [], []]
    for i in range(num_trials):
        training, test_set = divide80_20(examples)
        feature_vecs, labels = [], []

        for e in training:
            feature_vecs.append(e.get_features())
            labels.append(e.get_label())
        feature_vecs = np.array(feature_vecs)
        labels = np.array(labels)
        model = LogisticRegression().fit(feature_vecs, labels)

        for i in range(len(Passenger.features)):
            weights[i].append(model.coef_[0][i])

        true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, survived, 0.5)
        auroc = build_roc(model, test_set, survived, None, False)
        tmp = get_stats(true_pos, false_pos, true_neg, false_neg, False)
        stats.append(tmp + (auroc,))

    print('Averages for', num_trials, 'trials')
    if print_weights:
        for feature in range(len(weights)):
            feature_mean = sum(weights[feature]) / num_trials
            feature_std = stdDev(weights[feature])
            print(' Mean weight of', Passenger.features[feature], '=', str(round(feature_mean, 3)) + ',',
              '95% confidence interval =', round(1.96 * feature_std, 3))
    if print_stats:
        summarize_stats(stats)


def build_passenger_examples(file_name):
    data = load_titanic_data(file_name)
    examples = []
    for i in range(len(data['age'])):
        a = Passenger(data["pClass"][i], data["age"][i], data["gender"][i], data["survived"][i], data["name"][i])
        examples.append(a)
    return examples


if __name__ == "__main__":
    data_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(data_dir, "titanic.csv")

    # Build examples
    examples = build_passenger_examples(data_path)
    training, test = divide80_20(examples)

    test_models(examples, 100, True, False)
