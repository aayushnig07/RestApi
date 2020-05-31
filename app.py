import flask
from flask import jsonify, request, abort, make_response
import json
import db_operations

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resource/books', methods=['POST'])
def post_books():
    if not request.json:
        abort(400)
    else:
        try:
            author = request.json['author']
            first_sentence = request.json['first_sentence']
            year_published = request.json['published']
            title = request.json['title']

            db_operations.insertRecord(
                author, first_sentence, title, year_published)
            
            
        except Exception:
            abort(400)
        return jsonify()


@app.route('/api/v1/resource/books/all', methods=['GET'])
def get_all_books():
    return jsonify(db_operations.showAllData())

@app.route('/api/v1/resource/books', methods=['GET'])
def get_book_by_id():
    try:
        if 'id' in request.args:
            id = int(request.args['id'])
            if id is not None:
                books = db_operations.showOneData(id)
            else:
                abort(400)
    
        result=[]
        for book in books:
            if(book['id']==id):
                result.append(book)
    
        if(len(result)==0):
            abort(404)
    except Exception as e:
        print(str(e))
        abort(400)

   
        
    return jsonify(result)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)

@app.errorhandler(400)
def bad_syntax(error):
    return make_response(jsonify({'error':'Bad Syntax'}),400)

app.run()