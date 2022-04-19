
""" Demonstrate
    1. NLP (Natural Language Processing)
    2. Marry doodles.txt with the lexicon
    3. Generate a wordcloud from doodles text

."""

import re
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from collections import Counter
from wordcloud import WordCloud # using python 3.7
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from nltk.stem.lancaster import LancasterStemmer 
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# NEGWORDS = ["not", "no", "none", "neither", "never", "nobody", "n't", 'nor']
# STOPWORDS = ["an", "a", "the"] + NEGWORDS
STOPWORDS = ["an", "a", "the", "or", "and", "thou", "must", "that", "this", "self", "unless", "behind", "for", "which",
             "whose", "can", "else", "some", "will", "so", "from", "to", "by", "within", "of", "upon", "th", "with",
             "it", "doodles","&amp","just","tweet","httpstco","tweet","chance","follow","amp","retweet","httpstcofkugazrt","httpstcojtwvgmqulrt"
             ,"giving","away","random","one","ejust","worth","win","hey","oh","doodle"]


def _remove_stopwords(txt):
    """Delete from txt all words contained in STOPWORDS."""
    words = txt.split()
    # words = txt.split(" ")
    for i, word in enumerate(words):
        if word in STOPWORDS:
            words[i] = " "
    return (" ".join(words))


with open('doodles500kfinal.txt', 'r', encoding='utf-8') as doodles_read:
    # read(n) method will put n characters into a string
    doodles_string = doodles_read.read()

doodles_split = str.split(doodles_string, sep=',')
#print(doodles_split)
#len(doodles_split)

doc_out = []
for k in doodles_split:
    cleantextprep = str(k)
        # Regex cleaning
    expression = "[^a-zA-Z ]"  # keep only letters, numbers and whitespace
    cleantextCAP = re.sub(expression, '', cleantextprep)  # apply regex
    cleantext = cleantextCAP.lower()  # lower case
    cleantext = _remove_stopwords(cleantext)
    bound = ''.join(cleantext)
    doc_out.append(bound)       # a list of sentences

#print(doc_out)
#print(doodles_split)

# print clean text
for line in doc_out:
    print(line)

### Read in BL lexicon
# Negative lexicon
ndct = ''
with open('bl_negative 2.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    for line in infile:
        ndct = ndct + line

# create a list of negative words
ndct = ndct.split('\n')
ndct = [entry for entry in ndct]
len(ndct)

# Positive lexicon
pdct = ''
with open('bl_positive 2.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    for line in infile:
        pdct = pdct + line

pdct = pdct.split('\n')
# pdct = [entry for entry in pdct]
len(pdct)


# Count words being collected in the lexicon


def wordcount(words, dct):
    counting = Counter(words)
    count = []
    for key, value in counting.items():
        if key in dct:
            count.append([key, value])
    return count

def decompose_word(doc):
    txt = []
    for word in doc:
        txt.extend(word.split())
    return txt

# decompose a list of sentences into words by self-defined function
tokenslist = decompose_word(doc_out)
# decompose a list of sentences into words from NLTK module
 tokens = nltk.word_tokenize(doc_out)

# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

tokens=[]
for i in tokenslist:
    tokens.append(lemmatizer.lemmatize(i))
print(tokens)

def lemmatize_all(doc_out):
    wnl = WordNetLemmatizer()
    for word, tag in pos_tag(word_tokenize(doc_out)):
        if tag.startswith('NN'):
            yield wnl.lemmatize(word, pos='n')
        elif tag.startswith('VB'):
            yield wnl.lemmatize(word, pos='v')
        elif tag.startswith('JJ'):
            yield wnl.lemmatize(word, pos='a')
        elif tag.startswith('R'):
            yield wnl.lemmatize(word, pos='r')
        else:
            yield word


# generate wordcloud
comment_words = ' '
for token in tokens:
    comment_words = comment_words + token + ' '

print(comment_words)

with open('data.txt','w') as f:
    f.write(comment_words)

import stylecloud
from IPython.display import Image

stylecloud.gen_stylecloud(file_path='data.txt', collocations=False,
                          size=800,
                          output_name='wordcloud.png')
#
Image(filename='wordcloud.png')
plt.show()


# wordcloud = WordCloud(width = 800, height = 800,
#                 background_color ='white',
#                 min_font_size = 5).generate(comment_words)
#
# plt.figure(figsize=(8, 8), facecolor=None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad=0)
# plt.savefig("wordcloud.png",format='png',dpi=200)
# plt.show()


# Number of words in article
nwords = len(tokens)

nwc = wordcount(tokens, ndct)   # wordcount(text,lexicon)
# [['die', 3], ['famine', 1], ['lies', 2], ['foe', 1], ['cruel', 1], ['gaudy', 1], ['waste', 2], ['pity', 1], ['besiege', 1], ['tattered', 1], ['weed', 1], ['sunken', 1], ['shame', 3], ['excuse', 1], ['cold', 1], ['beguile', 1], ['wrinkles', 1], ['dies', 1], ['abuse', 1], ['deceive', 1], ['hideous', 1], ['sap', 1], ['frost', 1], ['prisoner', 1], ['bereft', 1], ['ragged', 1], ['forbidden', 1], ['death', 1], ['burning', 1], ['weary', 1], ['feeble', 1], ['sadly', 1], ['annoy', 1], ['offend', 1], ['chide', 1], ['wilt', 2], ['fear', 1], ['wail', 1], ['weep', 1], ['deny', 1], ['hate', 2], ['conspire', 1]]

pwc = wordcount(tokens, pdct)
# [['tender', 2], ['bright', 1], ['abundance', 1], ['sweet', 5], ['fresh', 2], ['spring', 1], ['proud', 1], ['worth', 1], ['beauty', 7], ['treasure', 3], ['praise', 2], ['fair', 3], ['proving', 1], ['warm', 1], ['fond', 1], ['lovely', 2], ['golden', 2], ['loveliness', 1], ['free', 1], ['beauteous', 2], ['great', 1], ['gentle', 2], ['work', 1], ['fairly', 1], ['excel', 1], ['leads', 1], ['willing', 1], ['happier', 2], ['gracious', 2], ['homage', 1], ['majesty', 1], ['heavenly', 1], ['strong', 1], ['adore', 1], ['like', 2], ['joy', 2], ['gladly', 1], ['pleasure', 1], ['sweetly', 1], ['happy', 1], ['pleasing', 1], ['well', 1], ['enjoys', 1], ['love', 4], ['beloved', 1]]

# Total number of positive/negative words
ntot, ptot = 0, 0
for i in range(len(nwc)):
    ntot += nwc[i][1]

for i in range(len(pwc)):
    ptot += pwc[i][1]


# Print results
print('Positive words:')
for i in range(len(pwc)):
    print(str(pwc[i][0]) + ': ' + str(pwc[i][1]))
print('Total number of positive words: ' + str(ptot))
print('\n')
print('Percentage of positive words: ' + str(round(ptot / nwords, 4)))
print('\n')
print('Negative words:')
for i in range(len(nwc)):
    print(str(nwc[i][0]) + ': ' + str(nwc[i][1]))
print('Total number of negative words: ' + str(ntot))
print('\n')
print('Percentage of negative words: ' + str(round(ntot / nwords, 4)))



def decompose_word(doc):
    txt = []
    for word in doc:
        txt.extend(word.split())
    return txt

# decompose a list of sentences into words by self-defined function
tokens = decompose_word(doc_out)
# decompose a list of sentences into words from NLTK module
tokens_nltk = nltk.word_tokenize(str(doc_out))  

