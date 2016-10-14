from flask import jsonify
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer


def stem_tokens(tokens):
    """
    Returns:Returns base form of tokenized words

    """

    return [stemmer.stem(item) for item in tokens]


def normalization(text):
    """
    Returns:Returns processed tokenized words

    """

    return stem_tokens(nltk.word_tokenize(text.lower().translate(delete_all_punctuation)))


def cosine_similarity(text_1, text_2):
    """
    Returns:Returns cosine similarity using term frequency inverse document frequency

    """

    tfidf = vectorizer.fit_transform([text_1, text_2])
    return ((tfidf * tfidf.T).A)[0, 1]


stemmer = nltk.stem.porter.PorterStemmer()
delete_all_punctuation = dict((ord(character), None) for character in string.punctuation)
vectorizer = TfidfVectorizer(tokenizer=normalization, stop_words='english')


def compare(user_doc_description, list_all_items):
    """
    Returns: Return cosine similarity of given doc with all docs in database as a json ar

    """

    doc_description_keys = []
    score_value = []
    for item in list_all_items:
        description = item['document']['description']
        doc_description_keys.append(description)
        score_value.append("%.4f" % cosine_similarity(user_doc_description, description))

    sim_dict_rating = (zip(doc_description_keys, score_value))
    sim_dict_rating.sort(reverse=True, key=lambda x: x[1])
    return jsonify({"Similarity Rating with ": sim_dict_rating[:5]})
