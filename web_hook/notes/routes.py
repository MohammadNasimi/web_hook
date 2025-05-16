from flask import Blueprint
from flask import request, jsonify
from .models import Notes
from ..exceptions import resource_bad_request

notes_blueprint = Blueprint('notes', __name__)


# POST - Create a new note
@notes_blueprint.route('/add', methods=['POST'])
def create_notes():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "title is required"}), 400
    if not request.json or "content" not in request.json:
        return jsonify({"error": f"content is required"}), 400
    if not request.json or "tags" not in request.json:
        return jsonify({"error": f"tags[list] is required"}), 400

    note = Notes(title=request.json['title'],
            content=request.json['content'],
            tags=request.json['tags'])
    
    note.create()
    return jsonify({"note_id":note.id}), 201


# GET - Retrieve all resources
@notes_blueprint.route('/list', methods=['GET'])
def get_notes():
    return jsonify(Notes.list())

# GET - Retrieve a single resource
@notes_blueprint.route('/get-note/<string:note_id>', methods=['GET'])
def get_note(note_id):
    note = Notes.get(note_id)
    if note:
        return jsonify(note)
    return jsonify({"error": "note not found"}), 404


# PUT - Replace an entire resource
@notes_blueprint.route('/update/<string:note_id>', methods=['PUT'])
def update_note(note_id):
    if not request.json or "title" not in request.json:
        return jsonify({"error": "title is required"}), 400
    if not request.json or "content" not in request.json:
        return jsonify({"error": f"content is required"}), 400
    if not request.json or "tags" not in request.json:
        return jsonify({"error": f"tags[list] is required"}), 400

    new_note = {"title":request.json['title'],
            "content":request.json['content'],
            "tags":request.json['tags']}
    
    note = Notes.update(note_id, new_note)
    if note:
        return jsonify({"update note_id":note_id}), 201
    return jsonify({"error": "note not found"}), 404

@notes_blueprint.route('/delete/<string:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Notes.delete(note_id)
    if note:
        return jsonify({"delete": note}),204
    return jsonify({"error": "note not found"}), 404

