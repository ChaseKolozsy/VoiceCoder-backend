from flask import Blueprint, request, jsonify
from ..models import db, PdbSyntax

pdb_syntax_bp = Blueprint('pdb_syntax', __name__)

@pdb_syntax_bp.route('/pdb', methods=['GET'])
def get_pdb_syntax():
    syntaxes = PdbSyntax.query.all()
    return jsonify([s.command for s in syntaxes])

@pdb_syntax_bp.route('/pdb', methods=['POST'])
def add_pdb_syntax():
    data = request.get_json()
    new_syntax = PdbSyntax(command=data['command'], translation=data['translation'])
    db.session.add(new_syntax)
    db.session.commit()
    return jsonify({"message": "PDB syntax added"}), 201