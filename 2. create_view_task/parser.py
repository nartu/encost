from db_tables import Base, engine
from db_tables import Energy, Operators, Periods, Reasons
from sqlalchemy.orm import sessionmaker
from pathlib import Path, PurePath
import csv

# print(Base.metadata.tables.items())

ROOT_DIR = Path(__file__).resolve().parent.parent

session = sessionmaker()()

# name of tables
tables = ['energy', 'operators', 'periods', 'reasons']

for tn in tables:
    # path to file for parse
    path  = PurePath(ROOT_DIR).joinpath('2. create_view_task').joinpath(tn+'.csv')
    # table model
    t = globals()[tn.capitalize()]
    i = 0
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            print(row)
            new = t(**row)
            session.add(new)
            i += 1
            if i==100:
                session.commit()
                # session.flush()
                i = 0

session.commit()

# print(dir(getattr(session, '_new').values))
# print(vars(session))
