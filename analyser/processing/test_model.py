def test_model(X_test, model, model_type):
    '''Realiza o teste do modelo.'''
    if model_type == 'naive':
        prediction = model.classify(X_test) # TODO: conferir documentação
    elif model_type == 'svc':
        prediction = model.predict(X_test)
    
    return prediction
