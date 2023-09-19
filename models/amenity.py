#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel
from models.place import place_amenity
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

var_value = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if var_value == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                        back_populates="amenities")
    else:
        name = ""
