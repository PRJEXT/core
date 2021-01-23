from os import getenv
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
SEED = int(getenv('SEED'))


def import_data(file_name, sample='full'):
    '''Importa um arquivo csv da pasta data e retorna um dataframe.'''
    path = f'data/{file_name}.csv'
    
    data_frame = pd.read_csv(path)

    if sample == 'full':
        return data_frame
    else:
        return data_frame.sample(sample, random_state=SEED)
