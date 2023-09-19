#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

var_st = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if var_st == 'db':
        name = Column(String(128), nullable=False)

        place_amenities = relationship("Place", secondary=place_amenity,
                                        back_populates="amenities")
    else:
        name = ""
