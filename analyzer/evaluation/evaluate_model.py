from sklearn.metrics import f1_score


def evaluate_model(y_test, prediction):
    '''Avalia o modelo utilizando a métrica F1 Score.'''
    # O parâmetro average é necessário por termos multiclass/multilabel targets,
    # ele altera como as métricas são calculadas
    score = f1_score(y_test, prediction, average='micro')
    
    return score
