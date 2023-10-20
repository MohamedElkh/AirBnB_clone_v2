#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
import os
import shlex

var_st = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if var_st == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """ func cities """
            val = models.storage.all()
            listxx = []
            res = []

            for key in val:
                city = key.replace('.', ' ')
                city = shlex.split(city)

                if (city[0] == 'City'):
                    listxx.append(val[key])
            for el in listxx:
                if (el.state_id == self.id):
                    res.append(el)
            return (res)
