
import pickle
import nltk
import string



class cb:
    def response(self,user_response,clf,vect):
        text_test = [user_response]
        X_test = vect.transform(text_test)
        prediction = clf.predict(X_test)
        return prediction[0]

