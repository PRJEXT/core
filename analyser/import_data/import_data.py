import pandas as pd


def import_data(path=None, size='full'):
    '''Importa o dataset e retorna um dataframe.'''
    if path:
        path = path
    else:
        path = 'data/train.csv'
    
    data_frame = pd.read_csv(path)

    if size == 'full':
        return data_frame
    elif size == 'small':
        return data_frame.sample(1000)
