#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


var_st = getenv('HBNB_TYPE_STORAGE')

if var_st == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()

storage.reload()
