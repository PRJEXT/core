import pandas as pd


def import_data(path=None):
    '''Importa o dataset e retorna um dataframe.'''
    if path:
        path = path
    else:
        path = 'data/train.csv'
    
    data_frame = pd.read_csv(path)
    return data_frame
