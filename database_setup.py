#!/usr/bin/python
# Author: Scott Iwako
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Origin(Base):

    __tablename__ = 'origin'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('origin.id'))
    origin = relationship(Origin)

engine = create_engine('sqlite:///coffee.db')
Base.metadata.create_all(engine)
