from nltk.corpus import brown
from nltk import FreqDist
from nltk import DecisionTreeClassifier
from nltk.classify import accuracy

# Começamos procurando os sufixos mais comuns

suffix_fdist = FreqDist()

for word in brown.words():
    word = word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
# print(common_suffixes)

# Nesta função, o extrator se baseia apenas na informação sobre os sufixos comuns (Se tiver) das palavras dadas
'''def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
    return features
'''

def pos_features(sentence, i):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]

    return features

tagged_words = brown.tagged_words(categories='news')

# print(tagged_words)

featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
size = int(len(featuresets)*0.1)
train_set, test_set = featuresets[:1000], featuresets[1000:2000]
classifier = DecisionTreeClassifier.train(train_set)
ac = accuracy(classifier, test_set)
print(ac)

print(classifier.classify(pos_features('cats')))

print(classifier.pseudocode(depth=4))