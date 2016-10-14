
# Overview

Document similarity scoring Rest Api written in **flask** using **PyMongo** (python driver) for working with **Mongodb**.

Comparing given test document with documents in the database to produce top 5 most similar documents.

## Similarity Scoring Metric

```
Cosine similarity is calculated between word vectors of test document and respective word vectors of 

all other documents in the database after preprocessing(nltk) and weight normalizing using tf-idf(sklearn python).
```


## Development Environment
Bare Minimun requirements

1. **Python**
2. **Flask**
3. **Mongodb**

Recommended Installs

1. **virtualenv** 


## Getting Started

1.Clone the project:

```
$ git clone https://github.com/aditya-skeptic/NlpFlaskApp.git
$ cd NlpFlaskApp
```

2.Create and initialize virtualenv for the project:

```
$ virtualenv NlpFlaskApp
$ pip install -r requirements.txt
```

## Running the App

```
$ python run.py
```

## Rest Api Endpoints
```
http://localhost:5000/add_document                - to add text document to database 
http://localhost:5000/check_plagiarism            - to check top 5 documents similar to test document passed as json 
http://localhost:5000/check_plagiarism/update_db  - to check top 5 similar documents and then add the given test document
```
## Usage

```
curl -X POST -H "Content-Type: application/json" -d '{ "author": "name", "description":"document to be **indexed** in database" }' http://localhost:5000/add_document

curl -X POST -H "Content-Type: application/json" -d '{ "author": "name", "description":"document to be **searched** for similarity in database" }' http://localhost:5000/check_plagiarism

curl -X POST -H "Content-Type: application/json" -d '{ "author": "name", "description":"document to be searched for similarity and then indexed in database" }' http:/localhost:5000/check_plagiarism/update_db
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/aditya-skeptic) for details on process for submitting pull requests.

## Author

* **Aditya Kumar** -   (https://github.com/aditya-skpetic)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
