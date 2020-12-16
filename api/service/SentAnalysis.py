import pickle
import re

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import download

# Esses pacotes do NLTK precisam ser baixados uma única vez antes de carregar os models.
# download('stopwords')
# download('wordnet')


class SentAnalysis():
    '''Classe principal do analisador de sentimentos.
    Possui como atributos os modelos de vetorizador e Support Vector Classifier (SVC),
    as stopwords e o lematizador (reduz as palavras aos seus radicais).
    Possui os métodos clean_text, responsável pela limpeza do texto recebido do servidor,
    e predict, que aplica o modelo de análise, retornando a classificação do sentimento
    identificada no texto.
    '''
    def __init__(self):
        with open('models/vectorizer.pkl', 'rb') as file:
            self.vectorizer = pickle.load(file)

        with open('models/model.pkl', 'rb') as file:
            self.model = pickle.load(file)

        self.stop_words = set(stopwords.words('portuguese'))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        text = re.sub(r'[^\w\s]', '', text, re.UNICODE)
        text = text.lower()
        text = [self.lemmatizer.lemmatize(token) for token in text.split(' ')]
        text = [self.lemmatizer.lemmatize(token, 'v') for token in text]
        text = [word for word in text if not word in self.stop_words]
        text = ' '.join(text)

        return text

    def predict(self, text: str):
        text = self.clean_text(text)
        X = self.vectorizer.transform([text])
        result = self.model.predict(X)

        if result[0] == 0:
            return 'negative'
        else:
            return 'positive'
