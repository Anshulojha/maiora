from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    type = Column(String)
    joke = Column(String)
    setup = Column(String, nullable=True)
    delivery = Column(String, nullable=True)
    nsfw = Column(Boolean)
    political = Column(Boolean)
    sexist = Column(Boolean)
    safe = Column(Boolean)
    lang = Column(String)
