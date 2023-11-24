#!/usr/bin/python3
"""This module defines a class to manage \
file storage for hbnb clone with a databasae"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import metadata, sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self) -> None:
        self.mysql_user = getenv('HBNB_MYSQL_USER')
        self.mysql_password = getenv('HBNB_MYSQL_PWD')
        self.mysql_host = getenv('HBNB_MYSQL_HOST')
        self.mysql_database = getenv('HBNB_MYSQL_DB')
        cone_str = "mysql+mysqldb://{}:{}@{}/{}".format(
            self.mysql_user,
            self.mysql_password,
            self.mysql_host,
            self.mysql_database
        )
        self.__engine = create_engine(cone_str, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retun instances of a given class or all classes"""
        obj_dict = {}
        self.__session = sessionmaker(bind=self.__engine)()
        if cls is not None:
            sess_objs = self.__session.query(cls).all()
            for obj in sess_objs:
                obj_dict['{}.{}'.format(
                    obj.__class__.__name__,
                    obj.id
                )] = obj
            return obj_dict
        else:
            sess_objs = self.__session.query(cls).all()
            for obj in sess_objs:
                if obj.__class__.__name__ != 'BaseModel':
                    obj_dict['{}.{}'.format(
                        obj.__class__.__name__,
                        obj.id
                    )] = obj
            return obj_dict
