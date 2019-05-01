from obj.BisTrackObj import *


class DepotObj:
    def __init__(self, amount, transfer_fee):
        self.__init_amount = amount
        self.amount = amount
        self.points = 0
        self.transfer_fee = transfer_fee
        self.bis_tracks = []

    def is_have_point(self):
        return self.points != 0

    def buy(self, mfi_obj):
        if self.is_have_point():
            return
        self.pay_transfer_fee()
        self.points = self.amount / mfi_obj.close_charge
        self.record_r_rate_track(mfi_obj, 'buy')
        # print("buy,charge_date:" + str(mfi_obj.charge_date))

    def sell(self, mfi_obj):
        if not self.is_have_point():
            return
        self.amount = self.points * mfi_obj.close_charge
        self.pay_transfer_fee()
        self.points = 0
        self.record_r_rate_track(mfi_obj, 'sell')
        # print("sell,charge_date:" + str(mfi_obj.charge_date))

    def record_r_rate_track(self, mfi_obj, act):
        r_rate = self.get_r_rate()
        bis_track_obj = BisTrackObj(mfi_obj.charge_date, r_rate, act)
        self.bis_tracks.append(bis_track_obj)

    def get_r_rate(self):
        return (self.amount - self.__init_amount) / self.__init_amount

    def pay_transfer_fee(self):
        self.amount = self.amount * (1 - self.transfer_fee)
