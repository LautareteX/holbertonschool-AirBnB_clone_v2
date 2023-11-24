#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade='all, delete-orphan')

    @property
    def cities(self):
        from models import storage
        c_instances = storage.all("City").values()
        m_cities = []
        for i in c_instances:
            if i.state_id == self.id:
                m_cities.append(i)
        return m_cities
