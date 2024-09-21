from flask import Blueprint, request, jsonify
from ..models import db, VimSyntax

vim_syntax_bp = Blueprint('vim_syntax', __name__)

@vim_syntax_bp.route('/vim', methods=['GET'])
def get_vim_syntax():
    syntaxes = VimSyntax.query.all()
    return jsonify([s.command for s in syntaxes])

@vim_syntax_bp.route('/vim', methods=['POST'])
def add_vim_syntax():
    data = request.get_json()
    new_syntax = VimSyntax(command=data['command'], translation=data['translation'])
    db.session.add(new_syntax)
    db.session.commit()
    return jsonify({"message": "Vim syntax added"}), 201