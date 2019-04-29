from IncomeConfig import *
from obj.DepotObj import *
from price.CalculateIncome import *
from price.GetPriceFromCsv import *

config = IncomeConfig()
mfi_array = get_price_from_csv(config.file_path, config.get_begin_date(), config.get_end_date())
max_r_rate = 0
max_r_rate_t = 0
max_r_rate_r1 = 0
max_r_rate_r2 = 0

for t_index in range(config.get_t_ranges()):
    t = config.get_t_low_limit() + config.t_step * t_index
    for r1_index in range(config.get_r1_ranges()):
        r1 = config.get_r1_low_limit() + config.r1_step * r1_index
        for r2_index in range(config.get_r2_ranges()):
            r2 = config.get_r2_low_limit() + config.r2_step * r2_index
            depot_obj = DepotObj(config.amount, config.transfer_fee)
            calculate_income(r1, r2, t, mfi_array, depot_obj)
            r_rate = depot_obj.get_r_rate()
            if r_rate > max_r_rate:
                max_r_rate = r_rate
                max_r_rate_t = t
                max_r_rate_r1 = r1
                max_r_rate_r2 = r2

print("最佳收益率：" + str(max_r_rate))
print("T：" + str(max_r_rate_t))
print("r1：" + str(max_r_rate_r1))
print("r2：" + str(max_r_rate_r2))
