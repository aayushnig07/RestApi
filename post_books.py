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
            result = {'author': author, 'first_sentence': first_sentence,
                      'published': year_published, 'title': title}
            print(result)
        except Exception:
            abort(400)
        return jsonify(result)

app.run()
