import pickle


def serialize_vectorizer(vectorizer):
    '''Serializa o modelo de vetorizador de texto.'''
    pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb'))
