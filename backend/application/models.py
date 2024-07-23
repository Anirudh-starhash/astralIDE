from .database import db

class User(db.Model):
    __tablename__='user'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_email=db.Column(db.String(128))
    password=db.Column(db.String(128))
    
class Folders(db.Model):
    __tablename__="folders"
    folder_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    folder_name=db.Column(db.String(128))
    no_of_files=db.Column(db.Integer)
    folder_toggle=db.Column(db.Integer)
    parent_folder=db.Column(db.String(128),nullable=True)
    nesting=db.Column(db.Integer,default=0)
    
class File(db.Model):
    __tablename__="file"
    file_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    file_name=db.Column(db.String(128))
    file_extension=db.Column(db.String(128))
    folder_name=db.Column(db.String(128))
    

    
    
    