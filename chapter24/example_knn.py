import random
import time

from matplotlib import pyplot as plt

from comprag.chapter24.preprocessing import build_marathon_examples, divide80_20
from comprag.chapter24.metrics import get_stats, accuracy
import os

random.seed(20)


def find_k_nearest(example, example_set, k):
    k_nearest, distances = [], []
    for i in range(k):
        k_nearest.append(example_set[i])
        distances.append(example.feature_dist(example_set[i]))
    max_dist = max(distances)

    for e in example_set[k:]:
        dist = example.feature_dist(e)
        if dist < max_dist:
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest, distances


def k_nearest_classify(training_set, test_set, label, k):
    """Assumes training and testSet lists of examples, k an int
    Uses a k-nearest neighbor classifier to predict
    whether each example in testSet has the given label
    Returns number of true positives, false positives,
    true negatives, and false negatives"""

    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        nearest, distances = find_k_nearest(e, training_set, k)
        num_match = 0
        for i in range(len(nearest)):
            if nearest[i].get_label() == label:
                num_match += 1
        if num_match > k // 2:
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1

    return true_pos, false_pos, true_neg, false_neg


def findK(training, min_k, max_k, num_folds, label):
    # Find average accuracy for range of odd values of k
    accuracies = []
    for k in range(min_k, max_k + 1, 2):
        score = 0.0
        start_time = time.time()
        for i in range(num_folds):
            fold = random.sample(training, min(5000, len(training)))
            examples, test_set = divide80_20(fold)
            true_pos, false_pos, true_neg, false_neg = k_nearest_classify(examples, test_set, label, k)
            score += accuracy(true_pos, false_pos, true_neg, false_neg)
            accuracies.append(score / num_folds)

        print(f"K: {k}, Time: {time.time() - start_time} sec =========> Accuracy: {score / num_folds}")
    plt.plot(range(min_k, max_k + 1, 2), accuracies)
    plt.title('Average Accuracy vs k (' + str(num_folds) + ' folds)')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.show()


if __name__ == "__main__":

    """
    Data: Boston Marathon 2019 results
    """
    data_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(data_dir, "Dataset-Boston-2019.csv")

    # Build examples
    examples = build_marathon_examples(data_path)

    # Split into train and test
    #training_data, test_data = divide80_20(examples)
    #truePos, falsePos, trueNeg, falseNeg = k_nearest_classify(training_data, test_data, 'M', 9)

    # Print performances
    #get_stats(truePos, falsePos, trueNeg, falseNeg)

    # Find best k
    findK(examples, 1, 21, 1, 'M')
