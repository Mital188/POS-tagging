import re
from collections import Counter

# unique words and their count
word = re.findall('\S+_', open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read())
word = [a.lower() for a in word]
unique_words = Counter(word)
count_word = len(word)
word_dic = {word: float("{0:4f}".format(float(unique_words[word]) / count_word)) for word in unique_words}

# unique word-tag count (Case Sensitive)
wordtag = open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read()
wordtag = wordtag.lower()
unique = Counter(wordtag.split())

# Count of unique tags
tag = re.findall('_\S+', open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read())
tag = [a.lower() for a in tag]
unique_tags = Counter(tag)
count_tag = len(tag)
tag_dic = {word: float("{0:4f}".format(int(unique_tags[word]) / count_tag)) for word in unique_tags}

# probability P(w|t)
p = {}
# accociates the tag number with word count / calcutaltes P(w/t)
for words in unique:
    for tags in unique_tags:
        if (words.endswith(tags)):
            p[words] = float("{0:4f}".format(int(unique[words]) / int(unique_tags[tags])))

count = 0
prob = {}

for wordtag in unique:
    w = re.findall('\S+_', wordtag)
    word = ''.join(w[0])
    word = word[:len(word) - 1]
    t = re.findall('_\S+', wordtag)
    tag = ''.join(t[0])
    tag = tag[1:]
    prob[tag + '|' + word] = float("{0:4f}".format(float(unique[wordtag]) / float(unique_words[w[0]])))

maxi = 0
kk = ""
prob_max = {}
for word in unique_words:
    w = re.findall('\S+_', word)
    wo = ''.join(w[0])
    wo = word[:len(word) - 1]
    maxi = 0
    for k in prob:
        if (k.endswith("|" + wo)):
            if (maxi < float(prob[k])):
                maxi = float(prob[k])
                kk = k
    prob_max[kk] = maxi
wo = ""
corpus2 = open("corpus2.txt",'w')
prob_list = list(prob_max.keys())
wordtag = open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read()
wordtag = wordtag.lower()
wordlist = wordtag.split()
for n,b in enumerate(wordlist):
    w= re.findall('\S+_',b)
    wo = ''.join(w[0])
    wo = wo[:len(wo)-1]
    for a in prob_list:
        if(a.endswith("|"+wo)):
            wordlist[n] = a

for n,a in enumerate(wordlist):
    w = re.findall('\|\S+', a)
    word = ''.join(w[0])
    word = word[1 :len(word)]
    t = re.findall('\S+\|', a)
    tag = ''.join(t[0])
    tag = tag[: len(tag) - 1]
    wordlist[n] = word + '_' + tag



new_corpus = " ".join(wordlist)
corpus2.write(new_corpus)

corpus1 = open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read()
corpus1 = corpus1.lower()
corpus_1 = corpus1.split()
unique = Counter(corpus1.split())

corpus2 = open('corpus2.txt').read()
corpus_2 = corpus2.split()

word = re.findall('\S+_', open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read())
word = [a.lower() for a in word]
unique_words = Counter(word)
words = list(unique_words.keys())

count = 0
eq = 0
error = {}
for w in words:
    error[w] =0

for a,b in zip(corpus_1,corpus_2):
    w= re.findall('\S+_',a)
    wo = ''.join(w[0])
    if(b != a):
        c = int(error[wo])
        c+=1
        error[wo] = c

sorted_error = sorted(error,key = error.__getitem__, reverse = True)
i=0
for er in sorted_error:
    e = er[:len(er)-1]
    i +=1
    if(i ==5):
        break


# change 'that_wdt' to 'that_in'
for prev,word in zip(corpus_1,corpus_1[1:]):
    if(word.startswith("that_")):
        if(prev.endswith("_nn")):
            i = corpus_1.index(word)
            corpus_1[i] = "that_in"


# convert 'have_vb' to 'have_vbp'
for prev,word in zip(corpus_1,corpus_1[1:]):
    if(word.startswith("have_")):
        if(prev.endswith("_md")):
            i = corpus_1.index(word)
            corpus_1[i] = "have_vbp"


# more_rbr to more_jjr
for prev,word in zip(corpus_1,corpus_1[1:]):
    if(word.startswith("more_")):
        if(prev.endswith("_vbd")):
            i = corpus_1.index(word)
            corpus_1[i] = "more_jjr"


# 's_vbz to 's_pos
for prev,word in zip(corpus_1,corpus_1[1:]):
    if(word.startswith("'s_")):
        if(prev.endswith("_prp")):
            i = corpus_1.index(word)
            corpus_1[i] = "'s_pos"

# plans_nns to plans_vbz
for prev,word in zip(corpus_1,corpus_1[1:]):
    if(word.startswith("plans_")):
        if(prev.endswith("_nn")):
            i = corpus_1.index(word)
            corpus_1[i] = "plans_vbz"


corpus3 = open("corpus3.txt",'w')
new_corpus = " ".join(corpus_1)
corpus3.write(new_corpus)

corpus1 = open('HW2_F16_NLP6320_POSTaggedTrainingSet-Windows.txt').read()
corpus1 = corpus1.lower()
corpus_1 = corpus1.split()
unique = Counter(corpus1.split())

corpus3 = open('corpus3.txt').read()
corpus_3 = corpus3.split()

count = 0
eq = 0
error1 = {}
for w in words:
    error1[w] =0

for a,b in zip(corpus_1,corpus_3):
    w= re.findall('\S+_',a)
    wo = ''.join(w[0])
    if(b != a):
        c = int(error1[wo])
        c+=1
        error1[wo] = c
sorted_error1 = sorted(error1,key = error1.__getitem__, reverse = True)
i=0
for er in sorted_error1:
    e = er[:len(er)-1]
    #print(e,"-",error1[er])
    i +=1
    if(i ==5):
        break
i=0
print (repr("Word").ljust(15), repr("Error Rate").ljust(15),repr("New Error Rate").ljust(15))
print ("------------------------------------------------------")
for er in sorted_error:
    e = er[:len(er)-1]
    print (repr(e).ljust(15), repr(error[er]).ljust(15),repr(error1[er]).ljust(15)) # Note trailing comma on previous line
    i+=1
    if(i ==5):
        break
