import sys
from db_table import Base, Endpoint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from pathlib import Path, PurePath
from urllib.parse import unquote

ROOT_DIR = Path(__file__).resolve().parent.parent


if len(sys.argv)>1:
    raw_file_name = sys.argv[1]
    raw_file_name = raw_file_name[7:] if raw_file_name[:7] == 'file://' else raw_file_name
    file_name = unquote(raw_file_name)
    if not Path(file_name).exists():
        print(f"File {filefile_name} does not exist!")
        sys.exit(0)
else:
    print("Mast be argument: fullpath of file .xlsx,.xlsm,.xltx,.xltm")
    # file = PurePath(ROOT_DIR, '1. upload_names', 'названия точек.xlsm')
    sys.exit(0)

try:
    wb = load_workbook(file_name)
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
