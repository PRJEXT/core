from nltk.classify import NaiveBayesClassifier as nbc
from sklearn.svm import SVC


def train_model(X_train, y_train, model_type):
    '''Realiza o treinamento do modelo.'''
    if model_type == 'naive':
        model = nbc.train(y_train)
    elif model_type == 'svc':
        model = SVC(kernel='linear')
        model.fit(X_train, y_train)

    return model
