#!/usr/bin/python3
""" model """
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError, OperationalError
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
import os

user = os.environ.get("HBNB_MYSQL_USER")
pwd = os.environ.get("HBNB_MYSQL_PWD")
host = os.environ.get("HBNB_MYSQL_HOST")
database = os.environ.get("HBNB_MYSQL_DB")
env = os.environ.get("HBNB_ENV")


class DBStorage:
    """An implementation of the Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """the class constructor for the database storage implementation"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, database),
                                       pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine, checkfirst=False)

    def all(self, cls=None):
        """a public instance method that returns a dictionary"""
        classes = [User, Place, State, City, Amenity, Review]
        res = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                keyn = ClassName + "." + obj.id
                res[keyn] = obj
        else:
            for cl in classes:
                for obj in self.__session.query(cl).all():
                    ClassName = obj.__class__.__name__
                    keyn = ClassName + "." + obj.id
                    res[keyn] = obj
        return res

    def new(self, obj):
        """a public instance method that adds"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """a public instance method that persists the actions"""
        self.__session.commit()

    def delete(self, obj=None):
        """a public instance method that deletes a created instance"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """a public instance method that initializes"""

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """func to call remove"""
        self.__session.close()
