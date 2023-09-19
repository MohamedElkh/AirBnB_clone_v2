#!/usr/bin/python3
""" model """
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError, OperationalError
from os import getenv
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.base_model import Base


class DBStorage:
    """An implementation of the Database Storage"""
    __engine = None
    __session = None
    Session = None

    def __init__(self):
        """the class constructor for the database storage implementation"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
                .format(user, pwd, host, database), pool_pre_ping=True)
        if env == 'test':
            metadata = MetaData()
            metadata.drop_all(self.__engine, checkfirst=False)

    def all(self, cls=None):
        """a public instance method that returns a dictionary"""

        if cls is None:
            cls = [State, City, User, Place, Review, Amenity]
            query = []
            for c in cls:
                query.extend(self.__session.query(c).all())
        else:
            query = self.__session.query(cls).all()
        cls_objs = {}
        for obj in query:
            cls_objs[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return cls_objs

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
    def start_session(self):
        """a public instance method used for starting a new session"""
        self.__session = DBStorage.Session()

    def call(self, string):
        """a public instance method used for executing
            sql commands on the class's engine"""
        self.__engine.execute(string)

    def stop_session(self):
        """a public instance method used for ending a session"""
        self.save()
        self.__session.close()

    def reload(self):
        """a public instance method that initializes"""
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
