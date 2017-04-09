import view
from model import *


def show_all(records):
    view.record_names()
    for item in records:
        view.print_record(item, get_used_fuel(item))


def show_summary(records):
    view.print_summary(get_general_length(records), get_general_fuel_used(records))


def show_by_date():
    pass


def show_period():
    pass


def add_record(item_list, records):
    record = Record(item_list[0], item_list[1], item_list[2])
    records.append(record)


def main_func():
    """ readiness level: 1, 4, 7"""
    choice = ''
    records = initialise("fuel_consumption.pickle")
    while choice != "7":
        choice = str(view.menu())
        if choice == "1":
            show_all(records)
        elif choice == "2":
            show_summary(records)
        elif choice == "3":
            pass
        elif choice == "6":
            add_record(view.enter_trip_details(), records)
        elif choice == "7":
            save_all(records, "fuel_consumption.pickle")
        else:
            pass


main_func()