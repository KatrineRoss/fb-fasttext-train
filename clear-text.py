import nltk
import gensim
import re
import pymorphy2
from nltk.corpus import stopwords

nltk.download('stopwords')

morph = pymorphy2.MorphAnalyzer()
cachedStopWords = stopwords.words("russian")
lines = []
only_nouns = True

def _load_file_data(input_file: str):
        with open(input_file, 'r', encoding='UTF-8') as file:
            lines = _process(file.readlines())
        return lines

def _process(lines):
    def apply_filter(filter, lines):
        for i in range(len(lines)):
            lines[i] = filter(lines[i])

    def gensim_preprocess(line):
        return gensim.utils.simple_preprocess(line, min_len=3, max_len=20)

    def normalize_text(lines):
        lst = []
        pattern = re.compile(r'[?!.]+')
        for line in filter(lambda x: len(x) > 0, map(str.strip, lines)):
            try:
                lst.extend(re.split(pattern, line))
            except Exception as e:
                print(line)
                print(e)
        lines = lst
        return lines

    def remove_stops(line):
        for word in line:
            if word.lower() not in cachedStopWords:
                yield word

    def morph_words(line):
        for word in line:
            if morph.word_is_known(word):
                word = morph.parse(word)[0].normal_form
            yield word

    def morph_nouns(line):
        for word in line:
            if morph.word_is_known(word):
                data = morph.parse(word)[0]
                if 'NOUN' in data.tag:
                    yield data.normal_form

    lines = normalize_text(lines)
    apply_filter(gensim_preprocess, lines)
    apply_filter(remove_stops, lines)
    apply_filter(morph_nouns if only_nouns else morph_words, lines)
    apply_filter(remove_stops, lines)
    return [line for line in map(list, lines) if len(line) > 1]

genres = ['comedies', 'fantasy', 'adventure', 'action', 'melodrama', 'horrors']

text = _load_file_data('initial/horrors.txt')
newFile = open('clean/clean-horrors.txt', "a", encoding='utf-8')

for i in range(len(text)):
    newFile.write(' '.join(text[i]) + '\n')

print('test')
