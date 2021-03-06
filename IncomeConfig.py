import time


class IncomeConfig:
    __begin_date = '2014-01-01'
    __end_date = '2018-12-31'
    file_path = './mfi.csv'  # 列顺序：时间	MFI原始	MFI六日平均	收盘价	累计涨幅
    r1 = [0.25, 3]  # 标准差
    r1_step = 0.05
    t = [10, 300]
    t_step = 10
    transfer_fee = 0.0001  # 手续费
    amount = 10000000  # 账户初始总额

    __format_begin_date = time.strptime(__begin_date, '%Y-%m-%d')
    __format_end_date = time.strptime(__end_date, '%Y-%m-%d')

    def get_begin_date(self):
        return self.__format_begin_date

    def get_end_date(self):
        return self.__format_end_date

    def get_r1_low_limit(self):
        return self.r1[0]

    def get_r1_up_limit(self):
        return self.r1[1]

    def get_r1_ranges(self):
        return int((self.get_r1_up_limit() - self.get_r1_low_limit()) / self.r1_step + 1)

    def get_t_low_limit(self):
        return self.t[0]

    def get_t_up_limit(self):
        return self.t[1]

    def get_t_ranges(self):
        return int((self.get_t_up_limit() - self.get_t_low_limit()) / self.t_step + 1)
