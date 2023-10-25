import csv


def get_data(filename):
    """
    Read the contents of the given file. Assumes the file
    in a comma-separated format, with 6 elements in each entry:
    0. Name (string), 1. Gender (string), 2. Age (int)
    3. Division (int), 4. Country (string), 5. Overall time (float)
    Returns: dict containing a list for each of the 6 variables.
    """

    data = {'rank': [], 'gender': [], 'age': [], 'country': [], 'time': []}

    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            data['rank'].append(row["Rank_Tot"])
            data['age'].append(int(row["Age"]))
            data['gender'].append(row["Gender"])
            data['country'].append(["Country"])
            data['time'].append(float(row["Result_sec"]))
    f.close()
    return data


def load_titanic_data(filename):
    data = {'name': [], 'gender': [], 'age': [], 'survived': [], 'pClass': []}

    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            if row["Age"] != '' and row["Sex"] != '' and row["Pclass"] != '' and row["Survived"] != "":
                data['name'].append(row["Name"])
                data['age'].append(int(float(row["Age"])))
                data['gender'].append(row["Sex"])
                data['pClass'].append(int(row["Pclass"]))
                data['survived'].append(int(row["Survived"]))
    f.close()
    data["gender"] = [0 if x.lower().startswith('f') else 1 for x in data["gender"]]
    return data
