from nltk.classify import NaiveBayesClassifier


def train_model(X_train, y_train):
    '''Realiza o treinamento do modelo.'''
    model = NaiveBayesClassifier(X_train, y_train)

    return model
