from gensim.models import Word2Vec
import gensim
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import nltk
import gensim.downloader as api


dataset = api.load("text8")
model = Word2Vec(dataset)
print(model)
quit()