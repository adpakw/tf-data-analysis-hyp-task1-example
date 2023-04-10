import pandas as pd
import numpy as np
import math

chat_id = 451783978 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  p1 = x_success / x_cnt
  p2 = y_success / y_cnt
  p = (x_success + y_success) / (x_cnt + y_cnt)
  z = (p2 - p1) / sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt))
  z_alpha = norm.ppf(1 - 0.06)
  return math.fabs(z) > z_alpha
