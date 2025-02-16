import math

def net_present_value(capital, rate, period):
    return capital * math.pow((1 + rate/100), period)