def save_data(data_frame, file_name):
    '''Salva o data frame em um arquivo csv na pasta data.'''
    path = f'data/{file_name}.csv'

    data_frame.to_csv(path, index=False)
