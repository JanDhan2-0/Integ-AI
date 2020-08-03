import numpy as np
import pandas as pd

import re
import os
import gc
import time

import string

from nltk.tokenize import sent_tokenize, word_tokenize 
import nltk
nltk.download('punkt')

import warnings
warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import Word2Vec 

model = Word2Vec.load('find_tags.model')
tags = ['atm','service','security','branch']

def get_top_three(word, model=model):

  l = model.most_similar(word, topn=3)

  words = [x[0] for x in l]

  return words

word_dict = {}

for word in tags:
  word_dict[word] = get_top_three(word)
  word_dict[word].append(word)

def lookup(sent, word_dict=word_dict):

  tags = []

  for k,v in word_dict.items():
    for item in v:
      if item in sent.split(' '):
        tags.append(k)
        break

  return tags