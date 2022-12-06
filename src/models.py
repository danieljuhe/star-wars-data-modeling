import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), primary_key=True, nullable=False)
    race = Column(String(100), ForeignKey('planet.race'), nullable=False)
    birth_year = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    eye_color = Column(String(50), nullable=True)
    hair_color = Column(String(50), nullable=True)
    gender = Column(String(100), nullable=True)
    homeworld_name = Column(String(250), ForeignKey('planet.name'), nullable=False)
    starship = Column(String(250), ForeignKey('starship.name'), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('people.homeworld_name'), nullable=False)
    race = Column(String(250), ForeignKey('people.race'), nullable=False)
    diameter = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    gravity = Column(String(100), nullable=True)
    climate = Column(String(100), nullable=True)
    terrain = Column(String(100), nullable=True)


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), ForeignKey('people.starship'), nullable=False)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    crew = Column(String(100), nullable=True)
    max_passengers = Column(Integer, nullable=True)
    max_cargo = Column(Integer, nullable=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
