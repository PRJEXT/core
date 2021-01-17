from sklearn.model_selection import train_test_split
from analyser.preprocessing.bag_of_words import generate_bag_of_words


def split(data_frame, sentiment_column, preprocessed_column):
    '''Realiza a separação dos dados de treino e de teste a partir das colunas de reviews e sentimentos do data frame.'''
    # X representa o que será utilizado para a predição (reviews pré-processadas/variável independente)
    X = generate_bag_of_words(data_frame, preprocessed_column)
    # y representa o que queremos prever (sentimentos/variável dependente)
    y = data_frame[sentiment_column]

    seed = 1234 # TODO: mudar para um lugar central (compartilhado com o módulo de importação de dados)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=seed)

    sets = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
    }

    return sets
