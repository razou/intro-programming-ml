import random
from sklearn.linear_model import LogisticRegression
random.seed(20)


if __name__ == "__main__":
    N = 50000
    featureVecs, labels = [], []
    for i in range(N):
        featureVecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5), random.random()])
        labels.append('A')
        featureVecs.append([random.gauss(0, 0.5), random.gauss(2, 0.), random.random()])
        labels.append('B')
        featureVecs.append([random.gauss(2, 0.5), random.gauss(0, 0.5), random.random()])
        labels.append('C')
        featureVecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5), random.random()])
        labels.append('D')

    model = LogisticRegression().fit(featureVecs, labels)
    print('model.classes_ =', model.classes_)

    for i in range(len(model.coef_)):
        print('For label', model.classes_[i], 'feature weights =', model.coef_[i])

    print('[0, 0] probs =', model.predict_proba([[0, 0, 1]])[0])
    print('[0, 2] probs =', model.predict_proba([[0, 2, 2]])[0])
    print('[2, 0] probs =', model.predict_proba([[2, 0, 3]])[0])
    print('[2, 2] probs =', model.predict_proba([[2, 2, 4]])[0])