import time


class MfiObj:
    def __init__(self, charge_date, mfi, mfi_six_day_avg, close_charge, cumulative_increase):
        self.charge_date = charge_date
        self.mfi = mfi
        self.mfi_six_day_avg = mfi_six_day_avg
        self.close_charge = close_charge
        self.cumulative_increase = cumulative_increase

    def get_charge_date(self):
        return time.strptime(self.charge_date, '%Y/%m/%d')
