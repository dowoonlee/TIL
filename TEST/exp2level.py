import numpy as np
import matplotlib.pyplot as plt



def lv2exp(lv):
    if (lv<=50):
        exp = lv**3*(100-lv)/50
    elif (lv<=68):
        exp = lv ** 3 * (100 - lv) / 100
    else:
        exp = lv**3 *(160-lv)/100
    return int(exp)


lvs = [i for i in range(1, 100)]
exp4lv = [lv2exp(i) for i in lvs]
cum_exp = [0]*len(lvs)
cum_exp [0] = exp4lv[0]
for i in range(1, len(lvs)):
    cum_exp[i] = cum_exp[i-1]+exp4lv[i]


print(cum_exp[-1]/2)
