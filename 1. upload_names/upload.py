import sys
from db_table import Base, Endpoint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from pathlib import Path, PurePath

ROOT_DIR = Path(__file__).resolve().parent.parent

if len(sys.argv)>1:
    file = sys.argv[1]
    if not Path(file).exists():
        print(f"File {file} does not exist!")
        sys.exit(0)
else:
    file = PurePath(ROOT_DIR, '1. upload_names', 'названия точек.xlsm')

print(file)
# endpoints_file = PurePath(ROOT_DIR, '1. upload_names', 'названия точек.xlsm')
# p2  = PurePath(ROOT_DIR).joinpath('2. create_view_task').joinpath('periods.csv')

try:
    wb = load_workbook(file)
except InvalidFileException as e:
    print("Поддерживаемые форматы: .xlsx,.xlsm,.xltx,.xltm")
    print(e)
    sys.exit(0)

ws = wb.active

session = sessionmaker()()

i = 0
for row in ws.values:
    i += 1
    if i==1: continue
    if row[0] is None: break
    new_endpoint = Endpoint(endpoint_id=row[0], endpoint_name=row[1])
    session.add(new_endpoint)

try:
    session.commit()
except OperationalError as e:
    print(e)
except Exception as e:
    print(e)
