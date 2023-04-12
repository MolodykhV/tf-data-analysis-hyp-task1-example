import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt, y_success, y_cnt):
    p_control = x_success / x_cnt
    p_test = y_success / y_cnt

    SE = np.sqrt((p_control * (1 - p_control) / x_cnt) + (p_test * (1 - p_test) / y_cnt))

    z = (p_test - p_control) / SE
    z_critical = norm.ppf(1 - 0.05 / 2)

    return z > z_critical
