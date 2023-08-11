def make_readable(seconds):
    # 1. convert seconds input to designated variables
    hh = seconds // 3600
    remaining_sec = seconds % 3600
    mm = remaining_sec // 60
    remaining_sec = remaining_sec % 60
    ss = remaining_sec
    # no remainder for ss


    # 2. convert the displayed output to the correct format for ease of understanding
    print(str(hh) + ":" + str(mm) + ":" + str(ss))
    return f"{hh:02d}:{mm:02d}:{ss:02d}"



print(make_readable(3600))