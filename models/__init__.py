#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from os import getenv

v_name = 'HBNB_TYPE_STORAGE'
var_st = os.environ.get(v_name)

if var_st == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
