from flask import Flask, url_for, request, jsonify, render_template

import numpy as np 
import os

import warnings
warnings.simplefilter('ignore')

import re
import string

import helpers
import tags
import pickle

from tensorflow.keras.preprocessing.sequence import pad_sequences

#load model, weights, tokenizers

model = helpers.open_model_from_json(filename='model.json', weights='best_acc_bank_weights.hdf5')
model.compile(loss = 'binary_crossentropy',
              metrics=['accuracy'],
              optimizer='adam')
tokenizer = pickle.load(open('tokenizer.pickle','rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello World'


@app.route('/sentiment_score', methods=['POST', "GET"])
def sentiment_score(tokenizer = tokenizer, model = model, maxlen=30):

	review = request.args['review'] #read reviews from html

	review = helpers.normalize(review)
	feature_vec = tokenizer.texts_to_sequences([review])

	feature_vec = pad_sequences(feature_vec, maxlen=maxlen)

	predictions = model.predict(feature_vec)[0]

	classes = ['negative','positive']

	pred = 0 if predictions <0.5 else 1

	caught = tags.lookup(review) #get tags of a particular sentence

	response = {
		"sentiment":classes[pred],
		"tags":caught
	}
	return response

if __name__ == '__main__':
	port = int(os.environ.get("PORT"))
	app.run(host='0.0.0.0',port=port)
