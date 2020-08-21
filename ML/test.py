#%%
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split


# %%
df = pd.read_csv("c.csv")

# %%
train,test = train_test_split(df,
                        stratify = df['Infected with Covid19'],
                        test_size = 0.1,
                        random_state = 20,
                    )
y_train = train['Infected with Covid19']
x_train = train.drop('Infected with Covid19',axis =1)


# %%
clf = svm.SVC()

# %%
clf.fit(x_train,y_train)

# %%
clf.score(x_train,y_train)

# %%
clf.score(test.drop('Infected with Covid19',axis=1),test['Infected with Covid19'])

# %%
import pickle
pickle.dump(clf,open("test.pkl","wb"))

# %%
clf.predict([[20,20,20,20]])[0]

# %%
