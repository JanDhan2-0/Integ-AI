import tags2
import helpers2

import pickle

import pandas as pd

df = pd.read_csv('reviews.csv')

from tensorflow.keras.preprocessing.sequence import pad_sequences

model = helpers2.open_model_from_json(filename='model/model.json', weights='model/best_acc_bank_weights.hdf5')
model.compile(loss = 'binary_crossentropy',
              metrics=['accuracy'],
              optimizer='adam')
tokenizer = pickle.load(open('model/tokenizer.pickle','rb'))

def get_sentiment_and_tag(review):

	review = helpers2.normalize(review)
	feature_vec = tokenizer.texts_to_sequences([review])

	maxlen = 30

	feature_vec = pad_sequences(feature_vec, maxlen=maxlen)

	predictions = model.predict(feature_vec)[0]

	classes = ['negative','positive']

	pred = 0 if predictions <0.5 else 1
	# certainty = 1-predictions[0] if pred == 0 else predictions[0]

	caught = tags2.lookup(review)

	return [classes[pred], caught]

# print(get_sentiment_and_tag('This atm is trash, bad security overall'))

df['Sentiment'] = df['Sentence'].apply(lambda x : get_sentiment_and_tag(x)[0])
df['Tags'] = df['Sentence'].apply(lambda x : get_sentiment_and_tag(x)[1])

df.to_csv('tagged_reviews.csv', index=False)