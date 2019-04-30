import numpy


def calculate_income(r1, t, mfi_array, depot_obj):
    last_mfi_obj = mfi_array[0]
    for index in range(t, mfi_array.__len__(), t):
        if (index + t) > mfi_array.__len__():
            break
        cur_mfi_obj = mfi_array[index]
        (avg, std) = __get_avg_std(mfi_array[index - t + 1:index + 1])
        low_limit = avg - r1 * std
        up_limit = avg + r1 * std
        if cur_mfi_obj.mfi_six_day_avg < low_limit:  # 当六日平均小于安全区间
            if cur_mfi_obj.close_charge > last_mfi_obj.close_charge:  # 如果累计涨幅是正的，说明上涨，赶紧买！
                depot_obj.buy(cur_mfi_obj)
            elif cur_mfi_obj.mfi > last_mfi_obj.mfi:  # 如果累计涨幅是负的，且指标较上交易点高，要赶紧卖
                depot_obj.sell(cur_mfi_obj)
        if cur_mfi_obj.mfi_six_day_avg > up_limit:  # 当六日平均大于安全区间
            if cur_mfi_obj.close_charge < last_mfi_obj.close_charge:  # 当累计涨幅是负的，说明下跌，赶紧卖
                depot_obj.sell(cur_mfi_obj)
            elif cur_mfi_obj.mfi < last_mfi_obj.mfi:  # 当累计涨幅是正的，且mfi比上个交易点低，赶紧买
                depot_obj.buy(cur_mfi_obj)
        last_mfi_obj = cur_mfi_obj


def __get_avg_std(mfi_array):
    std_array = []
    for mfi_obj in mfi_array:
        std_array.append(mfi_obj.mfi)
    avg = numpy.mean(std_array)
    std = numpy.sqrt(((std_array - avg) ** 2).sum() / (std_array.__len__() - 1))
    return avg, std  # ddof=1无偏差算标准差，即除以 N-1,若ddof=0则为带偏差标准差，即除以 N
