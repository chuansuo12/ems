import time


class IncomeConfig:
    __begin_date = '2008-04-08'
    __end_date = '2016-04-10'
    file_path = './mfi.csv'  # 要保证第一列是时间，第二列是MFI，第三列是六日平均
    r1 = [0.35, 0.65]  # 下限参数
    r1_step = 0.005
    r2 = [0.35, 0.65]  # 上线参数
    r2_step = 0.005
    t = [10, 300]
    t_step = 10
    transfer_fee = 0.0003  # 手续费
    amount = 100000  # 账户初始总额

    def get_begin_date(self):
        return time.strptime(self.__begin_date, '%Y-%m-%d')

    def get_end_date(self):
        return time.strptime(self.__end_date, '%Y-%m-%d')

    def get_r1_low_limit(self):
        return self.r1[0]

    def get_r1_up_limit(self):
        return self.r1[1]

    def get_r1_ranges(self):
        return int((self.get_r1_up_limit() - self.get_r1_low_limit()) / self.r1_step)

    def get_r2_low_limit(self):
        return self.r2[0]

    def get_r2_up_limit(self):
        return self.r2[1]

    def get_r2_ranges(self):
        return int((self.get_r2_up_limit() - self.get_r2_low_limit()) / self.r2_step)

    def get_t_low_limit(self):
        return self.t[0]

    def get_t_up_limit(self):
        return self.t[1]

    def get_t_ranges(self):
        return int((self.get_t_up_limit() - self.get_t_low_limit()) / self.t_step)
