import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Sequence, ARRAY, DateTime, Float, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:666@127.0.0.60/ectest')
Base.metadata.bind = engine
Base.metadata.extend_existing = True


# operators.csv
# {'endpoint_id': '499', 'login_time': '2020-07-25 08:17:40.000000 +03:00', 'logout_time': '2020-07-25 19:32:37.000000 +03:00', 'operator_name': 'Cашин Виктор Евгеньевич'}

class Operators(Base):
    __tablename__ = 'operators'
    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, nullable=False)
    login_time = Column(DateTime(timezone=True), nullable=True)
    logout_time = Column(DateTime(timezone=True), nullable=True)
    operator_name = Column(String(300), nullable=True)

# energy.csv
# {'endpoint_id': '499', 'event_time': '2020-09-01 00:48:00+03', 'kwh': '1.57037'}

class Energy(Base):
    __tablename__ = 'energy'
    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, nullable=False)
    event_time = Column(DateTime(timezone=True), nullable=True)
    kwh = Column(Numeric(8,5), nullable=True)

# periods.csv
# {'endpoint_id': '500', 'mode_start': '2020-09-02 04:41:00+03', 'mode_duration': '58', 'label': 'Работает'}

class Periods(Base):
    __tablename__ = 'periods'
    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, nullable=False)
    mode_start = Column(DateTime(timezone=True), nullable=True)
    mode_duration = Column(Integer, nullable=False)
    label = Column(String(300), nullable=True)

# reasons.csv
# {'endpoint_id': '500', 'event_time': '2020-07-23 18:58:00+03', 'reason': 'Переоснастка'}
class Reasons(Base):
    __tablename__ = 'reasons'
    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, nullable=False)
    event_time = Column(DateTime(timezone=True), nullable=True)
    reason = Column(String(300), nullable=True)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# if not exists
Base.metadata.create_all()


if __name__ == '__main__':
    pass
    # print(Base.metadata.tables)
    # session = sessionmaker()()
    #
    # new_endpoint = Endpoint(endpoint_id=404, endpoint_name="Процесс 4")
    # session.add(new_endpoint)
    # session.commit()
