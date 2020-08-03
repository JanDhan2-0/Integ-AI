import numpy as np
import pandas as pd

import os
import time
import re

import nltk

# try:
# 	nltk.data.find('tokenizers/punkt.zip')
# except:
# 	nltk.download('punkt')

import gc
import string

def normalize(data):

  data = data.lower()
  data = data.strip(string.punctuation)

  return data

def save_model_to_json(model, filename):

  model_json = model.to_json()
  with open(filename, 'w') as json_file :
    json_file.write(model_json)

  print('Model saved in json format in {}'.format(filename))


def open_model_from_json(filename, weights):

  from tensorflow.keras.models import model_from_json

  json_file = open(filename, 'r')
  loaded_model_json = json_file.read()
  json_file.close()

  loaded_model = model_from_json(loaded_model_json)
  loaded_model.load_weights(weights)
  print('Model loaded successfully')

  return loaded_model