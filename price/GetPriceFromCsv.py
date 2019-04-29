import csv
from itertools import islice
from obj.MfiObj import *


def filter_begin_end_date(mfi_obj_array, begin_date, end_date):
    filtered_mfi_objs = []
    for mfi_obj in mfi_obj_array:
        if mfi_obj.get_charge_date() < begin_date:
            continue
        if mfi_obj.get_charge_date() > end_date:
            break
        filtered_mfi_objs.append(mfi_obj)
    return filtered_mfi_objs


def get_price_from_csv(csv_file_path, begin_date, end_date):
    mfi_obj_array = []
    with open(csv_file_path) as f:
        csv_data = csv.reader(f)
        for mfi_line in islice(csv_data, 1, None):
            if mfi_line.__len__() > 3:
                mfi_obj = MfiObj(mfi_line[0], float(mfi_line[1]), float(mfi_line[2]), float(mfi_line[3]), float(mfi_line[6]))
                mfi_obj_array.append(mfi_obj)
    if mfi_obj_array.__len__() == 0:
        print("请确认文件是否正确：" + csv_file_path)
        raise
    return filter_begin_end_date(mfi_obj_array, begin_date, end_date)
