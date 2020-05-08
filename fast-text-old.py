only_nouns = False

model_file_name = 'C:/projects/TextStageProcessor/output_files/FastText/voyna-i-mir-tom-1_output.model'
text_file_name = 'C:/projects/TextStageProcessor/input_files/FastText/voyna-i-mir-tom-1.txt'
russian_stop_words = 'C:/projects/TextStageProcessor/sources/russian_stop_words.txt'

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
            if word not in stopwords:
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

    with open(russian_stop_words, 'r', encoding='UTF-8') as file:
        stopwords = set(map(str.strip, file.readlines()))

    lines = normalize_text(lines)
    apply_filter(gensim_preprocess, lines)
    apply_filter(remove_stops, lines)
    apply_filter(morph_nouns if only_nouns else morph_words, lines)
    apply_filter(remove_stops, lines)
    return [line for line in map(list, lines) if len(line) > 1]


text = _load_file_data(text_file_name)

model = FastText.load(model_file_name)
FastText.bo

lda_model = LdaMulticore(corpus=text, id2word=model.wv.vocab)
                        # (corpus=text_file_name,
                        #  id2word=model.wv.vocab,
                        #  random_state=100,
                        #  num_topics=7,
                        #  passes=10,
                        #  chunksize=1000,
                        #  batch=False,
                        #  alpha='asymmetric',
                        #  decay=0.5,
                        #  offset=64,
                        #  eta=None,
                        #  eval_every=0,
                        #  iterations=100,
                        #  gamma_threshold=0.001)

dictionary = model.wv.vocab
