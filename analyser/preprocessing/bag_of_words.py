from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = set(stopwords.words('english')) # alterar para português


def generate_bag_of_words(data_frame, preprocessed_column):
    '''Gera a bag of words a partir da coluna de textos pré-processados do data frame.'''
    # Instancia o vetorizador passado as stop words para serem desconsideradas
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    
    # Aplica a vetorização (tokenização + contagem de ocorrências) retornando a matriz de features TF-IDF
    vectorized_reviews = vectorizer.fit_transform(data_frame[preprocessed_column])

    return vectorized_reviews
