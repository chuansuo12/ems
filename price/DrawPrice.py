def draw_r_rate(depot_obj, t, r1):
    import matplotlib.pyplot as plt
    x_array = []
    y_array = []
    for bis_track in depot_obj.bis_tracks:
        x_array.append(bis_track.charge_date)
        y_array.append(bis_track.r_rate)
    plt.title("T:" + str(t) + ", r1:" + str(r1))
    plt.xlabel("date")
    plt.ylabel("return_rate")
    plt.plot(x_array, y_array)
    plt.show()


def draw_close_charge(mfi_obj_array):
    import matplotlib.pyplot as plt
    x_array = []
    y_array = []
    for mfi_obj in mfi_obj_array:
        x_array.append(mfi_obj.charge_date)
        y_array.append(mfi_obj.close_charge)
    plt.title("close_charge_history")
    plt.xlabel("date")
    plt.ylabel("close_charge")
    plt.plot(x_array, y_array)
    plt.show()
