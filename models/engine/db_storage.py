""" DB Storage Module, Handles SQLAlchemy storage"""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import os
from dotenv import load_dotenv

load_dotenv()

class DBStorage():
    """ DBStorage Class"""
    __engine = None
    __session = None
    __models = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

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
        """ Queries on the current db session depending on cls name"""
        result = {}
        session = self.__session

        if not cls:
            classes_to_query = self.__models.values()
        else:
            if isinstance(cls, str):
                cls = self.__models.get(cls)
                classes_to_query = [cls] if cls else []

        for model in classes_to_query:
            instances = session.query(model).all()

            for instance in instances:
                key = f"{type(instance).__name__}.{instance.id}"
                result[key] = instance            

        return result

    def new(self, obj):
        """ Adds the object to the current db session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit all xhanges of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from hte current db session if obj not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the db
            Creates the current db session from the engine
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Closes Session"""
        self.__session.close()

