#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone with a databasae"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import metadata


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
