#!/usr/bin/python
# Author: Scott Iwako
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
                'name': self.name,
                'id': self.id,
                'email': self.email,
                'picture': self.picture
                }


class Origin(Base):

    __tablename__ = 'origin'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'user_id': self.user_id
                }


class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    origin_id = Column(Integer, ForeignKey('origin.id'))
    origin = relationship(Origin)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'origin_id': self.origin_id,
                'description': self.description,
                'user_id': self.user_id
                }


engine = create_engine('sqlite:///coffeewithusers.db')
Base.metadata.create_all(engine)
