#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

var_name = 'HBNB_TYPE_STORAGE'
var_value = os.environ.get(variable_name)

if var_value == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
