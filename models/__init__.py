#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

var_st = getenv('HBNB_TYPE_STORAGE')

if var_st == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
