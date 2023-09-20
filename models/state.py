#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os

var_st = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if var_st == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """ func cities """
            from models.__init__ import storage
            from models.city import City

            objlist = []

            strgx = storage.all(City)

            for value in strgx:
                if self.id == value.state_id:
                    objlist.append(value)

            return obj_list
