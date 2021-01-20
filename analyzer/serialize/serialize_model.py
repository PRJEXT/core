import pickle


def serialize_model(model):
    '''Serializa o modelo de IA.'''
    pickle.dump(model, open('models/model.pkl', 'wb'))
