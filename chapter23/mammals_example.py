import random
from comprag.chapter17.central_limit_theorem import stdDev
from comprag.chapter23.clustering import Example, try_kmeans
from comprag.chapter23.data_reader import read_mammal_data, read_and_normalize_mammal_data
import numpy as np

random.seed(0)


def z_scale_features(vals):
    """Assumes vals is a sequence of floats"""
    result = np.array(vals)
    mean = sum(result) / len(result)
    result = result - mean
    return result / stdDev(result)


def i_scale_features(vals):
    """Assumes vals is a sequence of floats"""
    min_val, max_val = min(vals), max(vals)
    fit = np.polyfit([min_val, max_val], [0, 1], 1)
    return np.polyval(fit, vals)


def build_mammal_examples(feature_list, label_list, species_names):
    examples = []
    for i in range(len(species_names)):
        features = np.array(feature_list[i])
        example = Example(species_names[i], features, label_list[i])
        examples.append(example)
    return examples


def test_teeth(num_clusters: int, num_trials: int, data_path: str):
    features, labels, species = read_mammal_data(data_path)
    examples = build_mammal_examples(features, labels, species)
    best_clustering = try_kmeans(examples, num_clusters, num_trials)
    for c in best_clustering:
        names = ''
        for p in c.members():
            names += p.get_name() + ', '
        print('\n' + names[:-2])
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.get_label() == '0':
                herbivores += 1
            elif p.get_label() == '1':
                carnivores += 1
            else:
                omnivores += 1
        print(herbivores, 'herbivores,', carnivores, 'carnivores,', omnivores, 'omnivores')


def test_teeth2(num_clusters, num_trials, data_path, scale=lambda x: x):
    features, labels, species = read_and_normalize_mammal_data(data_path, scale)
    examples = build_mammal_examples(features, labels, species)
    best_clustering = try_kmeans(examples, num_clusters, num_trials)

    for c in best_clustering:
        names = ''
        for p in c.members():
            names += p.get_name() + ', '
        print('\n' + names[:-2])
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.get_label() == '0':
                herbivores += 1
            elif p.get_label() == '1':
                carnivores += 1
            else:
                omnivores += 1
        print(herbivores, 'herbivores,', carnivores, 'carnivores,', omnivores, 'omnivores')


if __name__ == "__main__":
    path_to_data = 'data.txt'
    n_clusters = 3
    n_trials = 20

    print('Clustering without scaling')
    test_teeth(num_clusters=n_clusters, num_trials=n_trials, data_path=path_to_data)
    print("= " * 20)
    print('\nClustering with z-scaling')
    test_teeth2(num_clusters=n_clusters, num_trials=n_trials, data_path=path_to_data, scale=z_scale_features)
    print("= " * 20)
    print('\nClustering with i-scaling')
    test_teeth2(num_clusters=n_clusters, num_trials=n_trials, data_path=path_to_data, scale=i_scale_features)
