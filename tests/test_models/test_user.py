#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os

class test_User(test_basemodel):
    """test """

    def __init__(self, *args, **kwargs):
        """testing """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test """
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_last_name(self):
        """test """
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_email(self):
        """test """
        new = self.value()
        self.assertEqual(type(new.email), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """test """
        new = self.value()
        self.assertEqual(type(new.password), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
