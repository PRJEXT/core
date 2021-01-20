def test_model(X_test, model):
    '''Realiza o teste do modelo.'''
    prediction = model.predict(X_test)
    
    return prediction
