import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) # alterar para português


def apply_clean_text(data_frame, text_column, preproc_column_name):
    '''Aplica o algoritmo de limpeza de textos em uma coluna do data frame.'''
    # Usa a lambda function para aplicar a função clean_text em cada linha do data frame
    data_frame[preproc_column_name] = data_frame[text_column].apply(lambda text: clean_text(text))


def clean_text(text):
    '''Algoritmo de limpeza de textos.'''
    # Define uma expressão regular para limpar o texto
    text = re.sub(r'[^w\s]', '', text, re.UNICODE)
    text = text.lower()
    
    # Lematiza cada palavra do texto (redução ao radical) utlizando a técnica de list comprehension
    text = [lemmatizer.lemmatize(word) for word in text.split(' ')]
    
    # Remove as stop words
    text = [word for word in text if not word in stop_words]
    text = ' '.join(text)
    
    return text
