from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC


def train_model(X_train, y_train, model_type):
    '''Realiza o treinamento do modelo.'''
    if model_type == 'naive':
        # O algoritmo multinomial de naive bayes aceita matrix esparsa
        model = MultinomialNB()
    elif model_type == 'svc':
        model = SVC(kernel='linear')
    
    model.fit(X_train, y_train)

    return model
