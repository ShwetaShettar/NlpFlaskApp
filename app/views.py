from app import app
from flask import jsonify, request, abort
from models import update_db, search_db


# default endpoint

@app.route('/')
@app.route('/index')
def index():
    return "Plagiarism Detector Running...."


# add document to database :endpoint

@app.route('/add_document', methods=['POST'])
def add_document():
    if not request.json or 'description' not in request.json:
        abort(400)
    data = request.json
    resp = update_db(data)
    return jsonify({'Response': resp}), 201


# check plagiarism  :endpoint

@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    if not request.json or 'description' not in request.json:
        abort(400)
    data = request.json
    result = search_db(data)
    return result


# check plagiarism and add document :endpoint

@app.route('/check_plagiarism/update_db', methods=['POST'])
def check_update():
    if not request.json or 'description' not in request.json:
        abort(400)
    data = request.json
    result = search_db(data)
    update_db(data)
    return result
