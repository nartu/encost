import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Sequence, ARRAY, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:666@127.0.0.60/ectest')
Base.metadata.bind = engine

### Структура БД:
# endpoint_id int
# endpoint_name varchar
#
class Endpoint(Base):
    __tablename__ = 'endpoints'
    endpoint_id = Column(Integer, primary_key=True, nullable=False)
    endpoint_name = Column(String(255), nullable=True)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# if not exists
Base.metadata.create_all()

if __name__ == '__main__':
    session = sessionmaker()()

    new_endpoint = Endpoint(endpoint_id=404, endpoint_name="Процесс 4")
    session.add(new_endpoint)
    session.commit()
