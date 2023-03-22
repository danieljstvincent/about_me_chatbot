import nltk
from nltk import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
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
        print('Token is: {}'.format(w))
        words.extend(w)
        documents.append((w, intent['tag']))


        if intent['tag'] not in classes:
            classes.append(intent['tag'])

    # print('Words list is: {}'.format(words))
    # print('Docs are: {}'.format(documents))
    # print('classes are: {}'.format(classes))
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))

pickle
