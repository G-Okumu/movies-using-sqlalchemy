
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer(), primary_key = True)
    name = Column(String(32))
    movies = relationship('Movie', back_populates='director')
    
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key = True)
    title = Column(String(55))
    genre = Column(String())
    director_id = Column(Integer(), ForeignKey('directors.id'))
    
    director = relationship('Director', back_populates='movies')