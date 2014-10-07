# -*- coding: UTF-8 -*-



def count(start, stop):
    start = int(start)
    stop = int(stop)
    msg = start
    comma = ","
    if start >= stop:
        while start > stop:
            start -= 1
            msg = str(msg) + str(comma) + str(start)
    else:
        if start == stop:
            msg = start
            msg = str(msg)
        else:
            while start < stop:
                start += 1
                msg = str(msg)
                msg = str(msg) + str(comma) + str(start)
    return str(msg)











