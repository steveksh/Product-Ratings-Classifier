import re 
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


# function used to clean data
def cleaner(review:str):
    # lower casing the words and removing the puncutations 
    review = re.sub('[^a-zA-Z]+',' ', review.lower())

    # stemming and lemmatization can be considered - performance depends on the usecase and the data nature 
    # https://www.analyticsvidhya.com/blog/2022/06/stemming-vs-lemmatization-in-nlp-must-know-differences/#:~:text=Stemming-,Lemmatization,form%2C%20which%20is%20called%20Lemma.

   # removing the stop words as they contribute no value to the ratings
    stop_words = set(stopwords.words('english'))
    results = [word for word in review.strip().split() if word not in stop_words]
    return " ".join(results)