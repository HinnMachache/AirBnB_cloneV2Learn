""" DB Storage Module, Handles SQLAlchemy storage"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session

import os
from dotenv import load_dotenv

load_dotenv()

class DBStorage():
    """ DBStorage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """ Database Constructor"""

        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        port = os.getenv('HBNB_MYSQL_PORT')
        sqlEnv = os.getenv('HBNB_ENV')

        # Create DB connection
        self.__engine = create_engine(
            f'mysql+mysqlbd://{username}:{password}@{host}:{port}/{db_name}',
            pool_pre_ping=True)
        
        if sqlEnv == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    
    def all(self, cls=None):
        pass

    def new(self, obj):
        """ Adds the object to the current db session"""
        pass

    def save(self):
        """ Commit all xhanges of the current db session"""
        pass

    def delete(self, obj=None):
        """ Delete from hte current db session if obj not None"""
        pass

    def reload(self):
        """ Creates all tables in the db
            Creates the current db session from the engine"""

