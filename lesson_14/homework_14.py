"Завдання 1: Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv"

import csv
from pathlib import Path


INPUT_DIR = Path(r"C:\Users\oleksii.yevplov\qa-automation-pyton\lesson_14\work_with_cvs")
OUTPUT_DIR = Path(r"C:\Users\oleksii.yevplov\qa-automation-pyton\lesson_14")

file_1 = INPUT_DIR / "rmc.csv"
file_2 = INPUT_DIR / "r-m-c.csv"
result_file = OUTPUT_DIR / "result_yevplov.csv"



def read_csv_auto(file):
   
    with open(file, encoding="utf-8") as f:
        first_line = f.readline()
    delimiter = ";" if ";" in first_line else ","
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        return list(reader)


def remove_duplicates_from_two_csv(file1, file2, result):
    data1 = read_csv_auto(file1)
    data2 = read_csv_auto(file2)

    
    header = data1[0] if data1 else []
    rows1 = data1[1:] if len(data1) > 1 else []
    rows2 = data2[1:] if len(data2) > 1 else []

 
    combined_rows = rows1 + rows2
    unique_rows = list(dict.fromkeys(tuple(row) for row in combined_rows))

  
    with open(result, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(unique_rows)


remove_duplicates_from_two_csv(file_1, file_2, result_file)

print("✅ Готово! Створено файл:", result_file)


"Завдання 2:Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log"

import json
import logging
from pathlib import Path


INPUT_DIR = Path(r"C:\Users\oleksii.yevplov\qa-automation-pyton\lesson_14\work_with_json")
OUTPUT_DIR = Path(r"C:\Users\oleksii.yevplov\qa-automation-pyton\lesson_14")


log_file = OUTPUT_DIR / "json__yevplov.log"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


for file_path in INPUT_DIR.iterdir():
    if file_path.is_file() and file_path.suffix == ".json":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)  
        except json.JSONDecodeError as e:
            logging.error(f"Невалідний JSON у файлі {file_path.name}: {e}")
        except Exception as e:
            logging.error(f"Помилка при обробці файлу {file_path.name}: {e}")

print(f"✅ Перевірка завершена. Лог у файлі: {log_file}")

"Завдання 3:Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо"

import logging
from pathlib import Path
import xml.etree.ElementTree as ET


XML_FILE = Path(r"C:\Users\oleksii.yevplov\qa-automation-pyton\lesson_14\ideas_for_testwork_with_xml\groups.xml")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def find_incoming_by_group_number(file_path, group_number):
   
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and number.text == str(group_number):
                timing = group.find("timingExbytes")
                if timing is not None:
                    incoming = timing.find("incoming")
                    if incoming is not None:
                        return incoming.text
        return None
    except ET.ParseError as e:
        logging.error(f"Помилка парсингу XML: {e}")
        return None


group_number_to_find = 2 
incoming_value = find_incoming_by_group_number(XML_FILE, group_number_to_find)

if incoming_value is not None:
    logging.info(f"Incoming для group {group_number_to_find}: {incoming_value}")
else:
    logging.info ( f"Group {group_number_to_find} не знайдено або немає incoming")
