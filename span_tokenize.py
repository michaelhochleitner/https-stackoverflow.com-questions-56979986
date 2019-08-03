from nltk.tokenize import WhitespaceTokenizer as wt
from nltk import sent_tokenize
sentences = sent_tokenize("This is a sentence. This is another sentence. The sky is blue.")
print(sentences)
print(list(wt().span_tokenize_sents(sentences)))