#%%
import pandas as pd
import numpy as np
import nltk
import numpy as np
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC  #importing machine learning classification algorithm
import random
import pickle


# %%
df = pd.read_csv("corna.csv")

# %%
y  = df['class']
x = df['question']
# %%
lemmer = nltk.stem.WordNetLemmatizer()

# %%
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

# %%
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# %%
def Normalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    


#%%
vectorizer = TfidfVectorizer(tokenizer=Normalize,stop_words = 'english')
X = vectorizer.fit_transform(x) 



# %%
clf  = LinearSVC(max_iter=800, C=0.1)

# %%
clf.fit(X,y)

# %%
text_test = ["how are you"] 

# %%
X_test = vectorizer.transform(text_test) 

# %%
print(clf.predict(X_test))

# %%
pickle.dump(clf,open("chat.pkl", 'wb'))

# %%
pickle.dump(vectorizer,open("vect.pkl","wb"))



# %%
