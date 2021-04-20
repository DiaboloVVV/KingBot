import datetime


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

    # SAVING MESSAGE ID FROM GIVEAWAY


def giveway_idFunction(msg_id):
    giveway_idFunction.ids = msg_id

    #  NOT WORKING YET
def timeRemaning(seconds):
    print(f"{seconds} this seconds")
    a = str(seconds // 3600)
    print(a + 'this a')
    # print('more than 48h but works')
    b = str((seconds % 3600) // 60)
    print(b + 'this b')
    if int(a) > 48:
        c = str((seconds // 3600) // 24)
        d = "{} days {} hours".format(c, b)
        return d
    else:
        d = "{} hours {} mins".format(a, b)
        return d
