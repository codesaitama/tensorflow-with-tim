import tensorflow as tf
from tensorflow import keras
import numpy as np
from pathlib import Path

data = keras.datasets.imdb

# save np.load
np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)

np.load = np_load_old

print(train_data[0])

word_index = data.get_word_index()

word_index = {k:(v+3) for k, v in word_index.items()}

word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=250)

test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=250)

print("File Path:", Path(__file__).absolute())
print("Directory Path:", Path().absolute()) 

def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])

def review_encode(s):
    encoded = [1]
    for word in s:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)
    return encoded

model = keras.models.load_model("model.h5")

with open(str(Path().absolute()) + '/codes/data/test_review.txt') as f:
    for line in f.readlines():
        nline = line.replace(',', '').replace('(', '').replace(')', '').replace(':', '').strip()
        encode = review_encode(nline)
        encode = keras.preprocessing.sequence.pad_sequences([encode], value=word_index["<PAD>"], padding="post", maxlen=250)
        predict = model.predict(encode)
        print(line)
        print(encode)
        print(predict[0])



 
