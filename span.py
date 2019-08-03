from nltk import sent_tokenize
from nltk.tokenize import string_span_tokenize
sentences = sent_tokenize("This is a sentence. This is another sentence. The sky is blue.")
for sentence in sentences:
    print(list(string_span_tokenize(sentence," ")))