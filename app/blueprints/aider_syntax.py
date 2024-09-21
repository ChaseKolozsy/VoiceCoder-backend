from flask import Blueprint, request, jsonify
from ..models import db, AiderSyntax

aider_syntax_bp = Blueprint('aider_syntax', __name__)

@aider_syntax_bp.route('/aider', methods=['GET'])
def get_aider_syntax():
    syntaxes = AiderSyntax.query.all()
    return jsonify([s.command for s in syntaxes])

@aider_syntax_bp.route('/aider', methods=['POST'])
def add_aider_syntax():
    data = request.get_json()
    new_syntax = AiderSyntax(command=data['command'], translation=data['translation'])
    db.session.add(new_syntax)
    db.session.commit()
    return jsonify({"message": "Aider syntax added"}), 201