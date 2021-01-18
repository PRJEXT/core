from sklearn.metrics import f1_score


def evaluate_model(y_test, prediction):
    '''Avalia o modelo utilizando a métrica F1 Score.'''
    score = f1_score(y_test, prediction)
    
    return score
