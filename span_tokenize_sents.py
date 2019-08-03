from nltk.tokenize import WhitespaceTokenizer
from nltk import sent_tokenize
sentences = sent_tokenize("This is a sentence. This is another sentence. The sky is blue.")
for sentence in sentences:
    print(list(WhitespaceTokenizer().span_tokenize(sentence)))