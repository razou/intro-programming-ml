def read_mammal_data(f_name):
    data_file = open(f_name, 'r')
    num_features = 0
    for line in data_file:
        if line[0:6] == '#Label':
            break
        if line[0:5] != '#Name':
            num_features += 1

    feature_vals, species_names, label_list = [], [], []
    for i in range(num_features):
        feature_vals.append([])

    for line in data_file:
        data_line = line[:-1].split(',')  # remove newline, then split
        species_names.append(data_line[0])
        class_label = data_line[-1]
        label_list.append(class_label)
        for i in range(num_features):
            feature_vals[i].append(float(data_line[i + 1]))

    feature_vector_list = []
    for mammal in range(len(species_names)):
        feature_vector = []
        for feature in range(num_features):
            feature_vector.append(feature_vals[feature][mammal])
        feature_vector_list.append(feature_vector)

    return feature_vector_list, label_list, species_names


def read_and_normalize_mammal_data(f_name, scale):
    data_file = open(f_name, 'r')
    num_features = 0
    # Process lines at top of file
    for line in data_file:
        if line[0:6] == '#Label':
            break
        if line[0:5] != '#Name':
            num_features += 1

    # Produce featureVals, speciesNames, and labelList
    feature_vals, species_names, label_list = [], [], []
    for i in range(num_features):
        feature_vals.append([])

    # Continue processing lines in file, starting after comments
    for line in data_file:
        data_line = line[:-1].split(',')
        species_names.append(data_line[0])
        class_label = data_line[-1]
        label_list.append(class_label)
        for i in range(num_features):
            feature_vals[i].append(float(data_line[i + 1]))

    for i in range(num_features):
        feature_vals[i] = scale(feature_vals[i])

    feature_vector_list = []

    for mammal in range(len(species_names)):
        feature_vector = []
        for feature in range(num_features):
            feature_vector.append(feature_vals[feature][mammal])
        feature_vector_list.append(feature_vector)

    return feature_vector_list, label_list, species_names
