#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", passive_deletes=True, backref="cities")
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """city getter"""
            new_list = []
            for value in models.storage.all().values():
                try:
                    if self.id == value.state_id:
                        new_list.append(value)
                except AttributeError:
                    pass

            return new_list

    def __init__(self, *args, **kwargs):
        """State constructor"""
        super().__init__(*args, **kwargs)
