#!/usr/bin/python3
"""test """
import os
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """class amenity """

    def __init__(self, *args, **kwargs):
        """init the class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name tp"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))
