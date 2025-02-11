import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

class TextCleaner:
    """Clean and preprocess text columns"""
    def __init__(self, lang='english'):
        self.stop_words = set(stopwords.words(lang))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        text = str(text).lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens
                 if word not in self.stop_words]
        return ' '.join(tokens)

    def transform(self, X):
        for col in X.select_dtypes(include=['object']).columns:
            X[col] = X[col].apply(self.clean_text)
        return X