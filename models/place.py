#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

var_st = getenv("HBNB_TYPE_STORAGE")

place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
                primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
                primary_key=True, nullable=False)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if var_st == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)

        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)

        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)

        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place')

        amenities = relationship("Amenity", secondary=place_amenity,
                                  back_populates="place_amenities",
                                  viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            objlist = []
            strgx = storage.all(Review)

            for val in strgx.values():
                if val.place_id in self.id:
                    objlist.append(val)
            return objlist

        @property
        def amenities(self):
            """ get am """
            from models import storage
            objlist = []
            strgx = storage.all(Amenity)

            for amenity in strgx.values():

                if amenity.id in self.amenity_ids:
                    objlist.append(amenity)
            return objlist

        @amenities.setter
        def amenities(self, Amenity):
            """ set the am """
            if isinstance(amenity, Amenity):

                self.amenity_ids.append(amenity.id)
