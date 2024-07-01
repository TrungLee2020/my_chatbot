from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

class Chatbot:
    def __init__(self):
        self.documents = []
        self.anwsers = []
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matric = None
    
    def load_data(self, filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
            self.documents = [item['question'] for item in data]
            self.anwsers = [item['answer'] for item in data]
        self.tfidf_matric = self.vectorizer.fit_transform(self.documents)
        
    def get_response(self, query):
        query_tfidf = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_tfidf, self.tfidf_matric)
        closest = similarities.argmax()
        return self.anwsers[closest]