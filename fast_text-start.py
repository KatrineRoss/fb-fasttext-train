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

model = fasttext.train_supervised('train-comedies-horrors.txt');

model.save_model("comedies-horrors-model.bin")

result = model.predict('девушка заброшенный дом призрак')

print('test');