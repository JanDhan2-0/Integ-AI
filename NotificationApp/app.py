from flask import Flask, url_for, request, jsonify, render_template

import push_notifs

from nltk.tokenize import sent_tokenize

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/notification', methods=['GET','POST'])
def notification():

	reviews = request.form['text']

	reviews = sent_tokenize(reviews)

	positives = push_notifs.get_promotions(reviews)

	return jsonify(positives)

if __name__ == "__main__":

	app.run(threaded=False)