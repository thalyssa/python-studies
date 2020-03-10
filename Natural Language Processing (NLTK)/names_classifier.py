from nltk.corpus import names
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy
from nltk.classify import apply_features
import random

''' PRIMEIRA VERSÃO
def gender_features(word):
    return {'last letter': word[-1], 'length': len(word), 'first letter': word[0]}
'''


def gender_features(word):
    return {'suffix1': word[-1:], 'suffix2': word[-2:]}


# Separa os nomes importados dos arquivos em masculinos e femininos, reorganizando a lista de forma aleatória depois.
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in
                                                                         names.words('female.txt')])
random.shuffle(labeled_names)

# Processamento dos dados e divisão da lista entre um conjunto de treinamento e um conjunto de testes.
# O conjunto de treinamento é usado para treinar um novo classificador.
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = NaiveBayesClassifier.train(train_set)

''' Com isso já é possível "brincar" com nomes que não estão nos dados de treinamento, por meio de:

print(classifier.classify(gender_features('Dorime')))'''

print('Acurácia inicial')
print(accuracy(classifier, test_set))

# classifier.show_most_informative_features(5)

''' Para largas quantidades de dados, é melhor usar:

    train_set = apply_features(gender_features, labeled_names[500:])
    test_set = apply_features(gender_features, labeled_names[:500])
'''

# ANÁLISE DE ERRO

train_names = labeled_names[1500:]  # Dados de treinamento
devtest_names = labeled_names[500:1500]  # Dados para performar análise de erro
test_names = labeled_names[:500]  # Array contendo os dados de teste do modelo

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]

classifier = NaiveBayesClassifier.train(train_set)

print('\nAnálise de erro')
print(accuracy(classifier, devtest_set))
print()

# Lista de erros feitos pelo classificador na previsão de gêneros
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))

# Printa a lista de erros
'''
for (tag, guess, name) in sorted(errors):
    print('Correct: {:<8} Guess: {:<8s} Name: {:<30}'. format(tag, guess, name))
'''
