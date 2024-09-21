from flask import Blueprint, request, jsonify
from ..models import db, PythonSyntax

python_syntax_bp = Blueprint('python_syntax', __name__)

@python_syntax_bp.route('/python', methods=['GET'])
def get_python_syntax():
    syntaxes = PythonSyntax.query.all()
    return jsonify([s.command for s in syntaxes])

@python_syntax_bp.route('/python', methods=['POST'])
def add_python_syntax():
    data = request.get_json()
    new_syntax = PythonSyntax(command=data['command'], translation=data['translation'])
    db.session.add(new_syntax)
    db.session.commit()
    return jsonify({"message": "Python syntax added"}), 201