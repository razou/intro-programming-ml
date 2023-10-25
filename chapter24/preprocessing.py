from comprag.chapter24.data_loader import get_data
import random

random.seed(20)


class Runner(object):

    def __init__(self, gender, age, time):
        self.featureVec = (age, time)
        self.label = gender

    def feature_dist(self, other):
        dist = 0.0
        for i in range(len(self.featureVec)):
            dist += abs(self.featureVec[i] - other.featureVec[i]) ** 2
        return dist ** 0.5

    def get_time(self):
        return self.featureVec[1]

    def get_age(self):
        return self.featureVec[0]

    def get_label(self):
        return self.label

    def get_features(self):
        return self.featureVec

    def __str__(self):
        return str(self.get_age()) + ', ' + str(self.get_time()) + ', ' + self.label


def build_marathon_examples(file_name):
    data = get_data(file_name)
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i], data['time'][i])
        examples.append(a)
    return examples


def divide80_20(examples):
    sample_indices = random.sample(range(len(examples)), len(examples) // 5)
    training_set, test_set = [], []
    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set
