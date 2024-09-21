from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PythonSyntax(db.Model):
    __tablename__ = 'python_syntax'
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(255), unique=True, nullable=False)
    translation = db.Column(db.Text, nullable=False)

class VimSyntax(db.Model):
    __tablename__ = 'vim_syntax'
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(255), unique=True, nullable=False)
    translation = db.Column(db.Text, nullable=False)

class PdbSyntax(db.Model):
    __tablename__ = 'pdb_syntax'
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(255), unique=True, nullable=False)
    translation = db.Column(db.Text, nullable=False)

class AiderSyntax(db.Model):
    __tablename__ = 'aider_syntax'
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(255), unique=True, nullable=False)
    translation = db.Column(db.Text, nullable=False)