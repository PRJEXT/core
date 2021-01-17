from sklearn.model_selection import train_test_split
from analyser.preprocessing.bag_of_words import generate_bag_of_words


def split(data_frame, sentiment_column, preprocessed_column):
    X = generate_bag_of_words(data_frame, preprocessed_column)
    y = data_frame[sentiment_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    sets = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
    }

    return sets
