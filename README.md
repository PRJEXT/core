# Core

Este repositório faz parte do projeto de análise de sentimentos de formulários em um ambiente educacional e é destinado ao analisador de sentimentos e à API em Python responsável pela integração com o back end.

## Configure o seu ambiente

Baixe o Python em https://www.python.org/downloads/ e instale em sua máquina. O download a partir do site vem com o pip (gerenciador de pacotes do Python) por padrão.

Com o Python e o pip instalados, crie uma pasta reservada com o nome deste repositório (core). Dentro dessa pasta, crie um ambiente virtual (virtual environment) do Python com o comando `python -m venv .venv` a partir da raiz do repositório.

> O Python já possui um módulo de criação de venv (como visto acima), mas existem outros módulos criados pela comunidade com suas vantanges e desvantagens.

Após o venv ser criado, será necessário ativá-lo com o comando `source .venv/bin/activate` se você estiver no Linux ou no Mac, ou `.\.venv\Scripts\activate` se estiver no Windows. Deve aparecer uma marcação no seu terminal indicando que o venv está ativo. Para desativá-lo, basta executar o comando `deactivate`.

> O procedimento de ativação deve ser feito sempre que o venv do projeto não estiver ativado e ele deve permanecer ativo enquanto você estiver rodando ou alterando o projeto.

Para instalar as dependências do projeto rode o comando `pip install -r requirements.txt` com o venv ativo.

As configurações com informações sensíveis ou globais devem ser feitas através do arquivo .env, que não deve ser compartilhado publicamente. Para ativá-lo renomeie o arquivo .env-example para apenas .env e insira os valores necessários.

## Rodando a API

Entre na pasta da API com `cd api` e inicie o servidor com o comando `uvicorn main:app --reload`. Você pode testar os endpoints no endereço http://localhost:8000/docs

## Treinando o modelo de Analisador de Sentimentos

Para realizar experimentos e treinar o modelo de analisador de sentimentos, primeiro acesse a pasta do analisador com `cd analyzer`. É necessário salvar o conjunto de dados (dataset) em formato .csv dentro da pasta "data".

As operações de manipulação dos dados, processamento e treino do modelo podem ser feitas a partir de um Jupyter notebook ou diretamente no interpretador do Python.

As funções disponíveis são as seguintes, considerando a ordem em que devem ser priorizadas:

1. **import_data:** importa os dados e retorna um data frame do pandas.
2. **label_to_number:** converte uma coluna do data frame contendo a classificação "positivo" e "negativo" para 1 e -1, respectivamente.
3. **apply_clean_text:** aplica o algoritmo de limpeza dos dados na coluna contendo as avaliações em texto.
4. **save_data:** salva o data frame em um arquivo .csv dentro da pasta "data".
5. **generate_bag_of_words:** gera uma matriz de vetores de palavras e suas respectivas contagens (bag of words) da coluna de avaliação e também retorna a instância do vetorizador.
6. **split_data:** separa os dados de treino e teste para ser utilizada no modelo.
7. **train_model:** realiza o treinamento do modelo utilizando o algoritmo de SVC ou Naive Bayes.
8. **test_model:** testa o modelo utilizando os dados de teste e retorna um array com as predições.
9. **evaluate_model:** avalia o desempenho do modelo utilizando a métrica F1 score, sendo a média harmônica entre precisão e recall.
10. **serialize_vectorizer:** serializa o vetorizador criado na geração da bag of words em um arquivo .pkl na pasta "models" para ser utilizado pela api.
11. **serialize_model:** serializa o modelo de analisador de sentimentos em um arquivo .pkl na pasta "models" para ser utilizado pela api.

Para utilizar os módulos, primeiramente faça a importação para o contexto do programa:
```python
from manage_data import import_data, save_data
from preprocessing import label_to_number, apply_clean_text, generate_bag_of_words
from processing import split_data, train_model, test_model
from evaluation import evaluate_model
from serialize import serialize_vectorizer, serialize_model
```

> O desempenho do modelo depende de diversos fatores, desde a escolha dos dados, o como eles são limpos e processados até quais métricas são utilizadas para inferir a sua acurácia. Portanto, os algoritmos apresentados serão atualizados conforme forem encontradas formas melhores de atingir os objetivos do projeto.