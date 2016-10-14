from app import mongo
import datetime
from doc_compare import compare
from flask import jsonify


def update_db(data):
    """
    Returns:Returns Successful if database if populated correctly

    """

    resp = mongo.db.plagiarism.insert({'datetime': datetime.datetime.utcnow(), 'document': data})
    if resp:
        return "Record Updated"
    else:
        return "Update Error"


def search_db(data):
    """
    Returns:Returns result of document compare using cosine similarity score

    """

    user_doc_description = data['description']
    all_items_db = list(mongo.db.plagiarism.find())
    if all_items_db:
        return compare(user_doc_description, all_items_db)
    else:
        return jsonify({"Error":"database empty"})
