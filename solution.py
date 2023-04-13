import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt, y_success, y_cnt):
    p1, p2 = x_success/x_cnt, y_success/y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z = (p1 - p2)/np.sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt))
    
    return z < -1.645
