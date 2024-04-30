#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


new_state = State()
new_state.name = "California"
print("-- new_state --")
print(new_state)
print("--------------------------------")
print("-- new_state.to_dict() --")
print(new_state.to_dict())
print("--------------------------------")
print("-- storage.all() --")
print(storage.all())
