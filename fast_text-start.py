from gensim.models import FastText, LdaMulticore
import gensim
import re
import pymorphy2
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import fasttext

# Получаем экземпляр анализатора (10-20мб)
morph = pymorphy2.MorphAnalyzer()
corpus_file = datapath('lee_background.cor')

model = fasttext.train_supervised('C:/projects/fastText/test1.txt');

# model.save_model("hc-model.bin")



print('test');