import random
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]  # Lista das 2000 palavras mais frequentes


# Extrator que checa a presença dessas palavras no documento

def document_features(document):
    document_words = set(
        document)  # Passado para o conjunto porque é mais rápido verificar a ocorrência de um termo aqui do que numa lista
    features = {}

    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)

    return features

# print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = NaiveBayesClassifier.train(train_set)

print(accuracy(classifier, test_set))

classifier.show_most_informative_features(5)