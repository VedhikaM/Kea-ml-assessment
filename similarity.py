from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

inputs = [
    "Looking for pricing details",
    "Need help with product features",
    "Interested in demo",
    "Want to know subscription cost",
    "Facing issue with login"
]

def find_best_match(query):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(inputs + [query])
    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_index = similarity.argmax()
    return inputs[best_index]
