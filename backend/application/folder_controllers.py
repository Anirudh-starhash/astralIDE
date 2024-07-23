from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import Folders,File
from application.database import db
import os
import subprocess

folder_blueprint=Blueprint("folder",__name__)

@folder_blueprint.route("/add_folder",methods=['GET','POST'])
def add_folder():
    data=request.get_json()
    folder_name=data.get("folder_name")
    no_of_files=data.get("no_of_files")
    parent_folder=data.get("parent_folder")
    
    f=db.session.execute(db.Select(Folders).where(Folders.folder_name==folder_name)).scalar()
    
    if f==None:
        new_folder=Folders(folder_name=folder_name,no_of_files=no_of_files,folder_toggle=0,parent_folder=parent_folder)
        db.session.add(new_folder)
        db.session.commit()
        
        return jsonify({
            'msg':'added'
        }),200
    
    else:
        return jsonify({
            'msg':'Some Error!'
        }),201
        
        
@folder_blueprint.route("/getFolders",methods=['GET','POST'])
def getFolders():
    
    f=db.session.execute(db.Select(Folders)).scalars().all()
    
    
    if f==None:
        return jsonify({
            'msg':'Some Error'
        }),201
     
    folders=[]
    
    for folder in f:
        folders.append({
            'folder_name':folder.folder_name,
            'no_of_files':folder.no_of_files,
            'folder_id':folder.folder_id,
            'folder_toggle':folder.folder_toggle
        })
        
    if folders==[]:
        return jsonify({
            'id':0
        }),200
        
    
    return jsonify({
        'folder':folders,
        'id':1
    }),200
    
folder_blueprint.route("/toggle_and_getInfo",methods=['GET','POST'])
def getInfo():
    data=request.get_json()
    folder_name=data.get("folder_name")
    folder_id=data.get("folder_id")
    
    f=db.session.execute(db.Select(Folders).where(Folders.folder_id==folder_id)).scalar()
    f.folder_toggle=1
    db.session.commit()
    n=f.nesting
    
    setup={}
    parent_folder=folder_name
    setup["files"]={}
    setup["folders"]={}
    while n!=0:
        
        folder_content=db.session.execute(db.Select(Folders).where(Folders.parent_folder==parent_folder)).scalars().all()
        # we get all folders inside the required folder
        file_content=db.session.execute(db.Select(File).where(File.folder_name==folder_name)).scalars().all()
        
       
        
        #n=2 
        {
            'name':'main',
            'files':{
                '1':'abc.cpp',
                '3':'xyz.java',
                '7':'cd.py'
            },
            'folders':{
                
                {
                     'name':'new_folder4',
                     'files':{},
                     'folders':{}
                }
            }
        }
        
        
        {
            'name':'main',
            'files':{},
            'folders':{
                {
                    'name':'new_folder1',
                    'files':{},
                    'folders':{}
                },
                {
                    'name':'new_folder2',
                    'files':{},
                    'folders':{}
                },
                {
                    'name':'new_folder3',
                    'files':{},
                    'folders':{}
                },
                
            }
        }
        
        # this is the outlayout of our original main folder
        
        {
            'name':'main',
            'file':{},
            'folders':{}
        }
        # this was it initial 
        # goes on till the end nesting a big json api
        
        
    
    
    