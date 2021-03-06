import argparse
import model
import serialize
import view


class KeysController:
    consump = model.Model("base.pickle")

    parser = argparse.ArgumentParser(description='Keys controller for Fuel Consumption.')

    parser.add_argument("-d", action='store',
                        help="add date value in format: 'DD-MM-YYYY'")
    parser.add_argument("-l", action='store',
                        help="add length passed")
    parser.add_argument("-c", action='store',
                        help="add coefficient of consumption")

    parser.add_argument("-fuel", action='store_true',
                        help="print general fuel used")
    parser.add_argument("-len", action='store_true',
                        help="print general len passed")
    parser.add_argument("-date", action='store',
                        help="print info by date")
    parser.add_argument("-print", action='store_true',
                        help="print all info")

    def __init__(self):
        self.args = self.parser.parse_args()
        if self.args.d and self.args.l and self.args.c:
            self.add_info()
        elif self.args.fuel:
            print(self.consump.get_general_fuel_used())
        elif self.args.len:
            print(self.consump.get_general_length())
        elif self.args.date:
            self.show_by_date()
        elif self.args.print:
            self.show_all_info(self.consump.records)

    def add_info(self):
        self.consump.add_data(self.args.d, self.args.l, self.args.c)
        self.consump.save_all("base.pickle")

    def show_by_date(self):
        if self.consump.check_validity_of_date(self.args.date):
            records_daily = self.consump.find_by_date(self.args.date)
            KeysController.show_all_info(records_daily)

    @staticmethod
    def show_all_info(records_list):
        for item in records_list:
            view.View.print_record(item, model.Model.get_used_fuel(item))

if __name__ == "__main__":
    k = KeysController()
