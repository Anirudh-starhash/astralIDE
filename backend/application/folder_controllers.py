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
    
    main={
        'name':'main',
        'files':[],
        'folders':{}
    }
 
    # this is the initial setup for main with nesting=0
    
    main={
     'id':0,
     'name':'main',
     'parent_folder':None,
     'files': ['abc.cpp','xyz.java','cd.py'],
     'folders':[
            {
                'id':1,
                'name':'new_folder1',
                'parent_folder':'main',
                'files':[],
                'folders' :{}  
            },
        
            {
                'id':2,
                'name':'new_folder2',
                'parent_folder':'main',
                'files':[],
                'folders' :{}  
            },
        
            {
                'id':3,
                'name':'new_folder3',
                'parent_folder':'main',
                'files':[],
                'folders' :{}  
            }
        ]
    }
    
    # this is after creating three folders in it nesting=1 and 1,2,3 are respective id of folders main=0
       
    # here main is m-way tree 
    
    # in terms of c++ whats our folder structure named as
    
    # map<string,variable_dataType> // variable_dataType can be a vector , map,int,string, char
    
    # class Node{
    #     string name;
    #     string parent_folder;
    #     vector<string> files;
    #     vector<Node*> folders; 
    # }
    
    
        
    
    
    