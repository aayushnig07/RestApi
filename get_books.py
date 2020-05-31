import flask
from flask import jsonify,request,abort,make_response
import json

app=flask.Flask(__name__)
app.config["DEBUG"]=True

def load_books():
    f=open('books.json')
    books_data=json.load(f)
    return books_data

@app.route('/api/v1/resource/books/all', methods=['GET'])
def get_all_books():
    return jsonify(load_books())

@app.route('/api/v1/resource/books', methods=['GET'])
def get_book_by_id():
    try:
        if 'id' in request.args:
            id = int(request.args['id'])
            if id is not None:
                books = load_books()
            else:
                abort(400)
    
        result=[]
        for book in books:
            if(book['id']==id):
                result.append(book)
    
        if(len(result)==0):
            abort(404)
    except Exception as e:
        abort(400)

   
        
    return jsonify(result)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)

@app.errorhandler(400)
def bad_syntax(error):
    return make_response(jsonify({'error':'Bad Syntax'}),400)

app.run()
