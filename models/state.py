#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


var_st = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if var_st == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            objlist = []
            strgx = storage.all(City)

            for cty in strgx.values():
                if cty.state_id == self.id:
                    objlist.append(cty)
            return objlist
