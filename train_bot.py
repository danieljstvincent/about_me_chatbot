import nltk
nltk.download()
from nltk.stem import WordNetLemmatizer
import json
import pickle


words = []
classes = []
documents = []
ignore_words = ['?', '!', '.']
data_file = open('intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # print(pattern, 'pattern', intent['patterns'], 'intent[patterns]')
        w = nltk.word_tokenize(pattern)
        print(w)
        # print('Token is: {}'.format(w))
        # words.extend(w)
        # documents.append((w, intent['tag']))

    #
    #     if intent['tag'] not in classes:
    #         classes.append(intent['tag'])
    #
    # print('Words list is: {}'.format(words))
    # print('Docs are: {}'.format(documents))
    # print('classes are: {}'.format(classes))

