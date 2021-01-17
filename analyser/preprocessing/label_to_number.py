def label_to_number(data_frame, label_column):
    '''Transforma as categorias de sentimentos para números.'''
    data_frame[label_column] = data_frame[label_column].map({'positive': 1, 'negative': -1})
